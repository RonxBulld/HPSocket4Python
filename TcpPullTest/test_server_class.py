# coding: utf-8

import sys
import time
import TcpPull
import ctypes


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
    def __init__(self, header:bool=True, len:int=ctypes.sizeof(TPkgHeader), *args, **kwargs):
        ctypes.Structure.__init__(self, *args, **kwargs)
        self.is_header = header
        self.length = len


class CBuffer():
    Buffer = None
    buffer = None
    def __init__(self, size):
        self.Buffer = ctypes.create_string_buffer(b' ' * size, size)
        self.buffer = ctypes.cast(self.Buffer, ctypes.POINTER(ctypes.c_byte))  # 从 char[] 转换到需要的 byte*

    def Contents(self):
        return self.Buffer

    def Ptr(self):
        return self.buffer

    def Size(self):
        return len(self.Buffer)-1

    def ToOtherPtr(self, contents_type):
        return ctypes.cast(self.Ptr(), ctypes.POINTER(contents_type))

    def __getitem__(self,index):
        return self.Buffer[index]

    def __len__(self):
        return self.Size()


def FindPkgInfo(Sender, ConnID):
    PkgInfo = TcpPull.HP_Server_GetConnectionExtra(Sender, ConnID, TPkgInfo)
    return PkgInfo


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


class Server(TcpPull.HP_TcpPullServer):
    @TcpPull.HP_TcpPullServer.EventDescription
    def OnAccept(self, Sender, ConnID, Client):
        # ::HP_Server_SetConnectionExtra(pSender, dwConnID, new TPkgInfo(true, sizeof(TPkgHeader)))
        self.pkg = TPkgInfo(True, TcpPull.SizeOf(TPkgHeader))
        TcpPull.HP_Server_SetConnectionExtra(Sender, ConnID, TcpPull.MakePointer(self.pkg))
        return TcpPull.EnHandleResult.HR_OK

    @TcpPull.HP_TcpPullServer.EventDescription
    def OnReceive(self, Sender, ConnID, Length):
        print('[--', sys._getframe().f_code.co_name, '--]', end='\t')
        print('Receive data from client:', ConnID)
        # 本 Demo 和其它的 TestEcho-Pull 一样，数据包的组织形式是 Head-Body 交错
        pInfo = FindPkgInfo(Sender, ConnID)
        if pInfo:
            required = pInfo.length
            remain = Length
            while remain >= required:
                remain -= required
                # Buffer = ctypes.create_string_buffer(b' ' * required)
                # buffer = ctypes.cast(Buffer, ctypes.POINTER(ctypes.c_byte))     # 从 char[] 转换到需要的 byte*
                Buf = CBuffer(required)
                result = TcpPull.HP_TcpPullServer_Fetch(Sender, ConnID, Buf.Ptr(), required)  # 这里获取 Body
                if result == TcpPull.EnFetchResult.FR_OK:
                    if pInfo.is_header:
                        pHeader = Buf.ToOtherPtr(TPkgHeader)
                        print('[TRACR] [Server] head -> seq: %d, body_len: %d' % (pHeader.contents.seq, pHeader.contents.body_len))
                        required = pHeader.contents.body_len    # 从 head 切换到 body
                    else:
                        pBody = Buf.ToOtherPtr(TPkgBody)        # pBody = (TPkgBody*)buffer
                        # 下面的转换需要小心，因为如果使用错误的字符集会导致crash
                        name = pBody.contents.name.decode('GBK')               # name = bytes.decode(pBody->name, 'GBK')
                        # 这里由于 python 语言的限制，没有 C 那么灵活所以 desc 部分单独拿出来处理
                        # 下面的转换需要小心，因为如果使用错误的字符集会导致crash
                        desc = Buf[TcpPull.SizeOf(TPkgBody):].decode('GBK')
                        print('[TRACE] body -> name: %s, age: %d, desc: %s' % (name, pBody.contents.age, desc))
                        required = TcpPull.SizeOf(TPkgHeader)    # 从 body 切换到 head
                    pInfo.is_header = not pInfo.is_header
                    pInfo.length = required
                    if not TcpPull.HP_Server_Send(Sender, ConnID, Buf.Ptr()):
                        return TcpPull.EnHandleResult.HR_ERROR

svr = Server()
svr.Start('0.0.0.0',5555)
while True:
    time.sleep(1)