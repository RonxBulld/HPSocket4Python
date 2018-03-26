# coding: utf-8

import time,sys,os
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/../')

from HPSocket import TcpPull
from HPSocket import helper
import HPSocket.pyhpsocket as HPSocket

class Agent(TcpPull.HP_TcpPullAgent):
    @TcpPull.HP_TcpPullAgent.EventDescription
    def OnConnect(self, Sender, ConnID):
        (ip,port)=HPSocket.HP_Agent_GetLocalAddress(Sender=Sender, ConnID=ConnID)
        print('[TRACER] [Agent] Connect Success: %s:%d in ConnID(%d)' % (ip,port,ConnID))

    @TcpPull.HP_TcpPullAgent.EventDescription
    def OnSend(self, Sender, ConnID, Data):
        print('[TRACER] [Agent] Send(%d) -> %s' % (ConnID, Data))

    @TcpPull.HP_TcpPullAgent.EventDescription
    def OnReceiveHead(self, Sender, ConnID, Seq: int, Length: int, raw:bytes):
        print('[TRACE] [Agent] head(%d) -> seq: %d, body_len: %d' % (ConnID, Seq, Length))
        # self.Send(Sender=Sender, ConnID=ConnID, Data=raw)

    @TcpPull.HP_TcpPullAgent.EventDescription
    def OnReceiveBody(self, Sender, ConnID, Body: bytes):
        (name, age, desc) = helper.GeneratePkg(Body)
        print('[TRACE] [Agent] body(%d) -> name: %s, age: %d, desc: %s' % (ConnID, name, age, desc))
        self.SendTest(ConnID=ConnID)

    @TcpPull.HP_TcpPullAgent.EventDescription
    def OnClose(self, Sender, ConnID, Operation, ErrorCode):
        print('[TRACE] [Agent] Close(%d): Opt=%d, Err=%d' % (ConnID, Operation, ErrorCode))

    @TcpPull.HP_TcpPullAgent.EventDescription
    def OnShutdown(self, Sender):
        print('[TRACE] [Agent] Agent is shutdown now.')

    @TcpPull.HP_TcpPullAgent.EventDescription
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
        if ConnID is not None:
            agt.SendTest(ConnID)
    while True:
        time.sleep(1)