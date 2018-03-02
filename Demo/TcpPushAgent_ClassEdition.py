# coding: utf-8

import time,sys,os
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/../')

from HPSocket import TcpPush
from HPSocket import helper
import HPSocket.pyhpsocket as HPSocket

class Agent(TcpPush.HP_TcpPushAgent):
    EventDescription = TcpPush.HP_TcpPushAgent.EventDescription

    @EventDescription
    def OnConnect(self, Sender, ConnID):
        (ip,port)=HPSocket.HP_Agent_GetLocalAddress(Sender=Sender, ConnID=ConnID)
        print('[TRACER] [Agent] Connect Success: %s:%d in ConnID(%d)' % (ip.decode('GBK'),port,ConnID))

    @EventDescription
    def OnSend(self, Sender, ConnID, Data, Length):
        print('[TRACER] [Agent] Send(%d) -> %s' % (ConnID, Data))

    @EventDescription
    def OnReceive(self, Sender, ConnID, Data, Length):
        print('[TRACE] [Agent] body(%d) -> %s' % (ConnID, repr(Data)))
        self.SendTest(ConnID = ConnID)
        return HPSocket.EnHandleResult.HR_OK

    @EventDescription
    def OnClose(self, Sender, ConnID, Operation, ErrorCode):
        print('[TRACE] [Agent] Close(%d): Opt=%d, Err=%d' % (ConnID, Operation, ErrorCode))

    @EventDescription
    def OnShutdown(self, Sender):
        print('[TRACE] [Agent] Agent is shutdown now.')

    @EventDescription
    def SendTest(self, ConnID):
        self.SEQ += 1
        buffer = helper.GeneratePkgBuffer(seq=self.SEQ, name='伤神恶趣味', age=23, desc='text to be sent\x00')
        suc = self.Send(self.Agent, ConnID, buffer)
        return suc


if __name__ == '__main__':
    agt = Agent()
    agt.Start('0.0.0.0')
    for i in range(10):
        ConnID = agt.Connect('127.0.0.1', 5555)
        if ConnID != None:
            agt.SendTest(ConnID)
    while True:
        time.sleep(1)