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

LP_c_wchar = ctypes.POINTER(ctypes.c_wchar)
def WValToLP_c_wchar(WVal, Coding='UTF-8'):
    '''自动识别 WVal 的数据类型：
            bytes           : 先转换(bytes->str->c_wchar_Array->LP_c_wchar)再返回
            str             : 先转换(str->c_wchar_Array->LP_c_wchar)再返回
            c_wchar_Array_* : 先转换(c_wchar_Array->LP_c_wchar)再返回
            LP_c_wchar      : 直接返回
        返回一个 Tuple，(buf:LP_c_wchar,len:int)
    '''
    BufferLength = None
    if isinstance(WVal, bytes):  # bytes->str
        WVal = WVal.decode(encoding='utf-8')
    if isinstance(WVal, str):  # str->c_wchar_Array
        WVal = ctypes.create_unicode_buffer(WVal, len(WVal))
    if isinstance(WVal, ctypes.Array) and WVal._type_ is ctypes.c_wchar:  # c_wchar_Array->LP_c_wchar
        BufferLength = len(WVal)
        WVal = ctypes.cast(WVal, LP_c_wchar)
    if isinstance(WVal, LP_c_wchar):
        if BufferLength == None:
            BufferLength = list(WVal._objects.values())[0]._length_
    else:
        raise TypeError('Only str/bytes/c_char_Array_*/LP_c_byte Support.')
    return (WVal, BufferLength)

LP_c_byte = ctypes.POINTER(ctypes.c_byte)
def ValToLP_c_byte(Val, Coding='GBK'):
    '''自动识别 Val 的数据类型：
            str             : 先转换(str->bytes->c_char_Array->LP_c_byte)再返回
            bytes           : 先转换(bytes->c_char_Array->LP_c_byte)再返回
            c_char_Array_*  : 先转换(c_char_Array->LP_c_byte)再返回
            LP_c_byte       : 直接返回
        返回一个 Tuple，(buf:LP_c_byte,len:int)
    '''
    BufferLength = None
    if isinstance(Val, str):  # str->bytes
        Val = bytes(Val, Coding)
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

_HP_Agent_SendPart = HP_Agent_SendPart
del HP_Agent_SendPart
def HP_Agent_SendPart(Agent, ConnID, Buffer, Offset):
    buffer = ctypes.cast(ctypes.create_string_buffer(Buffer, len(Buffer)), ctypes.POINTER(ctypes.c_byte))
    offset = ctypes.c_int(Offset)
    return _HP_Agent_SendPart(Agent, ConnID, buffer, len(Buffer), offset)

_HP_Client_SendPart = HP_Client_SendPart
del HP_Client_SendPart
def HP_Client_SendPart(Client, Buffer, Offset):
    buffer = ctypes.cast(ctypes.create_string_buffer(Buffer, len(Buffer)), ctypes.POINTER(ctypes.c_byte))
    offset = ctypes.c_int(Offset)
    return _HP_Client_SendPart(Client, buffer, len(Buffer), offset)

def BufsToWSABUFs(Bufs : list):
    if not isinstance(Bufs, list):
        raise TypeError('Argument "Bufs" must be list type.')
    BufsNum = len(Bufs)
    bufs = (WSABUF * BufsNum)()
    for i in range(BufsNum):
        (Buf, Length) = ValToLP_c_byte(Bufs[i])
        bufs[i].len = ctypes.c_ulong(Length)
        bufs[i].buf = Buf
    return bufs

_HP_Client_SendPackets = HP_Client_SendPackets
del HP_Client_SendPackets
def HP_Client_SendPackets(Client, Bufs : list):
    bufs = BufsToWSABUFs(Bufs)
    BufsNum = len(bufs)
    pWSABUF = ctypes.cast(bufs, LPWSABUF)
    return _HP_Client_SendPackets(Client, pWSABUF, BufsNum)

_HP_Server_SendPackets = HP_Server_SendPackets
del HP_Server_SendPackets
def HP_Server_SendPackets(Server, ConnID, Bufs):
    bufs = BufsToWSABUFs(Bufs)
    BufsNum = len(bufs)
    pWSABUF = ctypes.cast(bufs, LPWSABUF)
    return _HP_Server_SendPackets(Server, ConnID, pWSABUF, BufsNum)

_HP_Agent_SendPackets = HP_Agent_SendPackets
del HP_Agent_SendPackets
def HP_Agent_SendPackets(Agent, ConnID, Bufs):
    bufs = BufsToWSABUFs(Bufs)
    BufsNum = len(bufs)
    pWSABUF = ctypes.cast(bufs, LPWSABUF)
    return _HP_Agent_SendPackets(Agent, ConnID, pWSABUF, BufsNum)

class ConnectionExtra:
    _rwlock = ReadWriteLock()
    CEDict={}
    def Set(self, S, C, Data):
        self._rwlock.acquire_write()
        self.CEDict[(S, C)] = Data
        self._rwlock.release_write()
        return True

    def Get(self, S, C):
        ktp = (S, C)
        vv = None
        self._rwlock.acquire_read()
        if ktp in self.CEDict:
            vv = self.CEDict[ktp]
            self._rwlock.release_read()
        return vv

ServerConnectionExtra = ConnectionExtra()

_HP_Server_SetConnectionExtra = HP_Server_SetConnectionExtra
del HP_Server_SetConnectionExtra
def HP_Server_SetConnectionExtra(Sender, ConnID, Data):
    global ServerConnectionExtra
    return ServerConnectionExtra.Set(S=Sender, C=ConnID, Data=Data)

_HP_Server_GetConnectionExtra = HP_Server_GetConnectionExtra
del HP_Server_GetConnectionExtra
def HP_Server_GetConnectionExtra(Server, ConnID, type):
    global ServerConnectionExtra
    return ServerConnectionExtra.Get(S=Server, C=ConnID)

AgentConnectionExtra = ConnectionExtra()

_HP_Agent_SetConnectionExtra = HP_Agent_SetConnectionExtra
del HP_Agent_SetConnectionExtra
def HP_Agent_SetConnectionExtra(Sender, ConnID, Data):
    global AgentConnectionExtra
    return AgentConnectionExtra.Set(S=Sender, C=ConnID, Data=Data)

_HP_Agent_GetConnectionExtra = HP_Agent_GetConnectionExtra
del HP_Agent_GetConnectionExtra
def HP_Agent_GetConnectionExtra(Agent, ConnID, type):
    global AgentConnectionExtra
    return AgentConnectionExtra.Get(S=Agent, C=ConnID)

ClientConnectionExtra = ConnectionExtra()

_HP_Client_SetExtra = HP_Client_SetExtra
del HP_Client_SetExtra
def HP_Client_SetExtra(Sender, Data):
    global ClientConnectionExtra
    return ClientConnectionExtra.Set(S=Sender, C=None, Data=Data)

_HP_Client_GetConnectionExtra = HP_Client_GetExtra
del HP_Client_GetExtra
def HP_Client_GetExtra(Client, type):
    global ClientConnectionExtra
    return ClientConnectionExtra.Get(S=Client, C=None)

def GetAddressTemplate(Sender, ConnID, Callback):
    iAddressLen = 50
    pszAddress = ctypes.create_string_buffer(b' ' * iAddressLen, iAddressLen)  # 这里要预留空间，GetRemoteAddress的调用方负责管理内存
    iAddressLen = ctypes.c_int(iAddressLen)
    usPort = ctypes.c_ushort(0)
    if (ConnID is not None and Callback(Sender, ConnID, pszAddress, ctypes.byref(iAddressLen), ctypes.byref(usPort))) or (ConnID is None and Callback(Sender, pszAddress, ctypes.byref(iAddressLen), ctypes.byref(usPort))):
        return (ctypes.string_at(pszAddress, iAddressLen.value).decode('GBK'), usPort.value)
    else:
        return None

_HP_Server_GetRemoteAddress = HP_Server_GetRemoteAddress
del HP_Server_GetRemoteAddress
def HP_Server_GetRemoteAddress(Sender, ConnID):
    return GetAddressTemplate(Sender, ConnID, _HP_Server_GetRemoteAddress)

_HP_Agent_GetRemoteAddress = HP_Agent_GetRemoteAddress
del HP_Agent_GetRemoteAddress
def HP_Agent_GetRemoteAddress(Sender, ConnID):
    return GetAddressTemplate(Sender, ConnID, _HP_Agent_GetRemoteAddress)

_HP_Server_GetLocalAddress = HP_Server_GetLocalAddress
del HP_Server_GetLocalAddress
def HP_Server_GetLocalAddress(Sender, ConnID):
    return GetAddressTemplate(Sender, ConnID, _HP_Server_GetLocalAddress)

_HP_Agent_GetLocalAddress = HP_Agent_GetLocalAddress
del HP_Agent_GetLocalAddress
def HP_Agent_GetLocalAddress(Sender, ConnID):
    return GetAddressTemplate(Sender, ConnID, _HP_Agent_GetLocalAddress)

_HP_Agent_GetRemoteHost = HP_Agent_GetRemoteHost
del HP_Agent_GetRemoteHost
def HP_Agent_GetRemoteHost(Sender, ConnID):
    return GetAddressTemplate(Sender, ConnID, _HP_Agent_GetRemoteHost)

_HP_Server_GetListenAddress = HP_Server_GetListenAddress
del HP_Server_GetListenAddress
def HP_Server_GetListenAddress(Server):
    return GetAddressTemplate(Server, None, _HP_Server_GetListenAddress)

_HP_UdpCast_GetRemoteAddress = HP_UdpCast_GetRemoteAddress
del HP_UdpCast_GetRemoteAddress
def HP_UdpCast_GetRemoteAddress(UdpCast):
    return GetAddressTemplate(UdpCast, None, _HP_UdpCast_GetRemoteAddress)

_HP_Client_GetRemoteHost = HP_Client_GetRemoteHost
del HP_Client_GetRemoteHost
def HP_Client_GetRemoteHost(Client):
    return GetAddressTemplate(Client, None, _HP_Client_GetRemoteHost)

_HP_Client_GetLocalAddress = HP_Client_GetLocalAddress
del HP_Client_GetLocalAddress
def HP_Client_GetLocalAddress(Client):
    return GetAddressTemplate(Client, None, _HP_Client_GetLocalAddress)

_HP_Server_GetPendingDataLength = HP_Server_GetPendingDataLength
del HP_Server_GetPendingDataLength
def HP_Server_GetPendingDataLength(Server, ConnID):
    cPending = ctypes.c_int(0)
    if _HP_Server_GetPendingDataLength(Server, ConnID, ctypes.byref(cPending)):
        return cPending.value
    else:
        return None

_HP_Agent_GetPendingDataLength = HP_Agent_GetPendingDataLength
del HP_Agent_GetPendingDataLength
def HP_Agent_GetPendingDataLength(Server, ConnID):
    cPending = ctypes.c_int(0)
    if _HP_Agent_GetPendingDataLength(Server, ConnID, ctypes.byref(cPending)):
        return cPending.value
    else:
        return None

_HP_Server_IsPauseReceive = HP_Server_IsPauseReceive
del HP_Server_IsPauseReceive
def HP_Server_IsPauseReceive(Server, ConnID):
    cPaused = ctypes.c_bool(False)
    if _HP_Server_IsPauseReceive(Server, ConnID, ctypes.byref(cPaused)):
        return cPaused.value
    else:
        return None

_HP_Agent_IsPauseReceive = HP_Agent_IsPauseReceive
del HP_Agent_IsPauseReceive
def HP_Agent_IsPauseReceive(Server, ConnID):
    cPaused = ctypes.c_bool(False)
    if _HP_Agent_IsPauseReceive(Server, ConnID, ctypes.byref(cPaused)):
        return cPaused.value
    else:
        return None

_HP_Server_GetAllConnectionIDs = HP_Server_GetAllConnectionIDs
del HP_Server_GetAllConnectionIDs
def HP_Server_GetAllConnectionIDs(Server):
    Count = HP_Server_GetConnectionCount(Server)
    cCount = ctypes.c_uint(Count)
    IDs = (ctypes.c_uint64 * Count)()
    pIDs = ctypes.cast(IDs, ctypes.POINTER(ctypes.c_ulong))
    if _HP_Server_GetAllConnectionIDs(Server, pIDs, ctypes.byref(cCount)):
        return list(IDs)
    else:
        return None

_HP_Agent_GetAllConnectionIDs = HP_Agent_GetAllConnectionIDs
del HP_Agent_GetAllConnectionIDs
def HP_Agent_GetAllConnectionIDs(Agent):
    Count = HP_Agent_GetConnectionCount(Agent)
    cCount = ctypes.c_uint(Count)
    IDs = (ctypes.c_uint64 * Count)()
    pIDs = ctypes.cast(IDs, ctypes.POINTER(ctypes.c_uint))
    if _HP_Agent_GetAllConnectionIDs(Agent, pIDs, ctypes.byref(cCount)):
        return list(IDs)
    else:
        return None

_HP_Server_GetConnectPeriod = HP_Server_GetConnectPeriod
del HP_Server_GetConnectPeriod
def HP_Server_GetConnectPeriod(Server, ConnID):
    cPeriod = ctypes.c_int(0)
    if _HP_Server_GetConnectPeriod(Server, ConnID, ctypes.byref(cPeriod)):
        return cPeriod.value
    else:
        return None

_HP_Agent_GetConnectPeriod = HP_Agent_GetConnectPeriod
del HP_Agent_GetConnectPeriod
def HP_Agent_GetConnectPeriod(Server, ConnID):
    cPeriod = ctypes.c_int(0)
    if _HP_Agent_GetConnectPeriod(Server, ConnID, ctypes.byref(cPeriod)):
        return cPeriod.value
    else:
        return None

_HP_Server_GetSilencePeriod = HP_Server_GetSilencePeriod
del HP_Server_GetSilencePeriod
def HP_Server_GetSilencePeriod(Server, ConnID):
    cPeriod = ctypes.c_int(0)
    if _HP_Server_GetSilencePeriod(Server, ConnID, ctypes.byref(cPeriod)):
        return cPeriod.value
    else:
        return None

_HP_Agent_GetSilencePeriod = HP_Agent_GetSilencePeriod
del HP_Agent_GetSilencePeriod
def HP_Agent_GetSilencePeriod(Server, ConnID):
    cPeriod = ctypes.c_int(0)
    if _HP_Agent_GetSilencePeriod(Server, ConnID, ctypes.byref(cPeriod)):
        return cPeriod.value
    else:
        return None

_HP_Agent_Connect = HP_Agent_Connect
del HP_Agent_Connect
def HP_Agent_Connect(Agent, Host, Port):
    __target__ = (bytes(Host, 'GBK'), Port)
    cLConnID = ctypes.c_ulong(0)
    if _HP_Agent_Connect(Agent, __target__[0], __target__[1], ctypes.byref(cLConnID)):
        return cLConnID.value
    else:
        return None

_HP_Agent_ConnectWithExtra = HP_Agent_ConnectWithExtra
del HP_Agent_ConnectWithExtra
def HP_Agent_ConnectWithExtra(Agent, Host, Port, Data):
    ConnID = HP_Agent_Connect(Agent, Host, Port)
    if ConnID == None:
        return None
    HP_Agent_SetConnectionExtra(Agent, ConnID, Data)
    return ConnID

# _HP_HttpClient_GetTransferEncoding = HP_HttpClient_GetTransferEncoding
# del HP_HttpClient_GetTransferEncoding
# def HP_HttpClient_GetTransferEncoding():
#     return _HP_HttpClient_GetTransferEncoding.decode("GBK")

_HP_Client_GetLastErrorDesc = HP_Client_GetLastErrorDesc
del HP_Client_GetLastErrorDesc
def HP_Client_GetLastErrorDesc():
    return _HP_Client_GetLastErrorDesc.decode("GBK")

_HP_Agent_GetLastErrorDesc = HP_Agent_GetLastErrorDesc
del HP_Agent_GetLastErrorDesc
def HP_Agent_GetLastErrorDesc():
    return _HP_Agent_GetLastErrorDesc.decode("GBK")

_HP_Server_GetLastErrorDesc = HP_Server_GetLastErrorDesc
del HP_Server_GetLastErrorDesc
def HP_Server_GetLastErrorDesc():
    return _HP_Server_GetLastErrorDesc.decode("GBK")

# _HP_HttpClient_GetContentEncoding = HP_HttpClient_GetContentEncoding
# del HP_HttpClient_GetContentEncoding
# def HP_HttpClient_GetContentEncoding():
#     return _HP_HttpClient_GetContentEncoding.decode("GBK")

# _HP_HttpClient_GetContentType = HP_HttpClient_GetContentType
# del HP_HttpClient_GetContentType
# def HP_HttpClient_GetContentType():
#     return _HP_HttpClient_GetContentType.decode("GBK")

ServerStoreDict = {}
_HP_Server_Start = HP_Server_Start
del HP_Server_Start
def HP_Server_Start(Server, BindAddress, Port):
    global ServerStoreDict
    BindAddress = bytes(BindAddress, 'GBK')
    ServerStoreDict[Server] = (BindAddress, Port)
    return _HP_Server_Start(Server, BindAddress, Port)

AgentStoreDict = {}
_HP_Agent_Start = HP_Agent_Start
del HP_Agent_Start
def HP_Agent_Start(Agent, BindAddress, AsyncConnect):
    global AgentStoreDict
    BindAddress = bytes(BindAddress, 'GBK')
    AgentStoreDict[Agent] = BindAddress
    return _HP_Agent_Start(Agent, BindAddress, AsyncConnect)

ClientStoreDict = {}
_HP_Client_Start = HP_Client_Start
del HP_Client_Start
def HP_Client_Start(Client, BindAddress, Port, AsyncConnect):
    global ClientStoreDict
    BindAddress = bytes(BindAddress, 'GBK')
    ClientStoreDict[Client] = (BindAddress, Port)
    return _HP_Client_Start(Client, BindAddress, Port, AsyncConnect)

_HP_Client_StartWithBindAddress = HP_Client_StartWithBindAddress
del HP_Client_StartWithBindAddress
def HP_Client_StartWithBindAddress(Client, RemoteAddress, Port, AsyncConnect, BindAddress):
    global ClientStoreDict
    RemoteAddress = bytes(RemoteAddress, 'GBK')
    BindAddress = bytes(BindAddress, 'GBK')
    ClientStoreDict[Client] = (RemoteAddress, Port, BindAddress)
    return _HP_Client_Start(Client, RemoteAddress, Port, AsyncConnect)

_HP_Client_GetPendingDataLength = HP_Client_GetPendingDataLength
del HP_Client_GetPendingDataLength
def HP_Client_GetPendingDataLength(Client):
    Pending = ctypes.c_uint(0)
    if _HP_Client_GetPendingDataLength(Client, ctypes.byref(Pending)):
        return Pending.value
    else:
        return None

_HP_Client_IsPauseReceive = HP_Client_IsPauseReceive
del HP_Client_IsPauseReceive
def HP_Client_IsPauseReceive(Client):
    IsPause = ctypes.c_bool(False)
    if _HP_Client_IsPauseReceive(Client, ctypes.byref(IsPause)):
        return IsPause.value
    else:
        return None

_HP_GetSocketErrorDesc = HP_GetSocketErrorDesc
del HP_GetSocketErrorDesc
def HP_GetSocketErrorDesc(ErrorCode):
    return _HP_GetSocketErrorDesc(ErrorCode).decode("GBK")

_HP_TcpServer_SendSmallFile = HP_TcpServer_SendSmallFile
del HP_TcpServer_SendSmallFile
def HP_TcpServer_SendSmallFile(Server, ConnID, FileName, Head, Tail):
    FileName = bytes(FileName, 'GBK')

    cHead = WSABUF()
    cHead.len = len(Head)
    bHead = bytes(Head, 'GBK')
    cHead.buf = ctypes.cast(ctypes.create_string_buffer(bHead, len(bHead)), ctypes.POINTER(ctypes.c_byte))

    cTail = WSABUF()
    cTail.len = len(Tail)
    bTail = bytes(Tail, 'GBK')
    cTail.buf = ctypes.cast(ctypes.create_string_buffer(bTail, len(bTail)), ctypes.POINTER(ctypes.c_byte))

    return _HP_TcpServer_SendSmallFile(Server, ConnID, FileName, ctypes.pointer(cHead), ctypes.pointer(cTail))

_HP_TcpAgent_SendSmallFile = HP_TcpAgent_SendSmallFile
del HP_TcpAgent_SendSmallFile
def HP_TcpAgent_SendSmallFile(Agent, ConnID, FileName, Head, Tail):
    FileName = bytes(FileName, 'GBK')

    cHead = WSABUF()
    cHead.len = len(Head)
    bHead = bytes(Head, 'GBK')
    cHead.buf = ctypes.cast(ctypes.create_string_buffer(bHead, len(bHead)), ctypes.POINTER(ctypes.c_byte))

    cTail = WSABUF()
    cTail.len = len(Tail)
    bTail = bytes(Tail, 'GBK')
    cTail.buf = ctypes.cast(ctypes.create_string_buffer(bTail, len(bTail)), ctypes.POINTER(ctypes.c_byte))

    return _HP_TcpAgent_SendSmallFile(Agent, ConnID, FileName, ctypes.pointer(cHead), ctypes.pointer(cTail))

_HP_TcpClient_SendSmallFile = HP_TcpClient_SendSmallFile
del HP_TcpClient_SendSmallFile
def HP_TcpClient_SendSmallFile(Client, FileName, Head, Tail):
    FileName = bytes(FileName, 'GBK')

    cHead = WSABUF()
    cHead.len = len(Head)
    bHead = bytes(Head, 'GBK')
    cHead.buf = ctypes.cast(ctypes.create_string_buffer(bHead, len(bHead)), ctypes.POINTER(ctypes.c_byte))

    cTail = WSABUF()
    cTail.len = len(Tail)
    bTail = bytes(Tail, 'GBK')
    cTail.buf = ctypes.cast(ctypes.create_string_buffer(bTail, len(bTail)), ctypes.POINTER(ctypes.c_byte))

    return _HP_TcpClient_SendSmallFile(Client, FileName, ctypes.pointer(cHead), ctypes.pointer(cTail))

def FetchOrPeek(Sender, ConnID, Length, Callback):
    buf = ctypes.create_string_buffer(b' ' * Length, Length)
    if ConnID is not None:
        if Callback(Sender, ConnID, ctypes.cast(buf, ctypes.POINTER(ctypes.c_byte)), Length) == EnFetchResult.FR_OK:
            return ctypes.string_at(buf, Length)
        else:
            return None
    else:
        if Callback(Sender, ctypes.cast(buf, ctypes.POINTER(ctypes.c_byte)), Length) == EnFetchResult.FR_OK:
            return ctypes.string_at(buf, Length)
        else:
            return None

_HP_TcpPullServer_Fetch = HP_TcpPullServer_Fetch
del HP_TcpPullServer_Fetch
def HP_TcpPullServer_Fetch(Server, ConnID, Length):
    return FetchOrPeek(Server, ConnID, Length, _HP_TcpPullServer_Fetch)

_HP_TcpPullAgent_Fetch = HP_TcpPullAgent_Fetch
del HP_TcpPullAgent_Fetch
def HP_TcpPullAgent_Fetch(Agent, ConnID, Length):
    return FetchOrPeek(Agent, ConnID, Length, _HP_TcpPullAgent_Fetch)

_HP_TcpPullAgent_Peek = HP_TcpPullAgent_Peek
del HP_TcpPullAgent_Peek
def HP_TcpPullAgent_Peek(Agent, ConnID, Length):
    return FetchOrPeek(Agent, ConnID, Length, _HP_TcpPullAgent_Peek)

_HP_TcpPullServer_Peek = HP_TcpPullServer_Peek
del HP_TcpPullServer_Peek
def HP_TcpPullServer_Peek(Server, ConnID, Length):
    return FetchOrPeek(Server, ConnID, Length, _HP_TcpPullServer_Peek)

_HP_TcpPullClient_Fetch = HP_TcpPullClient_Fetch
del HP_TcpPullClient_Fetch
def HP_TcpPullClient_Fetch(Client, Length):
    return FetchOrPeek(Client, None, Length, _HP_TcpPullClient_Fetch)

_HP_TcpPullClient_Peek = HP_TcpPullClient_Peek
del HP_TcpPullClient_Peek
def HP_TcpPullClient_Peek(Client, Length):
    return FetchOrPeek(Client, None, Length, _HP_TcpPullClient_Peek)

def ConvertTemplate(Src, ConvCallback, GuessCallback, *OtherArgs):
    (sBuf, sLen) = ValToLP_c_byte(Src)
    DstLength = GuessCallback(sBuf, sLen)
    dBuf = ctypes.create_string_buffer(b' ' * DstLength, DstLength)
    DstLength = ctypes.c_uint(DstLength)

    if len(OtherArgs) == 0:
        result = ConvCallback(sBuf, sLen, ctypes.cast(dBuf, ctypes.POINTER(ctypes.c_byte)), ctypes.byref(DstLength))
    elif len(OtherArgs) == 5 or len(OtherArgs) == 1:
        result = ConvCallback(sBuf, sLen, ctypes.cast(dBuf, ctypes.POINTER(ctypes.c_byte)), ctypes.byref(DstLength), *OtherArgs)
    else:
        raise Exception('Bad arguments number, 4/5/9 paraments allowed.')

    if result == 0:
        return ctypes.string_at(dBuf, DstLength.value)
    elif result == -3:
        raise Exception('Bad input in %s.' % repr(ConvCallback))
    elif result == -5:
        raise Exception('Out of buffer in %s.' % repr(ConvCallback))
    else:
        raise Exception('A exception return code %d in %s' % (result, repr(ConvCallback)))

if hasattr(HPSocketDLL, "SYS_UrlDecode"):
    _SYS_UrlDecode = SYS_UrlDecode
    del SYS_UrlDecode
    def SYS_UrlDecode(Src):
        return ConvertTemplate(Src=Src, ConvCallback=_SYS_UrlDecode, GuessCallback=lambda s,l : _SYS_GuessUrlDecodeBound(s,l))

if hasattr(HPSocketDLL, "SYS_Base64Encode"):
    _SYS_Base64Encode = SYS_Base64Encode
    del SYS_Base64Encode
    def SYS_Base64Encode(Src):
        return ConvertTemplate(Src=Src, ConvCallback=_SYS_Base64Encode, GuessCallback=lambda s,l : SYS_GuessBase64EncodeBound(l))

if hasattr(HPSocketDLL, "SYS_GZipUncompress"):
    _SYS_GZipUncompress = SYS_GZipUncompress
    del SYS_GZipUncompress
    def SYS_GZipUncompress(Src):
        return ConvertTemplate(Src=Src, ConvCallback=_SYS_GZipUncompress, GuessCallback=lambda s,l : _SYS_GZipGuessUncompressBound(s,l))

if hasattr(HPSocketDLL, "SYS_UrlEncode"):
    _SYS_UrlEncode = SYS_UrlEncode
    del SYS_UrlEncode
    def SYS_UrlEncode(Src):
        return ConvertTemplate(Src=Src, ConvCallback=_SYS_UrlEncode, GuessCallback=lambda s,l : _SYS_GuessUrlEncodeBound(s,l))


if hasattr(HPSocketDLL, "SYS_Compress"):
    _SYS_Compress = SYS_Compress
    del SYS_Compress
    def SYS_Compress(Src):
        return ConvertTemplate(Src=Src, ConvCallback=_SYS_Compress, GuessCallback=lambda s,l : SYS_GuessCompressBound(l, False))


if hasattr(HPSocketDLL, "SYS_Base64Decode"):
    _SYS_Base64Decode = SYS_Base64Decode
    del SYS_Base64Decode
    def SYS_Base64Decode(Src):
        return ConvertTemplate(Src=Src, ConvCallback=_SYS_Base64Decode, GuessCallback=lambda s,l : _SYS_GuessBase64DecodeBound(s,l))


if hasattr(HPSocketDLL, "SYS_GZipCompress"):
    _SYS_GZipCompress = SYS_GZipCompress
    del SYS_GZipCompress
    def SYS_GZipCompress(Src):
        return ConvertTemplate(Src=Src, ConvCallback=_SYS_GZipCompress, GuessCallback=lambda s,l : SYS_GuessCompressBound(l, True))


if hasattr(HPSocketDLL, "SYS_Uncompress"):
    _SYS_Uncompress = SYS_Uncompress
    del SYS_Uncompress
    def SYS_Uncompress(Src):
        return ConvertTemplate(Src=Src, ConvCallback=_SYS_Uncompress, GuessCallback=lambda s,l : _SYS_GZipGuessUncompressBound(s,l))


if hasattr(HPSocketDLL, "SYS_UncompressEx"):
    _SYS_UncompressEx = SYS_UncompressEx
    del SYS_UncompressEx
    def SYS_UncompressEx(Src, WindowBits, UncompressBoundTimes = 3):
        return ConvertTemplate(Src, _SYS_UncompressEx, lambda s,l : _SYS_GZipGuessUncompressBound(s,l) * UncompressBoundTimes, WindowBits)

#
# if hasattr(HPSocketDLL, "SYS_CodePageToUnicode"):
#     _SYS_CodePageToUnicode = SYS_CodePageToUnicode
#     del SYS_CodePageToUnicode
#     def SYS_CodePageToUnicode(CodePage, Src):
#         (sBuf, sLen) = ValToLP_c_byte(Src)
#         DstLength = sLen * 2
#         dBuf = ctypes.create_unicode_buffer(' '*DstLength, DstLength)
#         DstLength = ctypes.c_int(DstLength)
#         DstLength = ctypes.c_int(DstLength)
#         if _SYS_CodePageToUnicode(CodePage, sBuf, ctypes.cast(dBuf, LP_c_wchar), ctypes.byref(DstLength)):
#             return ctypes.string_at(dBuf, DstLength.value)

#
# if hasattr(HPSocketDLL, "SYS_UnicodeToCodePage"):
#     _SYS_UnicodeToCodePage = SYS_UnicodeToCodePage
#     del SYS_UnicodeToCodePage
#     def SYS_UnicodeToCodePage(CodePage, WSrc):
#         (sBuf, sLen) = WValToLP_c_wchar(WSrc)
#         DstLength = sLen * 4
#         dBuf = ctypes.create_string_buffer(b' '*DstLength, DstLength)
#         if _SYS_UnicodeToCodePage(CodePage, sBuf, ctypes.cast(dBuf, LP_c_byte), ctypes.byref(DstLength)):
#             return ctypes.string_at(dBuf, DstLength.value)


if hasattr(HPSocketDLL, "SYS_CompressEx"):
    _SYS_CompressEx = SYS_CompressEx
    del SYS_CompressEx
    def SYS_CompressEx(Src, Level, Method, WindowBits, MemLevel, Strategy):
        return ConvertTemplate(Src, _SYS_CompressEx, lambda s,l : SYS_GuessCompressBound(l, False), Level, Method, WindowBits, MemLevel, Strategy)


def GuessTemplate(Src, Callback):
    (sBuf, sLen) = ValToLP_c_byte(Src)
    return Callback(sBuf, sLen)

if hasattr(HPSocketDLL, "SYS_GZipGuessUncompressBound"):
    _SYS_GZipGuessUncompressBound = SYS_GZipGuessUncompressBound
    del SYS_GZipGuessUncompressBound
    def SYS_GZipGuessUncompressBound(Src):
        return GuessTemplate(Src, _SYS_GZipGuessUncompressBound)

if hasattr(HPSocketDLL, "SYS_GuessUrlDecodeBound"):
    _SYS_GuessUrlDecodeBound = SYS_GuessUrlDecodeBound
    del SYS_GuessUrlDecodeBound
    def SYS_GuessUrlDecodeBound(Src):
        return GuessTemplate(Src, _SYS_GuessUrlDecodeBound)

if hasattr(HPSocketDLL, "SYS_GuessUrlEncodeBound"):
    _SYS_GuessUrlEncodeBound = SYS_GuessUrlEncodeBound
    del SYS_GuessUrlEncodeBound
    def SYS_GuessUrlEncodeBound(Src):
        return GuessTemplate(Src, _SYS_GuessUrlEncodeBound)

if hasattr(HPSocketDLL, "SYS_GuessBase64DecodeBound"):
    _SYS_GuessBase64DecodeBound = SYS_GuessBase64DecodeBound
    del SYS_GuessBase64DecodeBound
    def SYS_GuessBase64DecodeBound(Src):
        return GuessTemplate(Src, _SYS_GuessBase64DecodeBound)

if hasattr(HPSocketDLL, "SYS_EnumHostIPAddresses") and hasattr(HPSocketDLL, "SYS_FreeHostIPAddresses"):
    _SYS_EnumHostIPAddresses = SYS_EnumHostIPAddresses
    _SYS_FreeHostIPAddresses = SYS_FreeHostIPAddresses
    del SYS_EnumHostIPAddresses
    del SYS_FreeHostIPAddresses
    def SYS_EnumHostIPAddresses(Host, En_HP_IPAddrType):
        Host = ctypes.create_string_buffer(bytes(Host, 'GBK'))
        Count = ctypes.c_int(0)
        lp = ctypes.c_void_p(0)
        lpp = ctypes.cast(lp, ctypes.POINTER(HP_LPTIPAddr))
        IPAddrs = []
        if _SYS_EnumHostIPAddresses(ctypes.cast(Host, ctypes.c_char_p), En_HP_IPAddrType, ctypes.byref(lpp), ctypes.byref(Count)):
            # lpp.contents.contents.[type|address]
            # lpp 指向一个指针数组，数组中的每一项都是 HP_LPTIPAddr
            zlpp = ctypes.cast(lpp, ctypes.POINTER(HP_LPTIPAddr * Count.value))
            for i in range(Count.value):
                IPAddr = zlpp.contents[i].contents
                IPAddrs.append((IPAddr.type, IPAddr.address.decode()))
            _SYS_FreeHostIPAddresses(lpp)
            return IPAddrs
        else:
            return None

if hasattr(HPSocketDLL, "SYS_GbkToUnicode"):
    _SYS_GbkToUnicode = SYS_GbkToUnicode
    del SYS_GbkToUnicode
    def SYS_GbkToUnicode(Src):
        (bSrc, sLen) = ValToLP_c_byte(Src)
        dLen = sLen * 3
        bDst = ctypes.create_unicode_buffer(u' ' * dLen, dLen)
        dLen = ctypes.c_long(dLen)
        if _SYS_GbkToUnicode(ctypes.cast(bSrc, ctypes.c_char_p), ctypes.cast(bDst, ctypes.c_wchar_p), ctypes.byref(dLen)):
            return bDst.value
        else:
            return None

if hasattr(HPSocketDLL, "SYS_Utf8ToUnicode"):
    _SYS_Utf8ToUnicode = SYS_Utf8ToUnicode
    del SYS_Utf8ToUnicode
    def SYS_Utf8ToUnicode(Src):
        (bSrc, sLen) = ValToLP_c_byte(Src, 'utf-8')
        dLen = sLen * 3
        bDst = ctypes.create_unicode_buffer(u' ' * dLen, dLen)
        dLen = ctypes.c_long(dLen)
        if _SYS_Utf8ToUnicode(ctypes.cast(bSrc, ctypes.c_char_p), ctypes.cast(bDst, ctypes.c_wchar_p), ctypes.byref(dLen)):
            return bDst.value
        else:
            return None

if hasattr(HPSocketDLL, "SYS_GbkToUtf8"):
    _SYS_GbkToUtf8 = SYS_GbkToUtf8
    del SYS_GbkToUtf8
    def SYS_GbkToUtf8(Src):
        (bSrc, sLen) = ValToLP_c_byte(Src)
        dLen = sLen * 3
        bDst = ctypes.create_string_buffer(b' ' * dLen, dLen)
        dLen = ctypes.c_long(dLen)
        if _SYS_GbkToUtf8(ctypes.cast(bSrc, ctypes.c_char_p), ctypes.cast(bDst, ctypes.c_char_p), ctypes.byref(dLen)):
            return bDst.value
        else:
            return None

if hasattr(HPSocketDLL, "SYS_Utf8ToGbk"):
    _SYS_Utf8ToGbk = SYS_Utf8ToGbk
    del SYS_Utf8ToGbk
    def SYS_Utf8ToGbk(Src):
        (bSrc, sLen) = ValToLP_c_byte(Src)
        dLen = sLen * 3
        bDst = ctypes.create_string_buffer(b' ' * dLen, dLen)
        dLen = ctypes.c_long(dLen)
        if _SYS_Utf8ToGbk(ctypes.cast(bSrc, ctypes.c_char_p), ctypes.cast(bDst, ctypes.c_char_p), ctypes.byref(dLen)):
            return bDst.value
        else:
            return None

if hasattr(HPSocketDLL, "SYS_GetIPAddress"):
    _SYS_GetIPAddress = SYS_GetIPAddress
    del SYS_GetIPAddress
    def SYS_GetIPAddress(Host):
        IPLen = 30
        cIP = ctypes.create_string_buffer(b' '*IPLen, IPLen)
        IPLen = ctypes.c_int(IPLen)
        (bHost, sLen) = ValToLP_c_byte(Host)
        IPAddrType = ctypes.c_int(0)
        if _SYS_GetIPAddress(ctypes.cast(bHost, ctypes.c_char_p), ctypes.cast(cIP, ctypes.c_char_p), ctypes.byref(IPLen), ctypes.byref(IPAddrType)):
            return (ctypes.string_at(cIP, IPLen.value).decode('GBK'), IPAddrType.value)
        else:
            return None

if hasattr(HPSocketDLL, "SYS_GetSocketLocalAddress"):
    _SYS_GetSocketLocalAddress = SYS_GetSocketLocalAddress
    del SYS_GetSocketLocalAddress
    def SYS_GetSocketLocalAddress(socket):
        return GetAddressTemplate(socket, None, _SYS_GetSocketLocalAddress)

if hasattr(HPSocketDLL, "SYS_GetSocketRemoteAddress"):
    _SYS_GetSocketRemoteAddress = SYS_GetSocketRemoteAddress
    del SYS_GetSocketRemoteAddress
    def SYS_GetSocketRemoteAddress(socket):
        return GetAddressTemplate(socket, None, _SYS_GetSocketRemoteAddress)

if hasattr(HPSocketDLL, "SYS_SetSocketOption"):
    _SYS_SetSocketOption = SYS_SetSocketOption
    del SYS_SetSocketOption
    def SYS_SetSocketOption(socket, level, name, val, len):
        if isinstance(val, int):
            val = ctypes.c_int(val)
        elif isinstance(val, str) or isinstance(val, bytes):
            (val,tlen) = ValToLP_c_byte(val)
        elif isinstance(val, bool):
            val = ctypes.c_bool(val)
        elif isinstance(val, float):
            val = ctypes.c_float(val)
        else:
            raise TypeError('Only int/bytes/str/bool/float Support.')
        return _SYS_SetSocketOption(socket, level, name, ctypes.cast(ctypes.addressof(val), ctypes.c_void_p), len)

if hasattr(HPSocketDLL, "SYS_GetSocketOption"):
    _SYS_GetSocketOption = SYS_GetSocketOption
    del SYS_GetSocketOption
    def SYS_GetSocketOption(socket, level, name, type, len):
        buf = ctypes.create_string_buffer(b' '*len, len)
        _SYS_GetSocketOption(socket, level, name, ctypes.cast(buf, ctypes.c_void_p), ctypes.byref(len))
        if type is int:
            return ctypes.cast(buf, ctypes.POINTER(ctypes.c_int)).contents.value
        elif type is str:
            return ctypes.string_at(buf, len.value).decode('GBK')
        elif type is bytes:
            return ctypes.string_at(buf, len.value)
        elif type is bool:
            return ctypes.cast(buf, ctypes.POINTER(ctypes.c_bool)).contents.value
        elif type is float:
            return ctypes.cast(buf, ctypes.POINTER(ctypes.c_float)).contents.value
        else:
            raise TypeError('Only int/bytes/str/bool/float Support.')

if hasattr(HPSocketDLL, "SYS_IsIPAddress"):
    _SYS_IsIPAddress = SYS_IsIPAddress
    del SYS_IsIPAddress
    def SYS_IsIPAddress(Address):
        (Address, Length) = ValToLP_c_byte(Address)
        type = ctypes.c_int(0)
        if _SYS_IsIPAddress(ctypes.cast(Address, ctypes.c_char_p), ctypes.cast(ctypes.byref(type), ctypes.POINTER(En_HP_IPAddrType))):
            return type.value
        else:
            return False

if hasattr(HPSocketDLL, "SYS_UnicodeToUtf8"):
    _SYS_UnicodeToUtf8 = SYS_UnicodeToUtf8
    del SYS_UnicodeToUtf8
    def SYS_UnicodeToUtf8(WSrc):
        (sBuf, sLen) = WValToLP_c_wchar(WSrc)
        DstLength = sLen * 3
        dBuf = ctypes.create_string_buffer(b' '*DstLength, DstLength)
        if _SYS_UnicodeToUtf8(sBuf, ctypes.cast(dBuf, LP_c_byte), ctypes.byref(DstLength)):
            return ctypes.string_at(dBuf, DstLength.value)

if hasattr(HPSocketDLL, "SYS_UnicodeToGbk"):
    _SYS_UnicodeToGbk = SYS_UnicodeToGbk
    del SYS_UnicodeToGbk
    def SYS_UnicodeToGbk(WSrc):
        (sBuf, sLen) = WValToLP_c_wchar(WSrc)
        DstLength = sLen * 3
        dBuf = ctypes.create_string_buffer(b' '*DstLength, DstLength)
        if _SYS_UnicodeToGbk(sBuf, ctypes.cast(dBuf, LP_c_byte), ctypes.byref(DstLength)):
            return ctypes.string_at(dBuf, DstLength.value)

_HP_Agent_ConnectWithLocalPort = HP_Agent_ConnectWithLocalPort
del HP_Agent_ConnectWithLocalPort
def HP_Agent_ConnectWithLocalPort(Agent, RemoteIP, RemotePort, LocalPort = 0):
    global AgentStoreDict
    ConnID = 0
    cConnID = ctypes.c_ulong(ConnID)
    pConnID = ctypes.pointer(cConnID)
    RemoteIP = bytes(RemoteIP, 'GBK')
    AgentStoreDict[Agent] = RemoteIP
    if (HP_Agent_ConnectWithLocalPort(Agent, RemoteIP, RemotePort, pConnID, LocalPort)):
        ConnID = pConnID.contents.value
        return ConnID
    else:
        return False

_HP_Agent_ConnectWithExtraAndLocalPort = HP_Agent_ConnectWithExtraAndLocalPort
del HP_Agent_ConnectWithExtraAndLocalPort
def HP_Agent_ConnectWithExtraAndLocalPort(Agent, RemoteIP, RemotePort, Extra, LocalPort):
    global AgentStoreDict
    ConnID = 0
    cConnID = ctypes.c_ulong(ConnID)
    pConnID = ctypes.pointer(cConnID)
    RemoteIP = bytes(RemoteIP, 'GBK')
    AgentStoreDict[Agent] = RemoteIP
    if _HP_Agent_ConnectWithExtraAndLocalPort(Agent, RemoteIP, RemotePort, pConnID, LocalPort):
        ConnID = pConnID.contents.value
        AgentConnectionExtra.Set(S=Agent, C=ConnID, Data=Extra)
        return ConnID
    else:
        return False

_HP_HttpCookie_HLP_ParseExpires = HP_HttpCookie_HLP_ParseExpires
del HP_HttpCookie_HLP_ParseExpires
def HP_HttpCookie_HLP_ParseExpires(CookieExpires):
    tmExpires = ctypes.c_int(0)
    ptmExpires = ctypes.pointer(tmExpires)
    if HP_HttpCookie_HLP_ParseExpires(CookieExpires):
        return ptmExpires.contents.value
    else:
        return False

_HP_HttpClient_GetHeader = HP_HttpClient_GetHeader
del HP_HttpClient_GetHeader
def HP_HttpClient_GetHeader(Client, Name):
    lpszValue = ctypes.c_char_p(0)
