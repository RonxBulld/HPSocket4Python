# coding: utf-8

import HPSocket
import ctypes
import time
import sys


class TPkgHeader(ctypes.Structure):
    _fields_ = [
        ('seq', ctypes.c_uint),
        ('body_len', ctypes.c_int)
    ]

class TPkgBody(ctypes.Structure):
    _fields_ = [
        ('name', ctypes.c_char * 30),
        ('age', ctypes.c_short)
    ]

class TPkgInfo(ctypes.Structure):
    _fields_ = [
        ('is_header', ctypes.c_bool),
        ('length', ctypes.c_int)
    ]
    def __init__(self, header=True, len=ctypes.sizeof(TPkgHeader), *args, **kwargs):
        ctypes.Structure.__init__(self, *args, **kwargs)
        self.is_header = header
        self.length = len


class HP_TcpPullServer():
    Listener = None
    Server = None
    target = ('', 0)
    __target__ = None
    ServerHandler = None
    def __init__(self):
        self.Listener = HPSocket.Create_HP_TcpPullServerListener()
        self.Server = HPSocket.Create_HP_TcpPullServer(self.Listener)
        self.OnPrepareListenHandle = HPSocket.HP_FN_Server_OnPrepareListen(self.__OnPrepareListen__)
        self.OnAcceptHandle = HPSocket.HP_FN_Server_OnAccept(self.__OnAccept__)
        self.OnSendHandle = HPSocket.HP_FN_Server_OnSend(self.__OnSend__)
        self.OnReceiveHandle = HPSocket.HP_FN_Server_OnPullReceive(self.__OnReceive__)
        self.OnCloseHandle = HPSocket.HP_FN_Server_OnClose(self.__OnClose__)
        self.OnShutdownHandle = HPSocket.HP_FN_Server_OnShutdown(self.__OnShutdown__)

        HPSocket.HP_Set_FN_Server_OnPrepareListen(self.Listener, self.OnPrepareListenHandle)
        HPSocket.HP_Set_FN_Server_OnAccept(self.Listener, self.OnAcceptHandle)
        HPSocket.HP_Set_FN_Server_OnSend(self.Listener, self.OnSendHandle)
        HPSocket.HP_Set_FN_Server_OnPullReceive(self.Listener, self.OnReceiveHandle)
        HPSocket.HP_Set_FN_Server_OnClose(self.Listener, self.OnCloseHandle)
        HPSocket.HP_Set_FN_Server_OnShutdown(self.Listener, self.OnShutdownHandle)

    def __OnPrepareListen__(self, Sender, soListen):
        retval = self.OnPrepareListen(Sender, soListen)
        return retval if isinstance(retval, ctypes.c_int) else HPSocket.EnHandleResult.HR_OK

    def __OnAccept__(self, Sender, ConnID, Client):
        retval = self.OnAccept(Sender, ConnID, Client)
        return retval if isinstance(retval, ctypes.c_int) else HPSocket.EnHandleResult.HR_OK

    def __OnSend__(self, Sender, ConnID, pData, Length):
        retval = self.OnSend(Sender, ConnID, pData, Length)
        return retval if isinstance(retval, ctypes.c_int) else HPSocket.EnHandleResult.HR_OK

    def __OnReceive__(self, Sender, ConnID, Length):
        retval = self.OnReceive(Sender, ConnID, Length)
        return retval if isinstance(retval, ctypes.c_int) else HPSocket.EnHandleResult.HR_OK

    def __OnClose__(self, Sender, ConnID, Operation, ErrorCode):
        retval = self.OnClose(Sender, ConnID, Operation, ErrorCode)
        return retval if isinstance(retval, ctypes.c_int) else HPSocket.EnHandleResult.HR_OK

    def __OnShutdown__(self, Sender):
        retval = self.OnShutdown(Sender)
        return retval if isinstance(retval, ctypes.c_int) else HPSocket.EnHandleResult.HR_OK

    def FindPkgInfo(self, Sender, ConnID):
        pInfo = HPSocket.nullptr
        ppInfo = ctypes.pointer(pInfo)
        suc = HPSocket.HP_Server_GetConnectionExtra(Sender, ConnID, ppInfo)
        Info = ctypes.cast(ppInfo, ctypes.POINTER(ctypes.POINTER(TPkgInfo)))
        return Info.contents if suc == True else None


    def Start(self, host, port):
        self.target = (host, port)
        self.__target__ = (ctypes.create_string_buffer(str.encode(host)), ctypes.c_ushort(port))
        self.ServerHandler = HPSocket.HP_Server_Start(self.Server, self.__target__[0], self.__target__[1])

### 用户可以覆盖下面的方法以实现业务应用 ###

    def OnPrepareListen(self, Sender, SocketHandler):
        print(sys._getframe().f_code.co_name)

        iAddressLen = 50
        pszAddress = ctypes.create_string_buffer(b' ' * iAddressLen)
        piAddressLen = ctypes.pointer(ctypes.c_long(iAddressLen))
        pusPort = ctypes.pointer(ctypes.c_ushort(0))
        HPSocket.HP_Server_GetListenAddress(Sender, pszAddress, piAddressLen, pusPort)

        print('listen on: %s:%d'%(bytes.decode(pszAddress.value), pusPort.contents.value))
        return HPSocket.EnHandleResult.HR_OK

    def OnAccept(self, Sender, ConnID, Client):
        print(sys._getframe().f_code.co_name)

        iAddressLen = 50
        pszAddress = ctypes.create_string_buffer(b' ' * iAddressLen)
        piAddressLen = ctypes.pointer(ctypes.c_long(iAddressLen))
        pusPort = ctypes.pointer(ctypes.c_ushort(0))
        HPSocket.HP_Server_GetRemoteAddress(Sender, ConnID, pszAddress, piAddressLen, pusPort)

        print('client join: %s:%d'%(bytes.decode(pszAddress.value), pusPort.contents.value))

        # 这里一定要成员化，不然内存被回收
        self.pTPkgInfoInst = ctypes.pointer(TPkgInfo(header=True, len=ctypes.sizeof(TPkgHeader)))
        HPSocket.HP_Server_SetConnectionExtra(Sender, ConnID, self.pTPkgInfoInst)
        return HPSocket.EnHandleResult.HR_OK

    def OnSend(self, Sender, ConnID, pData, Length):
        print(sys._getframe().f_code.co_name)
        print('[Send->%d] size: %d' % (ConnID, Length))
        return HPSocket.EnHandleResult.HR_OK

    def OnReceive(self, Sender, ConnID, Length):
        print(sys._getframe().f_code.co_name)
        pInfo = self.FindPkgInfo(Sender, ConnID)
        if pInfo:
            required = pInfo.contents.length
            remain = Length
            while remain >= required:
                remain -= required
                buf = b' ' * required
                Buffer = ctypes.create_string_buffer(buf, required)
                buffer = ctypes.cast(Buffer, ctypes.POINTER(ctypes.c_byte))
                result = HPSocket.HP_TcpPullServer_Fetch(Sender, ConnID, buffer, required)
                if result == HPSocket.EnFetchResult.FR_OK:
                    if pInfo.contents.is_header:
                        pHeader = ctypes.cast(Buffer,ctypes.POINTER(TPkgHeader))
                        print('[TRACR] [Server] head -> seq: %d, body_len: %d' % (pHeader.contents.seq, pHeader.contents.body_len));
                        required = pHeader.contents.body_len
                    else:
                        # 需要计算真实的 desc 长度
                        tldesc = ctypes.sizeof(Buffer) - ctypes.sizeof(TPkgBody) - 1
                        pBody = ctypes.cast(Buffer, ctypes.POINTER(TPkgBody))
                        name = pBody.contents.name.decode('GBK')
                        desc = Buffer[ctypes.sizeof(TPkgBody):].decode('GBK')
                        print('[TRACE] body -> name: %s, age: %d, desc: %s' % (name, pBody.contents.age, desc))
                        required = ctypes.sizeof(TPkgHeader)
                    pInfo.contents.is_header = not pInfo.contents.is_header
                    pInfo.contents.length = required
                    if not HPSocket.HP_Server_Send(Sender, ConnID, buffer, len(Buffer)):
                        return HPSocket.EnHandleResult.HR_ERROR

        print(Sender, ConnID, Length)
        return HPSocket.EnHandleResult.HR_OK

    def OnClose(self, Sender, ConnID, Operation, ErrorCode):
        print(sys._getframe().f_code.co_name)
        print('[Client %d closed]Operation=%d, Error=%d' % (ConnID, Operation, ErrorCode))
        return HPSocket.EnHandleResult.HR_OK

    def OnShutdown(self, Sender):
        print(sys._getframe().f_code.co_name)
        print('[Server shutdown now]')
        return HPSocket.EnHandleResult.HR_OK

test=HP_TcpPullServer()
test.Start('0.0.0.0',5555)
while True:
    time.sleep(1)