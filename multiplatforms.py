# coding: utf-8
'''平台适配模块'''
import platform
import ctypes
import os

dist_dict = {
    ('Windows', '64bit'):(os.getcwd()+'/HPSocket4C_x64.dll',   'windll'),
    ('Windows', '32bit'):(os.getcwd()+'/HPSocket4C_x86.dll',   'windll'),
    ('Linux', '64bit'):  (os.getcwd()+'/libhpsocket4c_x64.so', 'cdll'),
    ('Linux', '32bit'):  (os.getcwd()+'/libhpsocket4c_x86.so', 'cdll'),
}

ostype = platform.system()

if ostype == 'Windows':
    pass
elif ostype == 'Linux':
    pass
else:
    raise Exception('Unknow operating system. - ' + ostype)

bits = platform.architecture()[0]
if bits == '32bit':
    pass
elif bits == '64bit':
    pass
else:
    raise Exception('Unknow data bits. - ' + bits)

dist = (ostype, bits)
config = dist_dict[dist]

def LoadHPSocketLibrary():
    '''模块自动识别平台类型，然后加载相应的库，返回库把柄'''
    global config
    dllhandler = getattr(ctypes, config[1]).LoadLibrary(config[0])
    return dllhandler