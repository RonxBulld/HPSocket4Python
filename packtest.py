# coding: utf-8
'''PACK模型测试'''
import ctypes,time
import pyhpsocket as hp

def OnSend(Sender, ConnID, pData, Len):
    print('Send',Len,'Bytes.')
    return hp.EnHandleResult.HR_OK

L=hp.Create_HP_TcpPackClientListener()
C=hp.Create_HP_TcpPackClient(L)

hp.HP_Set_FN_Client_OnSend(L, hp.HP_FN_Client_OnSend(OnSend))

hp.HP_TcpPackClient_SetMaxPackSize(C,ctypes.c_uint(0x01FFF))
hp.HP_TcpPackClient_SetPackHeaderFlag(C,ctypes.c_ushort(0x169))
target_ip=ctypes.create_string_buffer(str.encode('127.0.0.1'))
hp.HP_Client_Start(C,target_ip,ctypes.c_ushort(5555),ctypes.c_bool(False))

Bufs=['text to be sent']
count=len(Bufs)
WSABUFs = (hp.WSABUF * len(Bufs))()
for n in range(count):
    Buf = Bufs[n]
    WSABUFs[n].len = ctypes.c_uint(len(Buf))
    WSABUFs[n].buf = ctypes.cast(ctypes.pointer(ctypes.create_string_buffer(str.encode(Buf))),ctypes.c_char_p)
    # print(bytes(WSABUFs[n]))

suc=hp._HP_Client_SendPackets(C, WSABUFs, ctypes.c_int(count))
time.sleep(10)
print(suc)
hp.HP_Client_Stop(C)
hp.Destroy_HP_TcpPackClientListener(L)
hp.Destroy_HP_TcpPackClient(C)