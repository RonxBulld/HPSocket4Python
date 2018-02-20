# conding: utf-8
'''HP_TcpPull 类'''
import sys
sys.path.append('../')
from pyhpsocket import *


class HP_TcpPullServer():
    Listener = None
    Server = None
    target = ('', 0)
    __target__ = None
    def __init__(self):
        self.Listener = Create_HP_TcpPullServerListener()
        self.Server = Create_HP_TcpPullServer(self.Listener)
        self.OnPrepareListenHandle = HP_FN_Server_OnPrepareListen(self.OnPrepareListen)
        self.OnAcceptHandle = HP_FN_Server_OnAccept(self.OnAccept)
        self.OnSendHandle = HP_FN_Server_OnSend(self.OnSend)
        self.OnReceiveHandle = HP_FN_Server_OnPullReceive(self.OnReceive)
        self.OnCloseHandle = HP_FN_Server_OnClose(self.OnClose)
        self.OnShutdownHandle = HP_FN_Server_OnShutdown(self.OnShutdown)

        HP_Set_FN_Server_OnPrepareListen(self.Listener, self.OnPrepareListenHandle)
        HP_Set_FN_Server_OnAccept(self.Listener, self.OnAcceptHandle)
        HP_Set_FN_Server_OnSend(self.Listener, self.OnSendHandle)
        HP_Set_FN_Server_OnPullReceive(self.Listener, self.OnReceiveHandle)
        HP_Set_FN_Server_OnClose(self.Listener, self.OnCloseHandle)
        HP_Set_FN_Server_OnShutdown(self.Listener, self.OnShutdownHandle)

    def EventDescription(fn):
        def arguments(*args, **kwargs):
            retval = fn(*args, **kwargs)
            return retval if isinstance(retval, ctypes.c_int) else EnHandleResult.HR_OK
        return arguments

    def Start(self, host, port):
        self.target = (host, port)
        self.__target__ = (ctypes.create_string_buffer(str.encode(host)), ctypes.c_ushort(port))
        if HP_Server_Start(self.Server, self.__target__[0], self.__target__[1]):
            print('Start server success.')
        else:
            print('Cannot start server.')

### 用户可以覆盖下面的方法以实现业务应用 ###
    @EventDescription
    def OnPrepareListen(self, Sender, SocketHandler):
        return EnHandleResult.HR_OK

    @EventDescription
    def OnAccept(self, Sender, ConnID, Client):
        return EnHandleResult.HR_OK

    @EventDescription
    def OnSend(self, Sender, ConnID, pData, Length):
        return EnHandleResult.HR_OK

    @EventDescription
    def OnReceive(self, Sender, ConnID, Length):
        return EnHandleResult.HR_OK

    @EventDescription
    def OnClose(self, Sender, ConnID, Operation, ErrorCode):
        return EnHandleResult.HR_OK

    @EventDescription
    def OnShutdown(self, Sender):
        return EnHandleResult.HR_OK


class HP_TcpPullClient():
    Listener = None
    Client = None
    target = ('', 0)
    __target__ = None
    def __init__(self):
        self.Listener = Create_HP_TcpPullClientListener()
        self.Client = Create_HP_TcpPullClient(self.Listener)

        self.OnConnectHandle = HP_FN_Client_OnConnect(self.OnConnect)
        self.OnSendHandle = HP_FN_Client_OnSend(self.OnSend)
        self.OnReceiveHandle = HP_FN_Client_OnPullReceive(self.OnReceive)
        self.OnCloseHandle = HP_FN_Client_OnClose(self.OnClose)

        HP_Set_FN_Client_OnConnect(self.Listener, self.OnConnectHandle)
        HP_Set_FN_Client_OnSend(self.Listener, self.OnSendHandle)
        HP_Set_FN_Client_OnPullReceive(self.Listener, self.OnReceiveHandle)
        HP_Set_FN_Client_OnClose(self.Listener, self.OnCloseHandle)

    def EventDescription(fn):
        def arguments(*args, **kwargs):
            retval = fn(*args, **kwargs)
            return retval if isinstance(retval, ctypes.c_int) else EnHandleResult.HR_OK
        return arguments

    def Start(self, host, port):
        self.target = (host, port)
        self.__target__ = (ctypes.create_string_buffer(str.encode(host,encoding='GBK')), ctypes.c_ushort(port))
        AsyncConn = ctypes.c_bool(False)
        if HP_Client_Start(self.Client, self.__target__[0], self.__target__[1], AsyncConn):
            print('Start connect success.')
        else:
            print('Cannot start connect.')

### 用户可以覆盖下面的方法以实现业务应用 ###
    def Send(self):
        self.SEQ += 1
        buffer = self.GeneratePkgBuffer(self.SEQ, '伤神恶趣味', 23, 'text to be sent')
        HP_Client_Send(self.Client, ctypes.cast(buffer, ctypes.POINTER(ctypes.c_byte)), ctypes.c_int(len(buffer)))

    @EventDescription
    def OnConnect(self, Sender, ConnID):
        return EnHandleResult.HR_OK

    @EventDescription
    def OnSend(self, Sender, ConnID, pData, Length):
        return EnHandleResult.HR_OK

    @EventDescription
    def OnReceive(self, Sender, ConnID, Length):
        return EnHandleResult.HR_OK

    @EventDescription
    def OnClose(self, Sender, ConnID, Operation, ErrorCode):
        return EnHandleResult.HR_OK