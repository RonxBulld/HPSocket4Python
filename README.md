# HPSocket4Python
## 1.快速预览
HPSocket4Python 是 HPSocket 的 Python 绑定，力图在 Python 上更方便的使用 HPSocket 组件。目前已经可以通过继承类的方式来使用 Tcp_Push_Server。
代码形如：
```
# coding: utf-8

import time,sys,os
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/../')

from HPSocket import TcpPush
from HPSocket import helper
import HPSocket.pyhpsocket as HPSocket

class Server(TcpPush.HP_TcpPushServer):
    EventDescription = TcpPush.HP_TcpPushServer.EventDescription

    @EventDescription
    def OnAccept(self, Sender, ConnID, Client):
        (ip,port) = HPSocket.HP_Server_GetRemoteAddress(Sender=Sender, ConnID=ConnID)
        print('[%d, OnAccept] < %s' % (ConnID, (ip, port)))
        print('Current connected: %s' % repr(HPSocket.HP_Server_GetAllConnectionIDs(Sender)))

    @EventDescription
    def OnSend(self, Sender, ConnID, Data, Length):
        print('[%d, OnSend] > %s' % (ConnID, repr(Data)))

    @EventDescription
    def OnReceive(self, Sender, ConnID, Data, Length):
        print('[%d, OnReceive] < %s' % (ConnID, repr(Data)))
        self.Send(Sender=Sender, ConnID=ConnID, Data=Data)
        return HPSocket.EnHandleResult.HR_OK

    def OnClose(self, Sender, ConnID, Operation, ErrorCode):
        (ip, port) = HPSocket.HP_Server_GetRemoteAddress(Sender=Sender, ConnID=ConnID)
        print('[%d, OnClose] > %s opt=%d err=%d' % (ConnID, (ip, port), Operation, ErrorCode))
        return HPSocket.EnHandleResult.HR_OK


if __name__ == '__main__':
    svr = Server()
    if svr.Start(host='0.0.0.0', port=5555):
        print('server started.')
        while True:
            time.sleep(1)
    else:
        print('server fail.')
```

## 2.HPSocket4Python 做了什么：
    为了能让 Python 开发者更好（lan）的使用 HP-Socket 这一高性能高可用的 Socket 框架， HPSocket4Python 对其进行无侵入绑定。
    HPSocket4Python 只是一个中间件，将 Python 的函数调用通过转换进而使用以C++为主要语言的 HP-Socket。
    由于语言的定义差异，Python 很难原汁原味的调用 C++ API，比如 Python 不支持基础类型的参数传址、数据结构（类）隐含了其它一些成员等。
    必须借助 ctypes 模块进行转换。HPSocket4Python 简化了这一系列步骤，力图让开发人员在 3 分钟之内完成基础架构并关注业务逻辑的实现。

## 3.HPSocket4Python 如何实现的：
    HPSocket/HPSocketAPI.py --- 通过自动生成的文件，简单的封装API以及一些类型定义，对应 HPSocket4C.h 文件
    HPSocket/HPTypeDef.py --- 通过自动生成的文件，简单封装类型定义，对应 HPTypeDef.h 文件
    HPSocket/pyhpsocket.py --- 半自动生成的文件，整个体系的高级封装，调用和返回完全使用 Python 的数据结构，可以直接使用而无需掌握 ctypes 的知识
    HPSocket/multiplatforms.py --- 跨平台适应模块，自动检测已知的平台并加载相应的动态库
    HPSocket/Tcp[Pack/Push/Pull].py --- PACK/PUSH/PULL 模型的封装类，开发者可以直接继承然后重写相关的 On_ 族函数以实现业务逻辑

## 4.如何使用 HPSocket4Python：
    可以参考 Demo 目录下的示例，只需要继承你想使用的类，然后实现相应方法成员即可。
    注意，需要在函数定义前添加 EventDescription 函数描述，否则应手动设置 HPSocket.EnHandleResult.HR_XXX 返回值，
    不然可能会出现未定义的行为。
    这一版本的说明文档中暂未添加每条 API 的详细说明，计划在下一个版本推出。

## 5.已知的不足
    · 由于完全使用 Python 实现，可能会有一定的性能损失；
    · 目前只支持 5.1.1 版本的动态库，更高版本的兼容性尚未进行覆盖测试；
    · 高级封装未能支持 HTTP，UDP 的高级封装未编写 DEMO；

## 6.移植/跨平台
    只需要宿主系统安装了 Python3 并且有完整的标准库即可。
    包内提供了部分平台的动态库文件，若这之中不存在目标系统，则开发者需要自行编译 HP-Socket 库。