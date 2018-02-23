# coding: utf-8

import time,sys,os
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'\\..\\')

import TcpPull
import utils
import TcpPull.helper as helper

class Server(TcpPull.HP_TcpPullServer):
    def Start(self, host, port):
        if super().Start(host,port):
            print('Start server success, listen on %s:%d'%(host,port))
            return True
        else:
            print('Start server fail.')
            return False

    @TcpPull.HP_TcpPullServer.EventDescription
    def OnAccept(self, Sender, ConnID, Client):
        self.pkg = helper.TPkgInfo(True, utils.SizeOf(helper.TPkgHeader))
        TcpPull.HP_Server_SetConnectionExtra(Sender, ConnID, utils.MakePointer(self.pkg))
        return TcpPull.EnHandleResult.HR_OK

    @TcpPull.HP_TcpPullServer.EventDescription
    def OnReceiveHead(self, Sender, ConnID, Seq:int, Length:int):
        print('[TRACR] [Server] head -> seq: %d, body_len: %d' % (Seq, Length))

    @TcpPull.HP_TcpPullServer.EventDescription
    def OnReceiveBody(self, Sender, ConnID, Body: bytes):
        pkg = helper.GeneratePkg(Body)
        print('[TRACE] body -> name: %s, age: %d, desc: %s' % (pkg.name,pkg.age,pkg.desc))


svr = Server()
if svr.Start('0.0.0.0',5555):
    while True:
        time.sleep(1)
