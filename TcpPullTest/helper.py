# coding: utf-8

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
    def __init__(self, init_info):
        '''利用参数类型判断实现重载'''
        if isinstance(init_info, int):
            size = init_info
            self.Buffer = ctypes.create_string_buffer(b' ' * size, size)
            self.buffer = ctypes.cast(self.Buffer, ctypes.POINTER(ctypes.c_byte))  # 从 char[] 转换到需要的 byte*
        elif isinstance(init_info, bytes):
            data = init_info
            self.Buffer = ctypes.create_string_buffer(data, len(data))
            self.buffer = ctypes.cast(self.Buffer, ctypes.POINTER(ctypes.c_byte))
        else:
            raise TypeError('不支持的初始化参数类型')

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