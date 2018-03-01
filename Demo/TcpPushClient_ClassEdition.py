# coding: utf-8

import time,sys,os
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'\\..\\')

from HPSocket import TcpPush
from HPSocket import helper
import HPSocket.pyhpsocket as HPSocket

class Client(TcpPush.HP_TcpPushClient):
    counter = 0
    EventDescription = TcpPush.HP_TcpPushServer.EventDescription

    @EventDescription
    def OnSend(self, Sender, ConnID, Data, Length):
        print('[%d, OnSend] < %s' % (ConnID, repr(Data)))

    @EventDescription
    def OnConnect(self, Sender, ConnID):
        print('[%d, OnConnect] Success.' % ConnID)

    @EventDescription
    def OnReceive(self, Sender, ConnID, Data, Length):
        print('[%d, OnReceive] < %s' % (ConnID, repr(Data)))
        self.SendTest()

    def SendTest(self):
        self.counter += 1
        self.Send(self.Client, 'text to be sent - %d' % self.counter)


if __name__ == '__main__':
    cnt = Client()
    cnt.Start(host='127.0.0.1', port=5555)
    cnt.SendTest()
    while True:
        time.sleep(1)