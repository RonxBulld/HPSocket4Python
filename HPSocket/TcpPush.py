# coding: utf-8
"""HP_Tcp 类"""
import ctypes

import HPSocket.helper as helper
import HPSocket.pyhpsocket as HPSocket


class HP_TcpPush:
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
        return self.OnSend(Sender=Sender, ConnID=ConnID, Data=ctypes.string_at(pData, Length), Length=Length)

    @EventDescription
    def OnSend(self, Sender, ConnID, Data, Length):
        return HPSocket.EnHandleResult.HR_OK

    @EventDescription
    def OnClose(self, Sender, ConnID, Operation, ErrorCode):
        return HPSocket.EnHandleResult.HR_OK

    @EventDescription
    def OnReceiveWarp(self, Sender, ConnID, pData, Length):
        return self.OnReceive(Sender=Sender, ConnID=ConnID, Data=ctypes.string_at(pData, Length), Length=Length)

    @EventDescription
    def OnReceive(self, Sender, ConnID, Data, Length):
        return HPSocket.EnHandleResult.HR_OK

class HP_TcpPushServer(HP_TcpPush):
    Server = None

    def __init__(self):
        self.Listener = HPSocket.Create_HP_TcpServerListener()
        self.Server = HPSocket.Create_HP_TcpServer(self.Listener)

        self.OnPrepareListenHandle = HPSocket.HP_FN_Server_OnPrepareListen(self.OnPrepareListen)
        self.OnAcceptHandle = HPSocket.HP_FN_Server_OnAccept(self.OnAccept)
        self.OnHandShakeHandle = HPSocket.HP_FN_Server_OnHandShake(self.OnHandShake)
        self.OnSendHandle = HPSocket.HP_FN_Server_OnSend(self.OnSendWarp)
        self.OnReceiveHandle = HPSocket.HP_FN_Server_OnReceive(self.OnReceiveWarp)
        self.OnCloseHandle = HPSocket.HP_FN_Server_OnClose(self.OnClose)
        self.OnShutdownHandle = HPSocket.HP_FN_Server_OnShutdown(self.OnShutdown)

        HPSocket.HP_Set_FN_Server_OnPrepareListen(self.Listener, self.OnPrepareListenHandle)
        HPSocket.HP_Set_FN_Server_OnAccept(self.Listener, self.OnAcceptHandle)
        HPSocket.HP_Set_FN_Server_OnHandShake(self.Listener, self.OnHandShakeHandle)
        HPSocket.HP_Set_FN_Server_OnSend(self.Listener, self.OnSendHandle)
        HPSocket.HP_Set_FN_Server_OnReceive(self.Listener, self.OnReceiveHandle)
        HPSocket.HP_Set_FN_Server_OnClose(self.Listener, self.OnCloseHandle)
        HPSocket.HP_Set_FN_Server_OnShutdown(self.Listener, self.OnShutdownHandle)

    def __del__(self):
        HPSocket.Destroy_HP_TcpServer(self.Server)
        HPSocket.Destroy_HP_TcpServerListener(self.Listener)

    def Send(self, Sender, ConnID, Data):
        # if not isinstance(Data, list):
        #     Data = [ Data ]
        # return HPSocket.HP_Server_Sendets(Server=Sender, ConnID=ConnID, Bufs=Data)
        return HPSocket.HP_Server_Send(Server=Sender, ConnID=ConnID, Buffer=Data)

    def Start(self, host, port):
        self.target = (host, port)
        self.__target__ = (ctypes.create_string_buffer(str.encode(host)), ctypes.c_ushort(port))
        return HPSocket.HP_Server_Start(self.Server, self.__target__[0], self.__target__[1])

    ### 用户可以覆盖下面的方法以实现业务应用 ###
    @HP_TcpPush.EventDescription
    def OnPrepareListen(self, Sender, SocketHandler):
        return HPSocket.EnHandleResult.HR_OK

    @HP_TcpPush.EventDescription
    def OnAccept(self, Sender, ConnID, Client):
        return HPSocket.EnHandleResult.HR_OK

    @HP_TcpPush.EventDescription
    def OnShutdown(self, Sender):
        return HPSocket.EnHandleResult.HR_OK


class HP_TcpPushClient(HP_TcpPush):
    Client = None
    SEQ = 0

    def __init__(self):
        self.Listener = HPSocket.Create_HP_TcpClientListener()
        self.Client = HPSocket.Create_HP_TcpClient(self.Listener)

        self.OnPrepareConnectHandle = HPSocket.HP_FN_Client_OnPrepareConnect(self.OnPrepareConnect)
        self.OnConnectHandle = HPSocket.HP_FN_Client_OnConnect(self.OnConnect)
        self.OnHandShakeHandle = HPSocket.HP_FN_Client_OnHandShake(self.OnHandShake)
        self.OnSendHandle = HPSocket.HP_FN_Client_OnSend(self.OnSendWarp)
        self.OnReceiveHandle = HPSocket.HP_FN_Client_OnReceive(self.OnReceiveWarp)
        self.OnCloseHandle = HPSocket.HP_FN_Client_OnClose(self.OnClose)

        HPSocket.HP_Set_FN_Client_OnPrepareConnect(self.Listener, self.OnPrepareConnectHandle)
        HPSocket.HP_Set_FN_Client_OnConnect(self.Listener, self.OnConnectHandle)
        HPSocket.HP_Set_FN_Client_OnHandShake(self.Listener, self.OnHandShakeHandle)
        HPSocket.HP_Set_FN_Client_OnSend(self.Listener, self.OnSendHandle)
        HPSocket.HP_Set_FN_Client_OnReceive(self.Listener, self.OnReceiveHandle)
        HPSocket.HP_Set_FN_Client_OnClose(self.Listener, self.OnCloseHandle)

    def __del__(self):
        HPSocket.Destroy_HP_TcpClient(self.Client)
        HPSocket.Destroy_HP_TcpClientListener(self.Listener)

    def Send(self, Sender, Data):
        return HPSocket.HP_Client_Send(Client=Sender, Buffer=Data)

    def Start(self, host, port):
        self.target = (host, port)
        self.__target__ = (ctypes.create_string_buffer(str.encode(host, encoding='GBK')), ctypes.c_ushort(port))
        AsyncConn = ctypes.c_bool(False)
        return HPSocket.HP_Client_Start(self.Client, self.__target__[0], self.__target__[1], AsyncConn)

    ### 用户可以覆盖下面的方法以实现业务应用 ###
    @HP_TcpPush.EventDescription
    def OnPrepareConnect(self, Sender, ConnID, Socket):
        return HPSocket.EnHandleResult.HR_OK

    @HP_TcpPush.EventDescription
    def OnConnect(self, Sender, ConnID):
        return HPSocket.EnHandleResult.HR_OK


class HP_TcpPushAgent(HP_TcpPush):
    Agent = None
    SEQ = 0
    ConnIDPool = {}
    LatestConnID = 0

    def __init__(self):
        self.Listener = HPSocket.Create_HP_TcpAgentListener()
        self.Agent = HPSocket.Create_HP_TcpAgent(self.Listener)

        self.OnPrepareConnectHandle = HPSocket.HP_FN_Agent_OnPrepareConnect(self.OnPrepareConnect)
        self.OnConnectHandle = HPSocket.HP_FN_Agent_OnConnect(self.OnConnect)
        self.OnHandShakeHandle = HPSocket.HP_FN_Agent_OnHandShake(self.OnHandShake)
        self.OnSendHandle = HPSocket.HP_FN_Agent_OnSend(self.OnSendWarp)
        self.OnReceiveHandle = HPSocket.HP_FN_Agent_OnReceive(self.OnReceiveWarp)
        self.OnCloseHandle = HPSocket.HP_FN_Agent_OnClose(self.OnClose)
        self.OnShutdownHandle = HPSocket.HP_FN_Agent_OnShutdown(self.OnShutdown)

        HPSocket.HP_Set_FN_Agent_OnPrepareConnect(self.Listener, self.OnPrepareConnectHandle)
        HPSocket.HP_Set_FN_Agent_OnConnect(self.Listener, self.OnConnectHandle)
        HPSocket.HP_Set_FN_Agent_OnHandShake(self.Listener, self.OnHandShakeHandle)
        HPSocket.HP_Set_FN_Agent_OnSend(self.Listener, self.OnSendHandle)
        HPSocket.HP_Set_FN_Agent_OnReceive(self.Listener, self.OnReceiveHandle)
        HPSocket.HP_Set_FN_Agent_OnClose(self.Listener, self.OnCloseHandle)

    def __del__(self):
        HPSocket.Destroy_HP_TcpAgent(self.Agent)
        HPSocket.Destroy_HP_TcpAgentListener(self.Listener)

    def Send(self, Sender, ConnID, Data):
        return HPSocket.HP_Agent_Send(Sender, ConnID, Data)

    def Start(self, BindAddress):
        self.BindAddress = ctypes.create_string_buffer(bytes(BindAddress, 'GBK'), len(BindAddress))
        self.ConnIDPool.clear()
        self.LatestConnID = 0
        HPSocket.HP_TcpAgent_SetReuseAddress(self.Agent, ctypes.c_bool(True))
        return HPSocket.HP_Agent_Start(self.Agent, self.BindAddress, ctypes.c_bool(False))

    def Connect(self, host, port):
        __target__ = (ctypes.create_string_buffer(str.encode(host)), ctypes.c_ushort(port))
        cLConnID = ctypes.c_ulong(self.LatestConnID)
        if HPSocket.HP_Agent_Connect(self.Agent, __target__[0], __target__[1], ctypes.byref(cLConnID)):
            self.LatestConnID = cLConnID.value
            self.ConnIDPool[self.LatestConnID] = __target__
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
    @HP_TcpPush.EventDescription
    def OnPrepareConnect(self, Sender, ConnID, Socket):
        return HPSocket.EnHandleResult.HR_OK

    @HP_TcpPush.EventDescription
    def OnConnect(self, Sender, ConnID):
        return HPSocket.EnHandleResult.HR_OK

    @HP_TcpPush.EventDescription
    def OnShutdown(self, Sender):
        return HPSocket.EnHandleResult.HR_OK
