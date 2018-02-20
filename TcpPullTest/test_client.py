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


class HP_TcpPullClient():
    Listener = None
    Client = None
    target = ('', 0)
    __target__ = None
    ClientHandler = None
    pkgInfo = TPkgInfo()
    SEQ = 0
    def __init__(self):
        self.Listener = HPSocket.Create_HP_TcpPullClientListener()
        self.Client = HPSocket.Create_HP_TcpPullClient(self.Listener)

        self.OnConnectHandle = HPSocket.HP_FN_Client_OnConnect(self.OnConnect)
        self.OnSendHandle = HPSocket.HP_FN_Client_OnSend(self.OnSend)
        self.OnReceiveHandle = HPSocket.HP_FN_Client_OnPullReceive(self.OnReceive)
        self.OnCloseHandle = HPSocket.HP_FN_Client_OnClose(self.OnClose)

        HPSocket.HP_Set_FN_Client_OnConnect(self.Listener, self.OnConnectHandle)
        HPSocket.HP_Set_FN_Client_OnSend(self.Listener, self.OnSendHandle)
        HPSocket.HP_Set_FN_Client_OnPullReceive(self.Listener, self.OnReceiveHandle)
        HPSocket.HP_Set_FN_Client_OnClose(self.Listener, self.OnCloseHandle)

    def EventDescription(fn):
        def arguments(*args, **kwargs):
            retval = fn(*args, **kwargs)
            return retval if isinstance(retval, ctypes.c_int) else HPSocket.EnHandleResult.HR_OK
        return arguments

    def FindPkgInfo(self, Sender, ConnID):
        pInfo = HPSocket.nullptr
        ppInfo = ctypes.pointer(pInfo)
        suc = HPSocket.HP_Client_GetConnectionExtra(Sender, ConnID, ppInfo)     # 这里要求传入 void**
        Info = ctypes.cast(ppInfo, ctypes.POINTER(ctypes.POINTER(TPkgInfo)))    # 将 void** 转换为 TPkgInfo**
        return Info.contents if suc == True else None

    def GeneratePkgBuffer(self, seq, name, age, desc):
        desc_len = len(desc) + 1
        body_len = ctypes.sizeof(TPkgBody)
        head_len = ctypes.sizeof(TPkgHeader)
        buffer = ctypes.create_string_buffer(b'\0', head_len + body_len + desc_len)
        # 你有张良计，我有过墙梯
        pHeader = ctypes.cast(ctypes.byref(buffer, 0), ctypes.POINTER(TPkgHeader))
        pHeader.contents.seq = seq
        pHeader.contents.body_len = body_len + desc_len

        pBody = ctypes.cast(ctypes.byref(buffer, head_len), ctypes.POINTER(TPkgBody))
        pBody.contents.name = str.encode(name,encoding='GBK')
        pBody.contents.age = age

        bsDesc = str.encode(desc,encoding='GBK')
        bArr = bytearray(buffer.raw)
        bArr[head_len + body_len:head_len + body_len + desc_len] = bsDesc
        buffer = ctypes.create_string_buffer(bytes(bArr))

        return buffer

    def Start(self, host, port):
        self.target = (host, port)
        self.__target__ = (ctypes.create_string_buffer(str.encode(host,encoding='GBK')), ctypes.c_ushort(port))
        AsyncConn = ctypes.c_bool(False)
        if HPSocket.HP_Client_Start(self.Client, self.__target__[0], self.__target__[1], AsyncConn):
            print('Start connect success.')
        else:
            print('Cannot start connect.')

### 用户可以覆盖下面的方法以实现业务应用 ###
    def Send(self):
        self.SEQ += 1
        buffer = self.GeneratePkgBuffer(self.SEQ, '伤神恶趣味', 23, 'text to be sent')
        HPSocket.HP_Client_Send(self.Client, ctypes.cast(buffer, ctypes.POINTER(ctypes.c_byte)), ctypes.c_int(len(buffer)))

    @EventDescription
    def OnConnect(self, Sender, ConnID):
        print('[--', sys._getframe().f_code.co_name, '--]', end='\t')

        iAddressLen  = 50
        pszAddress   = ctypes.create_string_buffer(b' ' * iAddressLen)  # 这里要预留空间，GetRemoteAddress的调用方负责管理内存
        iAddressLen  = ctypes.c_long(iAddressLen)
        usPort       = ctypes.c_ushort(0)
        HPSocket.HP_Client_GetLocalAddress(Sender, pszAddress, ctypes.byref(iAddressLen), ctypes.byref(usPort))

        print('client address: %s:%d as %d'%(bytes.decode(pszAddress.value), usPort.value, ConnID))

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
        required = self.pkgInfo.length
        remain = Length
        while remain >= required:
            remain -= required
            Buffer = ctypes.create_string_buffer(b' ' * required)
            buffer = ctypes.cast(Buffer, ctypes.POINTER(ctypes.c_byte))     # 从 char[] 转换到需要的 byte*
            result = HPSocket.HP_TcpPullClient_Fetch(Sender, buffer, required)  # 这里获取 Body
            if result == HPSocket.EnFetchResult.FR_OK:
                if self.pkgInfo.is_header:
                    pHeader = ctypes.cast(Buffer,ctypes.POINTER(TPkgHeader))
                    print('[TRACR] [Client] head -> seq: %d, body_len: %d' % (pHeader.contents.seq, pHeader.contents.body_len));
                    required = pHeader.contents.body_len    # 从 head 切换到 body
                else:
                    pBody = ctypes.cast(buffer, ctypes.POINTER(TPkgBody))   # pBody = (TPkgBody*)buffer
                    name = pBody.contents.name.decode('GBK')               # name = bytes.decode(pBody->name, 'GBK')
                    # 这里由于 python 语言的限制，没有 C 那么灵活所以 desc 部分单独拿出来处理
                    desc = Buffer[ctypes.sizeof(TPkgBody):].decode('GBK')  # desc = bytes.decode(Buffer[sizeof(TPkgBody):], 'GBK')
                    print('[TRACE] [Client] body -> name: %s, age: %d, desc: %s' % (name, pBody.contents.age, desc))
                    required = ctypes.sizeof(TPkgHeader)    # 从 body 切换到 head
                self.pkgInfo.is_header = not self.pkgInfo.is_header
                self.pkgInfo.length = required

        return HPSocket.EnHandleResult.HR_OK

    @EventDescription
    def OnClose(self, Sender, ConnID, Operation, ErrorCode):
        print('[--', sys._getframe().f_code.co_name, '--]', end='\t')
        # Operation 的值参考枚举类 EnSocketOperation 的定义
        print('[Client %d closed]Operation=%d, Error=%d' % (ConnID, Operation, ErrorCode))
        return HPSocket.EnHandleResult.HR_OK

test = HP_TcpPullClient()
test.Start('127.0.0.1',5555)
while True:
    test.Send()
    time.sleep(0.05)
    # input("Press")