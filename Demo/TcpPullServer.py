# coding: utf-8

import time,sys,os
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/../')

from HPSocket import TcpPull
from HPSocket import helper
import HPSocket.pyhpsocket as HPSocket

class Server(TcpPull.HP_TcpPullServer):
    def Start(self, host, port):
        if super().Start(host,port):
            print('Start server success, listen on %s:%d'%(host,port))
            return True
        else:
            print('Start server fail.')
            return False

    @TcpPull.HP_TcpPullServer.EventDescription
    def OnPrepareListen(self, Sender, SocketHandler):
        return HPSocket.EnHandleResult.HR_OK

    @TcpPull.HP_TcpPullServer.EventDescription
    def OnSend(self, Sender, ConnID, Data):
        print('[TRACR] [Server] send to %d -> [length=%d]%s'%(ConnID, len(Data), repr(Data)))
        return HPSocket.EnHandleResult.HR_OK

    @TcpPull.HP_TcpPullServer.EventDescription
    def OnClose(self, Sender, ConnID, Operation, ErrorCode):
        print('The custom out: %d[Opt=%d, Err=%d]'%(ConnID, Operation, ErrorCode))
        return HPSocket.EnHandleResult.HR_OK

    @TcpPull.HP_TcpPullServer.EventDescription
    def OnAccept(self, Sender, ConnID, Client):
        pkg = helper.TPkgInfo(True, helper.TPkgHeaderSize)     # 这块内存需要保护起来
        HPSocket.HP_Server_SetConnectionExtra(Sender, ConnID, pkg)
        print('New custom in: %d'%ConnID)
        return HPSocket.EnHandleResult.HR_OK

    @TcpPull.HP_TcpPullServer.EventDescription
    def OnReceiveHead(self, Sender, ConnID, Seq:int, Length:int, raw:bytes):
        print('[TRACR] [Server] head -> seq: %d, body_len: %d' % (Seq, Length))
        self.Send(Sender, ConnID, raw)

    @TcpPull.HP_TcpPullServer.EventDescription
    def OnReceiveBody(self, Sender, ConnID, Body: bytes, raw:bytes):
        (name, age, desc) = helper.GeneratePkg(Body)
        print('[TRACE] body -> name: %s, age: %d, desc: %s' % (name,age,desc))
        Buf = helper.GeneratePkgBuffer(seq=-1,name=name,age=age,desc=desc)
        self.Send(Sender, ConnID, raw)

if __name__ == '__main__':
    svr = Server()
    if svr.Start('0.0.0.0',5555):
        while True:
            time.sleep(1)
