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
    # 这里定义的结构和 C 语言的 DEMO 不一样，原因请看 OnReceive

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
    def __init__(self):
        self.Listener = HPSocket.Create_HP_TcpPullServerListener()
        self.Server = HPSocket.Create_HP_TcpPullServer(self.Listener)
        self.OnPrepareListenHandle = HPSocket.HP_FN_Server_OnPrepareListen(self.OnPrepareListen)
        self.OnAcceptHandle = HPSocket.HP_FN_Server_OnAccept(self.OnAccept)
        self.OnSendHandle = HPSocket.HP_FN_Server_OnSend(self.OnSend)
        self.OnReceiveHandle = HPSocket.HP_FN_Server_OnPullReceive(self.OnReceive)
        self.OnCloseHandle = HPSocket.HP_FN_Server_OnClose(self.OnClose)
        self.OnShutdownHandle = HPSocket.HP_FN_Server_OnShutdown(self.OnShutdown)

        HPSocket.HP_Set_FN_Server_OnPrepareListen(self.Listener, self.OnPrepareListenHandle)
        HPSocket.HP_Set_FN_Server_OnAccept(self.Listener, self.OnAcceptHandle)
        HPSocket.HP_Set_FN_Server_OnSend(self.Listener, self.OnSendHandle)
        HPSocket.HP_Set_FN_Server_OnPullReceive(self.Listener, self.OnReceiveHandle)
        HPSocket.HP_Set_FN_Server_OnClose(self.Listener, self.OnCloseHandle)
        HPSocket.HP_Set_FN_Server_OnShutdown(self.Listener, self.OnShutdownHandle)

    def EventDescription(fn):
        def arguments(*args, **kwargs):
            retval = fn(*args, **kwargs)
            return retval if isinstance(retval, ctypes.c_int) else HPSocket.EnHandleResult.HR_OK
        return arguments

    def FindPkgInfo(self, Sender, ConnID):
        pInfo = HPSocket.nullptr
        ppInfo = ctypes.pointer(pInfo)
        suc = HPSocket.HP_Server_GetConnectionExtra(Sender, ConnID, ppInfo)     # 这里要求传入 void**
        Info = ctypes.cast(ppInfo, ctypes.POINTER(ctypes.POINTER(TPkgInfo)))    # 将 void** 转换为 TPkgInfo**
        return Info.contents if suc == True else None


    def Start(self, host, port):
        self.target = (host, port)
        self.__target__ = (ctypes.create_string_buffer(str.encode(host)), ctypes.c_ushort(port))
        if HPSocket.HP_Server_Start(self.Server, self.__target__[0], self.__target__[1]):
            print('Start server success.')
        else:
            print('Cannot start server.')

### 用户可以覆盖下面的方法以实现业务应用 ###
    @EventDescription
    def OnPrepareListen(self, Sender, SocketHandler):
        print('[--', sys._getframe().f_code.co_name, '--]', end='\t')

        iAddressLen = 50
        pszAddress  = ctypes.create_string_buffer(b' ' * iAddressLen)
        iAddressLen = ctypes.c_int(iAddressLen)
        usPort      = ctypes.c_ushort(0)
        HPSocket.HP_Server_GetListenAddress(Sender, pszAddress, ctypes.byref(iAddressLen), ctypes.byref(usPort))

        print('listen on: %s:%d'%(bytes.decode(pszAddress.value), usPort.value))
        return HPSocket.EnHandleResult.HR_OK

    @EventDescription
    def OnAccept(self, Sender, ConnID, Client):
        print('[--', sys._getframe().f_code.co_name, '--]', end='\t')

        iAddressLen  = 50
        pszAddress   = ctypes.create_string_buffer(b' ' * iAddressLen)  # 这里要预留空间，GetRemoteAddress的调用方负责管理内存
        iAddressLen  = ctypes.c_int(iAddressLen)
        usPort       = ctypes.c_ushort(0)
        HPSocket.HP_Server_GetRemoteAddress(Sender, ConnID, pszAddress, ctypes.byref(iAddressLen), ctypes.byref(usPort))

        print('client join: %s:%d as %d'%(bytes.decode(pszAddress.value), usPort.value, ConnID))

        # 这里一定要成员化，不然内存被回收
        self.pTPkgInfoInst = ctypes.pointer(TPkgInfo(header=True, len=ctypes.sizeof(TPkgHeader)))
        HPSocket.HP_Server_SetConnectionExtra(Sender, ConnID, self.pTPkgInfoInst)
        return HPSocket.EnHandleResult.HR_OK


    @EventDescription
    def OnSend(self, Sender, ConnID, pData, Length):
        print('[--', sys._getframe().f_code.co_name, '--]', end='\t')
        # 如果你在这里想获取发送的数据，可以对 pData 用索引的方式，就像操作字节数组一样去使用
        # 但是，pData 自身并不包含长度信息，所以不可以使用 [:] 的形式
        print('[Send->%d] size: %d' % (ConnID, Length))
        print(pData[0:Length])
        return HPSocket.EnHandleResult.HR_OK

    @EventDescription
    def OnReceive(self, Sender, ConnID, Length):
        print('[--', sys._getframe().f_code.co_name, '--]', end='\t')
        print('Receive data from client:', ConnID)
        # 本 Demo 和其它的 TestEcho-Pull 一样，数据包的组织形式是 Head-Body 交错
        pInfo = self.FindPkgInfo(Sender, ConnID)
        if pInfo:
            required = pInfo.contents.length
            remain = Length
            while remain >= required:
                remain -= required
                Buffer = ctypes.create_string_buffer(b' ' * required)
                buffer = ctypes.cast(Buffer, ctypes.POINTER(ctypes.c_byte))     # 从 char[] 转换到需要的 byte*
                result = HPSocket.HP_TcpPullServer_Fetch(Sender, ConnID, buffer, required)  # 这里获取 Body
                if result == HPSocket.EnFetchResult.FR_OK:
                    if pInfo.contents.is_header:
                        pHeader = ctypes.cast(Buffer,ctypes.POINTER(TPkgHeader))
                        print('[TRACR] [Server] head -> seq: %d, body_len: %d' % (pHeader.contents.seq, pHeader.contents.body_len));
                        required = pHeader.contents.body_len    # 从 head 切换到 body
                    else:
                        pBody = ctypes.cast(buffer, ctypes.POINTER(TPkgBody))   # pBody = (TPkgBody*)buffer
                        # 下面的转换需要小心，因为如果使用错误的字符集会导致crash
                        name = pBody.contents.name.decode('GBK')               # name = bytes.decode(pBody->name, 'GBK')
                        # 这里由于 python 语言的限制，没有 C 那么灵活所以 desc 部分单独拿出来处理
                        # 下面的转换需要小心，因为如果使用错误的字符集会导致crash
                        desc = Buffer[ctypes.sizeof(TPkgBody):].decode('GBK')  # desc = bytes.decode(Buffer[sizeof(TPkgBody):], 'GBK')
                        print('[TRACE] body -> name: %s, age: %d, desc: %s' % (name, pBody.contents.age, desc))
                        required = ctypes.sizeof(TPkgHeader)    # 从 body 切换到 head
                    pInfo.contents.is_header = not pInfo.contents.is_header
                    pInfo.contents.length = required
                    if not HPSocket.HP_Server_Send(Sender, ConnID, buffer, len(Buffer) - 1):    # 这里记得 -1
                        return HPSocket.EnHandleResult.HR_ERROR

        return HPSocket.EnHandleResult.HR_OK

    @EventDescription
    def OnClose(self, Sender, ConnID, Operation, ErrorCode):
        print('[--', sys._getframe().f_code.co_name, '--]', end='\t')
        # Operation 的值参考枚举类 EnSocketOperation 的定义
        print('[Client %d closed]Operation=%d, Error=%d' % (ConnID, Operation, ErrorCode))
        return HPSocket.EnHandleResult.HR_OK

    @EventDescription
    def OnShutdown(self, Sender):
        print('[--', sys._getframe().f_code.co_name, '--]', end='\t')
        print('[Server shutdown now]')
        return HPSocket.EnHandleResult.HR_OK

test = HP_TcpPullServer()
test.Start('0.0.0.0',5555)
while True:
    time.sleep(1)