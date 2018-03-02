# coding: utf-8

import ctypes
import struct

class TPkgHeader(ctypes.Structure):
    _fields_ = [
        ('seq', ctypes.c_uint),
        ('body_len', ctypes.c_int)
    ]
    def sizeof():
        return ctypes.sizeof(TPkgHeader)


class TPkgBody(ctypes.Structure):
    _fields_ = [
        ('name', ctypes.c_char * 30),
        ('age', ctypes.c_short)
    ]
    def sizeof():
        return ctypes.sizeof(TPkgBody)
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

    def Reset(self):
        self.is_header = True
        self.length = ctypes.sizeof(TPkgHeader)

    def sizeof():
        return ctypes.sizeof(TPkgInfo)


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

TPkgHeaderSize = 8
def UnpackTPkgHeader(Buffer):
    return struct.unpack('ii', Buffer)


def GeneratePkgBuffer(seq, name, age, desc):
    buffer = struct.pack('ii30sh%ds'%len(desc), seq, 30+2+len(desc), name.encode('GBK'), age,desc.encode('GBK'))
    return buffer


def GeneratePkg(buffer):
    desc_len = len(buffer) - 30 - 2
    fmt = '30sh%ds' % desc_len
    (name, age, desc) = struct.unpack(fmt, buffer)
    name = name.decode('GBK')
    desc = desc.decode('GBK')
    return (name, age, desc)