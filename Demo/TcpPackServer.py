# coding: utf-8

import time,sys,os
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/../')

from HPSocket import TcpPack
from HPSocket import helper
import HPSocket.pyhpsocket as HPSocket

class Server(TcpPack.HP_TcpPackServer):
    EventDescription = TcpPack.HP_TcpPackServer.EventDescription

    @EventDescription
    def OnAccept(self, Sender, ConnID, Client):
        (ip,port) = HPSocket.HP_Server_GetRemoteAddress(Sender=Sender, ConnID=ConnID)
        print('[%d, OnAccept] < %s' % (ConnID, (ip, port)))

    @EventDescription
    def OnSend(self, Sender, ConnID, Data):
        print('[%d, OnSend] > %s' % (ConnID, repr(Data)))

    @EventDescription
    def OnReceive(self, Sender, ConnID, Data):
        print('[%d, OnReceive] < %s' % (ConnID, repr(Data)))
        self.Send(Sender=Sender, ConnID=ConnID, Data=Data)
        return HPSocket.EnHandleResult.HR_OK

    def OnClose(self, Sender, ConnID, Operation, ErrorCode):
        (ip, port) = HPSocket.HP_Server_GetRemoteAddress(Sender=Sender, ConnID=ConnID)
        print('[%d, OnClose] > %s opt=%d err=%d' % (ConnID, (ip, port), Operation, ErrorCode))
        return HPSocket.EnHandleResult.HR_OK


if __name__ == '__main__':
    svr = Server()
    svr.Start(host='0.0.0.0', port=5555, head_flag=0x169)
    while True:
        time.sleep(1)