# coding: utf-8

import time,sys,os
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'\\..\\')

import TcpPull
import utils,ctypes
import TcpPull.helper as helper


class Client(TcpPull.HP_TcpPullClient):
    @TcpPull.HP_TcpPullServer.EventDescription
    def Start(self, host, port):
        if super().Start(host,port):
            print('Start server success, listen on %s:%d'%(host,port))
        else:
            print('Start server fail.')

    @TcpPull.HP_TcpPullClient.EventDescription
    def OnConnect(self, Sender, ConnID):
        print('Connected.')
        return TcpPull.EnHandleResult.HR_OK

    @TcpPull.HP_TcpPullClient.EventDescription
    def OnReceiveHead(self, Sender, ConnID, Seq: int, Length: int):
        print('[TRACR] [Client] head -> seq: %d, body_len: %d' % (Seq, Length))

    @TcpPull.HP_TcpPullClient.EventDescription
    def OnReceiveBody(self, Sender, ConnID, Body: bytes):
        pkg = helper.GeneratePkg(Body)
        print('[TRACE] [Client] body -> name: %s, age: %d, desc: %s' % (pkg.name,pkg.age,pkg.desc))

    def SendTest(self):
        self.SEQ += 1
        buffer = helper.GeneratePkgBuffer(seq=self.SEQ, name='伤神恶趣味', age=23, desc='text to be sent')
        self.Send(self.Client, buffer)


cnt = Client()
cnt.Start('127.0.0.1',5555)
for i in range(5):
    cnt.SendTest()
time.sleep(1)
