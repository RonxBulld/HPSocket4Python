# HPSocket4Python
这个是 HPSocket 的 Python 绑定，力图在 Python 上更方便的使用 HPSocket 组件。目前已经可以通过继承类的方式来使用 Tcp_Pull_Server。
代码形如：
```
class Server(TcpPull.HP_TcpPullServer):
    @TcpPull.HP_TcpPullServer.EventDescription
    def OnAccept(self, Sender, ConnID, Client):
        # ::HP_Server_SetConnectionExtra(pSender, dwConnID, new TPkgInfo(true, sizeof(TPkgHeader)))
        self.pkg = TPkgInfo(True, TcpPull.SizeOf(TPkgHeader))
        TcpPull.HP_Server_SetConnectionExtra(Sender, ConnID, TcpPull.MakePointer(self.pkg))
        return TcpPull.EnHandleResult.HR_OK

    @TcpPull.HP_TcpPullServer.EventDescription
    def OnReceive(self, Sender, ConnID, Length):
        print('[--', sys._getframe().f_code.co_name, '--]', end='\t')
        print('Receive data from client:', ConnID)
        # 本 Demo 和其它的 TestEcho-Pull 一样，数据包的组织形式是 Head-Body 交错
        pInfo = FindPkgInfo(Sender, ConnID)
        if pInfo:
            required = pInfo.length
            remain = Length
            while remain >= required:
                remain -= required
                # Buffer = ctypes.create_string_buffer(b' ' * required)
                # buffer = ctypes.cast(Buffer, ctypes.POINTER(ctypes.c_byte))     # 从 char[] 转换到需要的 byte*
                Buf = CBuffer(required)
                result = TcpPull.HP_TcpPullServer_Fetch(Sender, ConnID, Buf.Ptr(), required)  # 这里获取 Body
                if result == TcpPull.EnFetchResult.FR_OK:
                    if pInfo.is_header:
                        pHeader = Buf.ToOtherPtr(TPkgHeader)
                        print('[TRACR] [Server] head -> seq: %d, body_len: %d' % (pHeader.contents.seq, pHeader.contents.body_len))
                        required = pHeader.contents.body_len    # 从 head 切换到 body
                    else:
                        pBody = Buf.ToOtherPtr(TPkgBody)        # pBody = (TPkgBody*)buffer
                        # 下面的转换需要小心，因为如果使用错误的字符集会导致crash
                        name = pBody.contents.name.decode('GBK')               # name = bytes.decode(pBody->name, 'GBK')
                        # 这里由于 python 语言的限制，没有 C 那么灵活所以 desc 部分单独拿出来处理
                        # 下面的转换需要小心，因为如果使用错误的字符集会导致crash
                        desc = Buf[TcpPull.SizeOf(TPkgBody):].decode('GBK')
                        print('[TRACE] body -> name: %s, age: %d, desc: %s' % (name, pBody.contents.age, desc))
                        required = TcpPull.SizeOf(TPkgHeader)    # 从 body 切换到 head
                    pInfo.is_header = not pInfo.is_header
                    pInfo.length = required
                    if not TcpPull.HP_Server_Send(Sender, ConnID, Buf.Ptr()):
                        return TcpPull.EnHandleResult.HR_ERROR

svr = Server()
svr.Start('0.0.0.0',5555)
```