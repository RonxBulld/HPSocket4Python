# coding: utf-8
'''平台适配模块
    模块根据宿主系统平台自动配置库文件（DLL/SO）以及调用约定（STDCALL/CDECL）
'''
import platform
import ctypes


def script_path():
    '''获取当前脚本文件所在的路径，文件应该和库文件放置在同一目录'''
    import inspect, os
    this_file = inspect.getfile(inspect.currentframe())
    return os.path.abspath(os.path.dirname(this_file))


dist_dict = {
    ('Windows', 'AMD64', '64bit'): (script_path()+'/HPSocket4C_amd64_x64.dll',     'windll'),
    ('Linux', 'AMD64', '64bit'):   (script_path()+'/libhpsocket4c_amd64_x64.so',   'cdll'),
    ('Linux', 'aarch64', '64bit'): (script_path()+'/libhpsocket4c_aarch64_x64.so', 'cdll')
}


# 模块识别 Windows 系统和 Linux 系统
ostype = platform.system()
if ostype == 'Windows':
    pass
elif ostype == 'Linux':
    pass
else:
    raise Exception('Unknow operating system. - ' + ostype)

# 模块识别 32bit 和 64bit
bits = platform.architecture()[0]
if bits == '32bit':
    pass
elif bits == '64bit':
    pass
else:
    raise Exception('Unknow data bits. - ' + bits)

# 模块识别 x86/amd64/aarch64
machine = platform.machine()
if machine == 'x86':
    pass
elif machine == 'AMD64':
    pass
elif machine == 'aarch64':
    pass
else:
    raise Exception('Unsupport machine paltform. - ' + machine)

dist = (ostype, machine, bits)
config = dist_dict[dist]

def LoadHPSocketLibrary():
    '''模块自动识别平台类型，然后加载相应的库，返回库把柄'''
    global config
    dllhandler = getattr(ctypes, config[1]).LoadLibrary(config[0])
    return dllhandler
