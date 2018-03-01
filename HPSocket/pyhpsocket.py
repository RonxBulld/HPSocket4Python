# coding: utf-8
'''高级封装
    将简化和屏蔽大多数的 ctypes 操作
'''
from HPSocket.HPSocketAPI import *
import ctypes
import threading


class ReadWriteLock(object):

    def __init__(self):
        self.__monitor = threading.Lock()
        self.__exclude = threading.Lock()
        self.readers = 0

    def acquire_read(self):
        with self.__monitor:
            self.readers += 1
            if self.readers == 1:
                self.__exclude.acquire()

    def release_read(self):
        with self.__monitor:
            self.readers -= 1
            if self.readers == 0:
                self.__exclude.release()

    def acquire_write(self):
        self.__exclude.acquire()

    def release_write(self):
        self.__exclude.release()


LP_c_byte = ctypes.POINTER(ctypes.c_byte)
def ValToLP_c_byte(Val):
    '''自动识别 Val 的数据类型：
            str             : 先转换(str->bytes->c_char_Array->LP_c_byte)再发送
            bytes           : 先转换(bytes->c_char_Array->LP_c_byte)再发送
            c_char_Array_*  : 先转换(c_char_Array->LP_c_byte)再发送
            LP_c_byte       : 直接发送
        返回一个 Tuple，(buf:LP_c_byte,len:int)
    '''
    BufferLength = None
    if isinstance(Val, str):  # str->bytes
        Val = bytes(Val, 'GBK')
    if isinstance(Val, bytes):  # bytes->c_char_Array
        Val = ctypes.create_string_buffer(Val, len(Val))
    if isinstance(Val, ctypes.Array) and Val._type_ is ctypes.c_char:  # c_char_Array->LP_c_byte
        BufferLength = len(Val)
        Val = ctypes.cast(Val, LP_c_byte)
    if isinstance(Val, LP_c_byte):
        if BufferLength == None:
            BufferLength = list(Val._objects.values())[0]._length_
    else:
        raise TypeError('Only str/bytes/c_char_Array_*/LP_c_byte Support.')
    return (Val, BufferLength)


_HP_Server_Send = HP_Server_Send
del HP_Server_Send
def HP_Server_Send(Server, ConnID, Buffer):
    (Buffer, BufferLength) = ValToLP_c_byte(Buffer)
    return _HP_Server_Send(Server, ConnID, Buffer, BufferLength)


_HP_Agent_Send = HP_Agent_Send
del HP_Agent_Send
def HP_Agent_Send(Agent, ConnID, Buffer):
    (Buffer, BufferLength) = ValToLP_c_byte(Buffer)
    return _HP_Agent_Send(Agent, ConnID, Buffer, BufferLength)


_HP_Client_Send = HP_Client_Send
del HP_Client_Send
def HP_Client_Send(Client, Buffer):
    (Buffer, BufferLength) = ValToLP_c_byte(Buffer)
    return _HP_Client_Send(Client, Buffer, BufferLength)


_HP_Server_SendPart = HP_Server_SendPart
del HP_Server_SendPart
def HP_Server_SendPart(Server, ConnID, Buffer, Offset):
    buffer = ctypes.cast(ctypes.create_string_buffer(Buffer, len(Buffer)), ctypes.POINTER(ctypes.c_byte))
    offset = ctypes.c_int(Offset)
    return _HP_Server_SendPart(Server, ConnID, buffer, len(Buffer), offset)


_HP_Client_SendPackets = HP_Client_SendPackets
del HP_Client_SendPackets
def HP_Client_SendPackets(Client, Bufs):
    bufs = []
    Bufs = list(Bufs)
    for Buf in Bufs:
        buf = WSABUF()
        (Buf,Length) = ValToLP_c_byte(Buf)
        buf.len = ctypes.c_ulong(Length)
        buf.buf = Buf
        bufs.append(buf)
    pWSABUF = ctypes.cast(bufs, LPWSABUF)
    return _HP_Client_SendPackets(Client, pWSABUF, len(bufs))


_HP_Server_SendPackets = HP_Server_SendPackets
del HP_Server_SendPackets
def HP_Server_SendPackets(Server, ConnID, Bufs):
    bufs = WSABUF * len(Bufs)
    Bufs = list(Bufs)
    for Buf in Bufs:
        buf = WSABUF()
        (Buf, Length) = ValToLP_c_byte(Buf)
        buf.len = ctypes.c_ulong(Length)
        buf.buf = Buf
        bufs.append(buf)
    return _HP_Server_SendPackets(Server, ConnID, ctypes.pointer(bufs), len(bufs))


rwlock = ReadWriteLock()
_HP_Server_SetConnectionExtra = HP_Server_SetConnectionExtra
del HP_Server_SetConnectionExtra
CEDict={}
def HP_Server_SetConnectionExtra(Sender, ConnID, Data):
    global CEDict, rwlock
    # b=bytes(Data)
    # pd=ctypes.pointer(ctypes.create_string_buffer(b,len(b)))
    # CEDict[(Sender,ConnID)] = pd
    # return _HP_Server_SetConnectionExtra(Sender, ConnID, pd)
    rwlock.acquire_write()
    CEDict[(Sender, ConnID)] = Data
    rwlock.release_write()
    return True

_HP_Server_GetConnectionExtra = HP_Server_GetConnectionExtra
del HP_Server_GetConnectionExtra
def HP_Server_GetConnectionExtra(Server, ConnID, type):
    # pInfo = nullptr
    # suc = _HP_Server_GetConnectionExtra(Server, ConnID, ctypes.byref(pInfo))  # 这里要求传入 void**
    # Info = ctypes.cast(pInfo, ctypes.POINTER(type))  # 将 void** 转换为 type**
    # return Info.contents if suc == True else None
    global CEDict, rwlock
    ktp = (Server, ConnID)
    vv = None
    rwlock.acquire_read()
    if ktp in CEDict:
        vv = CEDict[ktp]
        rwlock.release_read()
    return vv


_HP_Server_GetRemoteAddress = HP_Server_GetRemoteAddress
del HP_Server_GetRemoteAddress
def HP_Server_GetRemoteAddress(Sender, ConnID):
    iAddressLen = 50
    pszAddress = ctypes.create_string_buffer(b' ' * iAddressLen, iAddressLen)  # 这里要预留空间，GetRemoteAddress的调用方负责管理内存
    iAddressLen = ctypes.c_int(iAddressLen)
    usPort = ctypes.c_ushort(0)
    _HP_Server_GetRemoteAddress(Sender, ConnID, pszAddress, ctypes.byref(iAddressLen), ctypes.byref(usPort))
    return (bytes.decode(pszAddress.value), usPort.value)


_HP_Agent_GetLocalAddress = HP_Agent_GetLocalAddress
del HP_Agent_GetLocalAddress
def HP_Agent_GetLocalAddress(Sender, ConnID):
    szAddress = ctypes.create_string_buffer(b' ' * 50, 50)
    iAddressLen = ctypes.c_int(50)
    usPort = ctypes.c_ushort(50)
    _HP_Agent_GetLocalAddress(Sender, ConnID, szAddress, ctypes.byref(iAddressLen), ctypes.byref(usPort))
    return (ctypes.string_at(szAddress, iAddressLen.value), usPort.value)

# _HP_Server_GetListenAddress = HP_Server_GetListenAddress
# del HP_Server_GetListenAddress
# def HP_Server_GetListenAddress():
#     pass