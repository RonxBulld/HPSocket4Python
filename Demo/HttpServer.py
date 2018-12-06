# coding: utf-8

import time,sys,os
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/../')

from HPSocket import Http
from HPSocket import helper
import HPSocket.pyhpsocket as HPSocket

class Server(Http.HP_HTTPServer):
    @Http.HP_HTTPServer.ParseEventDescription
    def OnMessageComplete(self, Sender, ConnID):
        print("[Trace][HttpServer]OnMessageComplete(%d)" % ConnID)



if __name__ == '__main__':
    svr = Server()
    svr.Start("0.0.0.0", 8081)
    while True:
        time.sleep(1)
