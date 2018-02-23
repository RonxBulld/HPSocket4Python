# coding: utf-8
'''高级封装
    将简化和屏蔽大多数的 ctypes 操作
'''

from HPSocket import *

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


_HP_Client_Send = HP_Client_Send
del HP_Client_Send
def HP_Client_Send(Client, Buffer):
    (Buffer, BufferLength) = ValToLP_c_byte(Buffer)
    return _HP_Client_Send(Client, Buffer, BufferLength)


_HP_Server_SendPart = HP_Server_SendPart
del HP_Server_SendPart
def HP_Server_SendPart(Server, ConnID, Buffer, Offset):
    buffer = ctypes.cast(ctypes.create_string_buffer(Buffer, len(Buffer) + 1), ctypes.POINTER(ctypes.c_byte))
    offset = ctypes.c_int(Offset)
    _HP_Server_SendPart(Server, ConnID, buffer, len(Buffer), offset)


_HP_Client_SendPackets = HP_Client_SendPackets
del HP_Client_SendPackets
def HP_Client_SendPackets(Client, Bufs):
    bufs = []
    Bufs = list(Bufs)
    for Buf in Bufs:
        buf = WSABUF()
        buf.len = ctypes.c_ulong(len(Buf))
        pbuf = ctypes.cast(ctypes.create_string_buffer(str.encode(Buf+'\0',encoding='GBK')), ctypes.c_char_p)
        buf.buf = pbuf
        bufs.append(Buf)
    pWSABUF = ctypes.cast(bufs, LPWSABUF)
    _HP_Client_SendPackets(Client, pWSABUF, len(bufs))


_HP_Server_SendPackets = HP_Server_SendPackets
del HP_Server_SendPackets
def HP_Server_SendPackets(Server, ConnID, Bufs):
    bufs = []
    Bufs = list(Bufs)
    for Buf in Bufs:
        buf = WSABUF()
        buf.len = ctypes.c_ulong(len(Buf))
        buf.buf = ctypes.cast(ctypes.create_string_buffer(Buf+'\0',len(Buf) + 1), ctypes.POINTER(ctypes.c_byte))
        bufs.append(Buf)
    _HP_Server_SendPackets(Server, ConnID, ctypes.pointer(bufs), len(bufs))


_HP_Server_GetConnectionExtra = HP_Server_GetConnectionExtra
del HP_Server_GetConnectionExtra
def HP_Server_GetConnectionExtra(Server, ConnID, type):
    pInfo = nullptr
    suc = _HP_Server_GetConnectionExtra(Server, ConnID, ctypes.byref(pInfo))  # 这里要求传入 void**
    Info = ctypes.cast(pInfo, ctypes.POINTER(type))  # 将 void** 转换为 type**
    return Info.contents if suc == True else None


_HP_Server_GetRemoteAddress = HP_Server_GetRemoteAddress
del HP_Server_GetRemoteAddress
def HP_Server_GetRemoteAddress(Sender, ConnID):
    iAddressLen = 50
    pszAddress = ctypes.create_string_buffer(b' ' * iAddressLen)  # 这里要预留空间，GetRemoteAddress的调用方负责管理内存
    iAddressLen = ctypes.c_int(iAddressLen)
    usPort = ctypes.c_ushort(0)
    _HP_Server_GetRemoteAddress(Sender, ConnID, pszAddress, ctypes.byref(iAddressLen), ctypes.byref(usPort))
    return (bytes.decode(pszAddress.value), usPort.value)


_HP_Server_GetListenAddress = HP_Server_GetListenAddress
del HP_Server_GetListenAddress
def HP_Server_GetListenAddress():
    pass