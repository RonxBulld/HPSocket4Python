# coding: utf-8

import time
import TcpPull
import helper


class Server(TcpPull.HP_TcpPullServer):
    @TcpPull.HP_TcpPullServer.EventDescription
    def OnAccept(self, Sender, ConnID, Client):
        self.pkg = helper.TPkgInfo(True, TcpPull.SizeOf(helper.TPkgHeader))
        TcpPull.HP_Server_SetConnectionExtra(Sender, ConnID, TcpPull.MakePointer(self.pkg))
        return TcpPull.EnHandleResult.HR_OK

    @TcpPull.HP_TcpPullServer.EventDescription
    def OnReceiveHead(self, Sender, ConnID, Seq:int, Length:int):
        print('[TRACR] [Server] head -> seq: %d, body_len: %d' % (Seq, Length))

    @TcpPull.HP_TcpPullServer.EventDescription
    def OnReceiveBody(self, Sender, ConnID, Body: bytes):
        BodyStruct = helper.CBuffer(Body)
        pBody = BodyStruct.ToOtherPtr(helper.TPkgBody)
        # 下面的转换需要小心，因为如果使用错误的字符集会导致crash
        name = pBody.contents.name.decode('GBK')  # name = bytes.decode(pBody->name, 'GBK')
        # 这里由于 python 语言的限制，没有 C 那么灵活所以 desc 部分单独拿出来处理
        # 下面的转换需要小心，因为如果使用错误的字符集会导致crash
        desc = BodyStruct[TcpPull.SizeOf(helper.TPkgBody):].decode('GBK')
        print('[TRACE] body -> name: %s, age: %d, desc: %s' % (name, pBody.contents.age, desc))


svr = Server()
svr.Start('0.0.0.0',5555)
while True:
    time.sleep(1)