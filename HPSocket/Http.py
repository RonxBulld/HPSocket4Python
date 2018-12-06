# coding: utf-8
"""HP_HTTP 类"""
import ctypes
import HPSocket.helper as helper
import HPSocket.pyhpsocket as HPSocket

class HP_HTTP:
    Listener = None
    target = ('', 0)
    EnHandleResult = HPSocket.EnHandleResult
    EnHPHttpParseResult = HPSocket.EnHttpParseResult

    def EventDescription(fn):
        def arguments(*args, **kwargs):
            retval = fn(*args, **kwargs)
            return retval if isinstance(retval, ctypes.c_int) else HPSocket.EnHandleResult.HR_OK
        return arguments

    def ParseEventDescription(fn):
        def arguments(*args, **kwargs):
            retval = fn(*args, **kwargs)
            return retval if isinstance(retval, ctypes.c_int) else HPSocket.EnHttpParseResult.HPR_OK
        return arguments

    @ParseEventDescription
    def OnMessageBegin(self, Sender, ConnID):
        return HP_HTTP.EnHPHttpParseResult.HPR_OK

    @ParseEventDescription
    def OnRequestLine(self, Sender, ConnID, Method, Url):
        return HP_HTTP.EnHPHttpParseResult.HPR_OK

    @ParseEventDescription
    def OnStatusLine(self, Sender, ConnID, StatusCode, Desc):
        return HP_HTTP.EnHPHttpParseResult.HPR_OK

    @ParseEventDescription
    def OnHeader(self, Sender, ConnID, Name, Value):
        return HP_HTTP.EnHPHttpParseResult.HPR_OK

    @ParseEventDescription
    def OnHeadersComplete(self, Sender, ConnID):
        return HP_HTTP.EnHPHttpParseResult.HPR_OK

    @ParseEventDescription
    def OnBodyWarp(self, Sender, ConnID, Data, Length):
        return self.OnBody(Sender=Sender, ConnID=ConnID, Data=ctypes.string_at(Data, Length))

    @ParseEventDescription
    def OnBody(self, Sender, ConnID, Data):
        return HP_HTTP.EnHPHttpParseResult.HPR_OK

    @ParseEventDescription
    def OnChunkHeader(self, Sender, ConnID, Length):
        return HP_HTTP.EnHPHttpParseResult.HPR_OK

    @ParseEventDescription
    def OnChunkComplete(self, Sender, ConnID):
        return HP_HTTP.EnHPHttpParseResult.HPR_OK

    @ParseEventDescription
    def OnMessageComplete(self, Sender, ConnID):
        return HP_HTTP.EnHPHttpParseResult.HPR_OK

    @ParseEventDescription
    def OnUpgrade(self, Sender, ConnID, UpgradeType):
        return HP_HTTP.EnHPHttpParseResult.HPR_OK

    @ParseEventDescription
    def OnParseError(self, Sender, ConnID, ErrorCode, ErrorDesc):
        return HP_HTTP.EnHPHttpParseResult.HPR_OK

    @EventDescription
    def OnWSMessageHeader(self, Sender, ConnID, Final, Reserved, OperationCode, Mask, BodyLen):
        return HP_HTTP.EnHandleResult.HR_OK

    @EventDescription
    def OnWSMessageBodyWarp(self, Sender, ConnID, Data, Length):
        return self.OnWSMessageBody(Sender=Sender, ConnID=ConnID, Data=ctypes.string_at(Data, Length))

    @EventDescription
    def OnWSMessageBody(self, Sender, ConnID, Data):
        return HP_HTTP.EnHandleResult.HR_OK

    @EventDescription
    def OnWSMessageComplete(self, Sender, ConnID):
        return HP_HTTP.EnHandleResult.HR_OK


class HP_HTTPServer(HP_HTTP):
    Server = None

    def __init__(self):
        self.Listener = HPSocket.Create_HP_HttpServerListener()
        self.Server = HPSocket.Create_HP_HttpServer(self.Listener)

        self.OnMessageBeginHandle = HPSocket.HP_FN_HttpServer_OnMessageBegin(self.OnMessageBegin)
        self.OnRequestLineHandle = HPSocket.HP_FN_HttpServer_OnRequestLine(self.OnRequestLine)
        self.OnHeaderHandle = HPSocket.HP_FN_HttpServer_OnHeader(self.OnHeader)
        self.OnHeadersCompleteHandle = HPSocket.HP_FN_HttpServer_OnHeadersComplete(self.OnHeadersComplete)
        self.OnBodyHandle = HPSocket.HP_FN_HttpServer_OnBody(self.OnBodyWarp)
        self.OnChunkHeaderHandle = HPSocket.HP_FN_HttpServer_OnChunkHeader(self.OnChunkHeader)
        self.OnChunkCompleteHandle = HPSocket.HP_FN_HttpServer_OnChunkComplete(self.OnChunkComplete)
        self.OnMessageCompleteHandle = HPSocket.HP_FN_HttpServer_OnMessageComplete(self.OnMessageComplete)
        self.OnUpgradeHandle = HPSocket.HP_FN_HttpServer_OnUpgrade(self.OnUpgrade)
        self.OnParseErrorHandle = HPSocket.HP_FN_HttpServer_OnParseError(self.OnParseError)
        self.OnWSMessageHeaderHandle = HPSocket.HP_FN_HttpServer_OnWSMessageHeader(self.OnWSMessageHeader)
        self.OnWSMessageBodyHandle = HPSocket.HP_FN_HttpServer_OnWSMessageBody(self.OnWSMessageBodyWarp)
        self.OnWSMessageCompleteHandle = HPSocket.HP_FN_HttpServer_OnWSMessageComplete(self.OnWSMessageComplete)

        HPSocket.HP_Set_FN_HttpServer_OnMessageBegin(self.Listener, self.OnMessageBeginHandle)
        HPSocket.HP_Set_FN_HttpServer_OnRequestLine(self.Listener, self.OnRequestLineHandle)
        HPSocket.HP_Set_FN_HttpServer_OnHeader(self.Listener, self.OnHeaderHandle)
        HPSocket.HP_Set_FN_HttpServer_OnHeadersComplete(self.Listener, self.OnHeadersCompleteHandle)
        HPSocket.HP_Set_FN_HttpServer_OnBody(self.Listener, self.OnBodyHandle)
        HPSocket.HP_Set_FN_HttpServer_OnChunkHeader(self.Listener, self.OnChunkHeaderHandle)
        HPSocket.HP_Set_FN_HttpServer_OnChunkComplete(self.Listener, self.OnChunkCompleteHandle)
        HPSocket.HP_Set_FN_HttpServer_OnMessageComplete(self.Listener, self.OnMessageCompleteHandle)
        HPSocket.HP_Set_FN_HttpServer_OnUpgrade(self.Listener, self.OnUpgradeHandle)
        HPSocket.HP_Set_FN_HttpServer_OnParseError(self.Listener, self.OnParseErrorHandle)
        HPSocket.HP_Set_FN_HttpServer_OnWSMessageHeader(self.Listener, self.OnWSMessageHeaderHandle)
        HPSocket.HP_Set_FN_HttpServer_OnWSMessageBody(self.Listener, self.OnWSMessageBodyHandle)
        HPSocket.HP_Set_FN_HttpServer_OnWSMessageComplete(self.Listener, self.OnWSMessageCompleteHandle)

    def __del__(self):
        HPSocket.Destroy_HP_HttpServer(self.Server)
        HPSocket.Destroy_HP_HttpServerListener(self.Listener)

    def Start(self, host, port):
        self.target = (host, port)
        return HPSocket.HP_Server_Start(self.Server, self.target[0], self.target[1])