# coding: utf-8
"""HP_TcpPull 类"""
import ctypes

import HPSocket.helper as helper
import HPSocket.pyhpsocket as HPSocket


class HP_TcpPull:
    Listener = None
    target = ('', 0)
    __target__ = None
    EnHandleResult = HPSocket.EnHandleResult

    def EventDescription(fn):
        def arguments(*args, **kwargs):
            retval = fn(*args, **kwargs)
            return retval if isinstance(retval, ctypes.c_int) else HPSocket.EnHandleResult.HR_OK

        return arguments

    @EventDescription
    def OnHandShake(self, Sender, ConnID):
        return HPSocket.EnHandleResult.HR_OK

    @EventDescription
    def OnSendWarp(self, Sender, ConnID, pData, Length):
        HPSocket.ctypes.string_at(pData, Length)
        return self.OnSend(Sender, ConnID, HPSocket.ctypes.string_at(pData, Length))

    @EventDescription
    def OnSend(self, Sender, ConnID, Data):
        return HPSocket.EnHandleResult.HR_OK

    @EventDescription
    def OnClose(self, Sender, ConnID, Operation, ErrorCode):
        return HPSocket.EnHandleResult.HR_OK

    ### Pull 模型特有的两个事件 ###
    @EventDescription
    def OnReceiveHead(self, Sender, ConnID, Seq: int, Length: int, raw:bytes):
        """若要使得该事件被触发，必须不重写 OnReceive 事件并且传输协议同官方 DEMO 一致，或者在重写 OnReceive 的时候有意识的调用本函数。"""
        return HPSocket.EnHandleResult.HR_OK

    @EventDescription
    def OnReceiveBody(self, Sender, ConnID, Body: bytes, raw:bytes):
        """若要使得该事件被触发，必须不重写 OnReceive 事件并且传输协议同官方 DEMO 一致，或者在重写 OnReceive 的时候有意识的调用本函数。"""
        return HPSocket.EnHandleResult.HR_OK


class HP_TcpPullServer(HP_TcpPull):
    Server = None

    def __init__(self):
        self.Listener = HPSocket.Create_HP_TcpPullServerListener()
        self.Server = HPSocket.Create_HP_TcpPullServer(self.Listener)

        self.OnPrepareListenHandle = HPSocket.HP_FN_Server_OnPrepareListen(self.OnPrepareListen)
        self.OnAcceptHandle = HPSocket.HP_FN_Server_OnAccept(self.OnAccept)
        self.OnHandShakeHandle = HPSocket.HP_FN_Server_OnHandShake(self.OnHandShake)
        self.OnSendHandle = HPSocket.HP_FN_Server_OnSend(self.OnSendWarp)
        self.OnReceiveHandle = HPSocket.HP_FN_Server_OnPullReceive(self.OnReceive)
        self.OnCloseHandle = HPSocket.HP_FN_Server_OnClose(self.OnClose)
        self.OnShutdownHandle = HPSocket.HP_FN_Server_OnShutdown(self.OnShutdown)

        HPSocket.HP_Set_FN_Server_OnPrepareListen(self.Listener, self.OnPrepareListenHandle)
        HPSocket.HP_Set_FN_Server_OnAccept(self.Listener, self.OnAcceptHandle)
        HPSocket.HP_Set_FN_Server_OnHandShake(self.Listener, self.OnHandShakeHandle)
        HPSocket.HP_Set_FN_Server_OnSend(self.Listener, self.OnSendHandle)
        HPSocket.HP_Set_FN_Server_OnPullReceive(self.Listener, self.OnReceiveHandle)
        HPSocket.HP_Set_FN_Server_OnClose(self.Listener, self.OnCloseHandle)
        HPSocket.HP_Set_FN_Server_OnShutdown(self.Listener, self.OnShutdownHandle)

    def __del__(self):
        HPSocket.Destroy_HP_TcpPullServer(self.Server)
        HPSocket.Destroy_HP_TcpPullServerListener(self.Listener)

    def Send(self, Sender, ConnID, Data):
        return HPSocket.HP_Server_Send(Sender, ConnID, Data)

    def Start(self, host, port):
        self.target = (host, port)
        self.__target__ = (ctypes.create_string_buffer(str.encode(host)), ctypes.c_ushort(port))
        return HPSocket.HP_Server_Start(self.Server, self.__target__[0], self.__target__[1])

    ### 用户可以覆盖下面的方法以实现业务应用 ###
    @HP_TcpPull.EventDescription
    def OnPrepareListen(self, Sender, SocketHandler):
        return HPSocket.EnHandleResult.HR_OK

    @HP_TcpPull.EventDescription
    def OnAccept(self, Sender, ConnID, Client):
        return HPSocket.EnHandleResult.HR_OK

    @HP_TcpPull.EventDescription
    def OnShutdown(self, Sender):
        return HPSocket.EnHandleResult.HR_OK

    @HP_TcpPull.EventDescription
    def OnReceive(self, Sender, ConnID, Length):
        # 在使用默认的数据结构情况下，数据包的组织形式是 Head-Body 交错
        pInfo = HPSocket.HP_Server_GetConnectionExtra(Sender, ConnID, helper.TPkgInfo)
        if pInfo:
            required = pInfo.length
            remain = Length
            while remain >= required:
                remain -= required
                Buf = helper.CBuffer(required)
                result = HPSocket.HP_TcpPullServer_Fetch(Sender, ConnID, Buf.Ptr(), required)  # 这里获取 Body
                if result == HPSocket.EnFetchResult.FR_OK:
                    if pInfo.is_header:
                        (Seq,Length)=helper.UnpackTPkgHeader(Buf.Contents().raw)
                        self.OnReceiveHead(Sender=Sender, ConnID=ConnID, Seq=Seq, Length=Length, raw=Buf.Contents().raw)
                        required = Length  # 从 head 切换到 body
                    else:
                        self.OnReceiveBody(Sender=Sender, ConnID=ConnID, Body=Buf.Contents().raw, raw=Buf.Contents().raw)
                        required = helper.TPkgHeaderSize  # 从 body 切换到 head
                    pInfo.is_header = not pInfo.is_header
                    pInfo.length = required
                    # if not self.Send(Sender, ConnID, Buf.Ptr()):
                    #     return HPSocket.EnHandleResult.HR_ERROR
        return HPSocket.EnHandleResult.HR_OK


class HP_TcpPullClient(HP_TcpPull):
    Client = None
    SEQ = 0
    pkgInfo = helper.TPkgInfo()

    def __init__(self):
        self.Listener = HPSocket.Create_HP_TcpPullClientListener()
        self.Client = HPSocket.Create_HP_TcpPullClient(self.Listener)

        self.OnPrepareConnectHandle = HPSocket.HP_FN_Client_OnPrepareConnect(self.OnPrepareConnect)
        self.OnConnectHandle = HPSocket.HP_FN_Client_OnConnect(self.OnConnect)
        self.OnHandShakeHandle = HPSocket.HP_FN_Client_OnHandShake(self.OnHandShake)
        self.OnSendHandle = HPSocket.HP_FN_Client_OnSend(self.OnSendWarp)
        self.OnReceiveHandle = HPSocket.HP_FN_Client_OnPullReceive(self.OnReceive)
        self.OnCloseHandle = HPSocket.HP_FN_Client_OnClose(self.OnClose)

        HPSocket.HP_Set_FN_Client_OnPrepareConnect(self.Listener, self.OnPrepareConnectHandle)
        HPSocket.HP_Set_FN_Client_OnConnect(self.Listener, self.OnConnectHandle)
        HPSocket.HP_Set_FN_Client_OnHandShake(self.Listener, self.OnHandShakeHandle)
        HPSocket.HP_Set_FN_Client_OnSend(self.Listener, self.OnSendHandle)
        HPSocket.HP_Set_FN_Client_OnPullReceive(self.Listener, self.OnReceiveHandle)
        HPSocket.HP_Set_FN_Client_OnClose(self.Listener, self.OnCloseHandle)

    def __del__(self):
        HPSocket.Destroy_HP_TcpPullClient(self.Client)
        HPSocket.Destroy_HP_TcpPullClientListener(self.Listener)

    def Send(self, Sender, Data):
        return HPSocket.HP_Client_Send(Sender, Data)

    def Start(self, host, port):
        self.target = (host, port)
        self.__target__ = (ctypes.create_string_buffer(str.encode(host, encoding='GBK')), ctypes.c_ushort(port))
        AsyncConn = ctypes.c_bool(False)
        self.pkgInfo.Reset()
        return HPSocket.HP_Client_Start(self.Client, self.__target__[0], self.__target__[1], AsyncConn)

    ### 用户可以覆盖下面的方法以实现业务应用 ###
    @HP_TcpPull.EventDescription
    def OnPrepareConnect(self, Sender, ConnID, Socket):
        return HPSocket.EnHandleResult.HR_OK

    @HP_TcpPull.EventDescription
    def OnConnect(self, Sender, ConnID):
        return HPSocket.EnHandleResult.HR_OK

    @HP_TcpPull.EventDescription
    def OnReceive(self, Sender, ConnID, Length):
        # 在使用默认的数据结构情况下，数据包的组织形式是 Head-Body 交错
        required = self.pkgInfo.length
        remain = Length
        while remain >= required:
            remain -= required
            Buf = helper.CBuffer(required)
            result = HPSocket.HP_TcpPullClient_Fetch(Sender, Buf.Ptr(), required)  # 这里获取 Body
            if result == HPSocket.EnFetchResult.FR_OK:
                if self.pkgInfo.is_header:
                    (Seq, Length) = helper.UnpackTPkgHeader(Buf.Contents().raw)
                    self.OnReceiveHead(Sender=Sender, ConnID=ConnID, Seq=Seq, Length=Length, raw=Buf.Contents().raw)
                    required = Length  # 从 head 切换到 body
                else:
                    self.OnReceiveBody(Sender=Sender, ConnID=ConnID, Body=Buf.Contents().raw, raw=Buf.Contents().raw)
                    required = helper.TPkgHeaderSize  # 从 body 切换到 head
                self.pkgInfo.is_header = not self.pkgInfo.is_header
                self.pkgInfo.length = required
        return HPSocket.EnHandleResult.HR_OK

class HP_TcpPullAgent(HP_TcpPull):
    Agent = None
    SEQ = 0
    pkgInfo = {}
    ConnIDPool = {}
    LatestConnID = 0

    def __init__(self):
        self.Listener = HPSocket.Create_HP_TcpPullAgentListener()
        self.Agent = HPSocket.Create_HP_TcpPullAgent(self.Listener)

        self.OnPrepareConnectHandle = HPSocket.HP_FN_Agent_OnPrepareConnect(self.OnPrepareConnect)
        self.OnConnectHandle = HPSocket.HP_FN_Agent_OnConnect(self.OnConnect)
        self.OnHandShakeHandle = HPSocket.HP_FN_Agent_OnHandShake(self.OnHandShake)
        self.OnSendHandle = HPSocket.HP_FN_Agent_OnSend(self.OnSendWarp)
        self.OnReceiveHandle = HPSocket.HP_FN_Agent_OnPullReceive(self.OnReceive)
        self.OnCloseHandle = HPSocket.HP_FN_Agent_OnClose(self.OnClose)
        self.OnShutdownHandle = HPSocket.HP_FN_Agent_OnShutdown(self.OnShutdown)

        HPSocket.HP_Set_FN_Agent_OnPrepareConnect(self.Listener, self.OnPrepareConnectHandle)
        HPSocket.HP_Set_FN_Agent_OnConnect(self.Listener, self.OnConnectHandle)
        HPSocket.HP_Set_FN_Agent_OnHandShake(self.Listener, self.OnHandShakeHandle)
        HPSocket.HP_Set_FN_Agent_OnSend(self.Listener, self.OnSendHandle)
        HPSocket.HP_Set_FN_Agent_OnPullReceive(self.Listener, self.OnReceiveHandle)
        HPSocket.HP_Set_FN_Agent_OnClose(self.Listener, self.OnCloseHandle)

    def __del__(self):
        HPSocket.Destroy_HP_TcpPullAgent(self.Agent)
        HPSocket.Destroy_HP_TcpPullAgentListener(self.Listener)

    def Send(self, Sender, ConnID, Data):
        return HPSocket.HP_Agent_Send(Sender, ConnID, Data)

    def Start(self, BindAddress):
        self.BindAddress = ctypes.create_string_buffer(bytes(BindAddress, 'GBK'), len(BindAddress))
        self.ConnIDPool.clear()
        self.pkgInfo.clear()
        self.LatestConnID = 0
        HPSocket.HP_TcpAgent_SetReuseAddress(self.Agent, ctypes.c_bool(True))
        return HPSocket.HP_Agent_Start(self.Agent, self.BindAddress, ctypes.c_bool(False))

    def Connect(self, host, port):
        __target__ = (ctypes.create_string_buffer(str.encode(host)), ctypes.c_ushort(port))
        cLConnID = ctypes.c_ulong(self.LatestConnID)
        if HPSocket.HP_Agent_Connect(self.Agent, __target__[0], __target__[1], ctypes.byref(cLConnID)):
            self.LatestConnID = cLConnID.value
            self.ConnIDPool[self.LatestConnID] = __target__
            self.pkgInfo[self.LatestConnID] = helper.TPkgInfo()
            return self.LatestConnID
        else:
            return None

    def DisConnect(self, ConnID):
        HPSocket.HP_Agent_Disconnect(self.Agent, ctypes.c_int(ConnID), ctypes.c_bool(True))
        del self.ConnIDPool[ConnID]

    def Stop(self):
        if not HPSocket.HP_Agent_Stop(self.Agent):
            raise Exception('Cannot stop agent!')

    ### 用户可以覆盖下面的方法以实现业务应用 ###
    @HP_TcpPull.EventDescription
    def OnPrepareConnect(self, Sender, ConnID, Socket):
        return HPSocket.EnHandleResult.HR_OK

    @HP_TcpPull.EventDescription
    def OnConnect(self, Sender, ConnID):
        return HPSocket.EnHandleResult.HR_OK

    @HP_TcpPull.EventDescription
    def OnShutdown(self, Sender):
        return HPSocket.EnHandleResult.HR_OK

    @HP_TcpPull.EventDescription
    def OnReceive(self, Sender, ConnID, Length):
        # 在使用默认的数据结构情况下，数据包的组织形式是 Head-Body 交错
        required = self.pkgInfo[ConnID].length
        remain = Length
        while remain >= required:
            remain -= required
            Buf = helper.CBuffer(required)
            result = HPSocket.HP_TcpPullAgent_Fetch(Sender, ConnID, Buf.Ptr(), required)  # 这里获取 Body
            if result == HPSocket.EnFetchResult.FR_OK:
                if self.pkgInfo[ConnID].is_header:
                    (Seq, Length) = helper.UnpackTPkgHeader(Buf.Contents().raw)
                    self.OnReceiveHead(Sender=Sender, ConnID=ConnID, Seq=Seq, Length=Length, raw=Buf.Contents().raw)
                    required = Length  # 从 head 切换到 body
                else:
                    self.OnReceiveBody(Sender=Sender, ConnID=ConnID, Body=Buf.Contents().raw, raw=Buf.Contents().raw)
                    required = helper.TPkgHeaderSize  # 从 body 切换到 head
                self.pkgInfo[ConnID].is_header = not self.pkgInfo[ConnID].is_header
                self.pkgInfo[ConnID].length = required
        return HPSocket.EnHandleResult.HR_OK
