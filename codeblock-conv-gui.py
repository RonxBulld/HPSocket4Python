#! python3
# coding: utf-8
"""
该程序多处使用硬编码，仅用于转换 HP-Socket v5.1.1 的 HPTypeDef.h 和 HPSocket4C.h 文件，非通用型转换器
发布代码仅为学习交流，避免后期无人维护和拓展，禁止用于商业用途
如需修改代码，须保留所有版权信息
                —— RonxBulld 2017.12.15
"""
import tkinter as tk
import re, sys, traceback

root=tk.Tk()
inputbox = tk.Text(root)
outputbox = tk.Text(root)
header='''# coding: utf-8

####################################
# Converter: codeblock-conv-gui.py #
# Version: 1.4 Developer Edition   #
# Author: Rexfield                 #
# Email: redwoodmax@vip.qq.com     #
####################################

'''

compatibility='''
import ctypes

# 保持兼容性的类型定义
PVOID = ctypes.c_void_p
LPVOID = ctypes.c_void_p
ULONG_PTR = ctypes.POINTER(ctypes.c_ulong)
UINT_PTR = ctypes.POINTER(ctypes.c_uint)
nullptr = PVOID(0)
class WSABUF(ctypes.Structure):
    _fields_ = [
        ('len', ctypes.c_ulong),
        ('buf', ctypes.c_char_p)
    ]
LPWSABUF=ctypes.POINTER(WSABUF)
SOCKET=ctypes.POINTER(ctypes.c_uint)

'''

apiprev='''
from HPTypeDef import *
import multiplatforms
# HPSocketDLL = ctypes.windll.LoadLibrary('HPSocket4C_x64.dll')
HPSocketDLL = multiplatforms.LoadHPSocketLibrary()
CONNID = ctypes.c_ulong
HP_CONNID = ctypes.c_ulong

'''

tbet = {
    'enum':'ctypes.c_int',
    'LPCTSTR':'ctypes.c_char_p',
    'LPCSTR':'ctypes.c_char_p',
    'int':'ctypes.c_int',
    'void':'None',
    'USHORT':'ctypes.c_ushort',
    'BOOL':'ctypes.c_bool',
    'DWORD':'ctypes.c_uint',
    'LPDWORD': 'ctypes.POINTER(ctypes.c_ulong)',
    'TCHAR':'ctypes.c_char',
    'char':'ctypes.c_char',
    'long':'ctypes.c_long',
    'ULONGLONG':'ctypes.c_ulonglong',
    'u_long':'ctypes.c_ulong',
    'BYTE':'ctypes.c_byte',
    '__time_t':'ctypes.c_ulong',
    '__time64_t':'ctypes.c_ulonglong',
    'WCHAR':'ctypes.c_wchar',
    }

lineno=1

def try_conv_type(stype):
    global tbet,lineno
    ss=''
    ptr_times = 0
    if type(stype) is str:
        stype=stype.replace('*', ' * ').replace('[]', ' [] ')
        stype=stype.split(' ')
        stype=[s for s in stype if s != '']
    if type(stype) is list:
        liveenum=False
        if 'enum' in stype:
            liveenum=True
        stype = [ss for ss in stype if ss not in ['const','enum']]
        while stype[-1] == '*' or stype[-1] == '[]':
            stype.pop(-1)
            ptr_times += 1
        ss=' '.join(stype)
        if liveenum:
            ss=ss.replace('En', 'En_HP_')
    if ss in tbet:
        ss = tbet[ss]
    if ptr_times:
        ss = 'ctypes.POINTER(' * ptr_times + ss + ')' * ptr_times
    return ss

mbet={
    'CALLBACK':'__stdcall',
    'MAKEWORD(1, 0)':'1',
    'MAKEWORD(1, 1)':'257',
    'BYTE lpszMask[4]':'int lpszMask'
}
rek='()[]'
regstr=r'%s'%('|'.join(list(mbet.keys())))
for c in rek:
    regstr = regstr.replace(c, '\\'+c)
mbet_re = re.compile(regstr)
def try_macro_replace(src):
    global mbet_re,mbet
    while True:
        result=re.search(mbet_re, src)
        if result == None:
            break
        src = src[:result.span()[0]] + mbet[src[result.span()[0]:result.span()[1]]] + src[result.span()[1]:]
    return src

def enumconv_func(src):
    enum_types = [n for n in re.findall(re.compile(r'}(.*);', re.DOTALL), src)[0].replace('\n', '').replace('\t', '').replace(' ', '').split(',') if '*' not in n]
    enum_names = re.findall(r'typedef\s+enum\s+(\w+)', src)[0]
    # 构造头
    conved = 'class %s():\n' % enum_names
    # 构造文档
    conved += '''    """\n%s\n    """\n''' % ''.join([' ' * 4 + line for line in src.splitlines(keepends=True)])
    # 构造枚举量
    enums = re.findall(r'(\w+)\s*\=\s*([xX0-9]+)\,?\s*(\/\/(.*))?', src)
    iterlenmax = max([len(e[0]) for e in enums])
    conved += '\n'.join([' ' * 4 + e[0] + ' ' * (iterlenmax - len(e[0]) + 1) + '= %-3s # %s' % (e[1], e[2]) for e in enums]) + '\n'
    for entn in enum_types:
        conved += '%s = ctypes.c_int\n'%entn
    return conved

def enumconv():
    global inputbox, outputbox
    src=inputbox.get(0.0, tk.END)

    conved = globals()[sys._getframe().f_code.co_name+'_func'](src)

    outputbox.delete(0.0, tk.END)
    outputbox.insert(tk.END, conved + '\n')

def ltype_anay(ltype):
    rere=re.findall(r'\s*(\*)?\s*(\w+)', ltype)
    # print(ltype,rere)
    result=rere[0]
    type_name = result[1]
    is_ptr = result[0]=='*'
    return (type_name, is_ptr)

def structconv_func(src):
    struct_type = re.findall(r'\s*typedef\s+struct\s+(\w+)', src)[0]
    struct_names = [n for n in re.findall(re.compile(r'}(.*);', re.DOTALL), src)[0].replace('\n', '').replace('\t', '').replace(' ', '').split(',')]
    # 构造头
    conved = 'class %s(ctypes.Structure):\n' % struct_type
    # 构造文档
    conved += '''    """\n%s\n    """\n''' % ''.join([' ' * 4 + line for line in src.splitlines(keepends=True)])
    # 构造成员
    conved += '    _fields_=[\n'
    members = re.findall(r'([^\n]*);', re.findall(r'\{([^}]*)\}', src)[0])
    members = [[tm for tm in m.replace('\t', ' ').split(' ') if tm != ''] for m in members]
    for me in members:
        conved += "        ('%s', %s),\n" % (me[-1], try_conv_type(me[:-1]))
    conved += '    ]'
    # 继承复用
    for name in struct_names:
        (name, is_ptr) = ltype_anay(name)
        conved += '\n%s = %s' % (name, struct_type if is_ptr == False else 'ctypes.POINTER(%s)'%struct_type)
    return conved

def structconv():
    global inputbox, outputbox
    src = inputbox.get(0.0, tk.END)

    conved = globals()[sys._getframe().f_code.co_name+'_func'](src)

    outputbox.delete(0.0, tk.END)
    outputbox.insert(tk.END, conved + '\n')

def typedefconv_func(src):
    line=src.replace('\t',' ')
    rtype,ltypel = re.findall(r'typedef\s+(?:const)?\s*(\w+)\s*([A-Za-z_\s,*]+);', line)[0]
    rtype=try_conv_type(rtype)
    ltypes=re.split(r'\s*,\s*', ltypel)
    conved = '# %s\n'%line
    for ltype in ltypes:
        (ltype,is_ptr)=ltype_anay(ltype)
        conved += '%s = %s\n' % (ltype, rtype if is_ptr == False else 'ctypes.POINTER(%s)'%rtype)
    return conved

def typedefconv():
    global inputbox, outputbox
    src = inputbox.get(0.0, tk.END)
    conved = ''
    for line in src.splitlines():
        if len(line)>0:
            conved += globals()[sys._getframe().f_code.co_name+'_func'](line)
        else:
            conved += '\n'

    outputbox.delete(0.0, tk.END)
    outputbox.insert(tk.END, conved + '\n')

def commentconv_func(src):
    blockcoms = re.findall(r'\/\*(.*?)\*\/', src, re.DOTALL)
    conved = ''
    for blockcom in blockcoms:
        conved += '# %s\n'%(blockcom.replace('\n', '\n# '))
    return conved
        
def commentconv():
    global inputbox, outputbox
    src = inputbox.get(0.0, tk.END)
    conved = globals()[sys._getframe().f_code.co_name+'_func'](src)
    
    outputbox.delete(0.0, tk.END)
    outputbox.insert(tk.END, conved + '\n')

def proc_args(argstr):
    args = re.split(r'\s*,\s*', argstr)
    argstype = []
    args = [a for a in args if a!='']
    for arg in args:
        argitems = re.findall(r'(\w+|\*|\[\])', arg)
        nindex = -1 if argitems[-1]!='[]' else -2
        argname = argitems.pop(nindex)
        argtype = try_conv_type(argitems)
        argstype.append(argtype)
    return argstype

def callbackdefconv_func(src):
    # 构造文档
    conved = '# %s\n' % src
    result=re.findall(r'typedef[\s]+([A-Za-z_]+)[\s]+\(__stdcall[\s]+\*([A-Za-z_]+)\)[\s]*\((.*)\);', src)[0]
    rettype,name = result[0:2]
    # 构造头
    conved += '%s = ctypes.CFUNCTYPE(%s, ' % (name, rettype)
    # 构造参数
    argstype = proc_args(result[2])
    conved += ', '.join(argstype) + ')\n'
    return conved

def callbackdefconv():
    global inputbox, outputbox
    src = inputbox.get(0.0, tk.END)
    conved = ''

    for line in src.splitlines():
        conved += globals()[sys._getframe().f_code.co_name+'_func'](line)
        
    outputbox.delete(0.0, tk.END)
    outputbox.insert(tk.END, conved + '\n')

def apidefconv_func(src):
    # 构造文档
    src=src.replace('\t',' ')
    rettype,name,argstr=re.findall(r'HPSOCKET_API\s+(\w+)\s+__stdcall (\w+)\((.*)\)',src)[0]
    # 构造参数
    argstype = proc_args(argstr)
    conved = '# %s' % src
    conved += '''
if hasattr(HPSocketDLL, "{name}"):
    {name} = HPSocketDLL.{name}
    {name}.restype = {restype}
    {name}.argtypes = [{args}]

'''.format(**{'name':name, 'restype':try_conv_type(rettype), 'args':', '.join(argstype)})
    # conved += '%s = HPSocketDLL.%s if hasattr(HPSocketDLL, "%s") else None\n'%(name,name,name)
    # conved += 'if %s:\n' % name
    # conved += '    %s.restype = %s\n'%(name, try_conv_type(rettype))
    # conved += '    %s.argtypes = [%s]\n'%(name, ', '.join(argstype))
    return conved

def apidefconv():
    global inputbox, outputbox
    src = inputbox.get(0.0, tk.END)
    conved = ''
    for line in src.splitlines():
        if line[0:2] == '//':
            line = line.replace('//', '# ')
            conved += line + '\n'
        elif line[0:len('HPSOCKET_API')] == 'HPSOCKET_API':
            conved += globals()[sys._getframe().f_code.co_name+'_func'](line)
        elif len(line) == 0:
            conved += '\n'
        else:
            raise Exception('不可预知的行代码')
    outputbox.delete(0.0, tk.END)
    outputbox.insert(tk.END, conved + '\n')


realline=''
def get_next_line(lines):
    global realline, lineno
    realline = lines.pop(0)
    lineno += 1
    return try_macro_replace(realline)

def autoconv():
    global inputbox, outputbox, realline, lineno, header
    src = inputbox.get(0.0, tk.END)
    conved = ''
    lines = src.splitlines()
    line=''
    hadapi=False
    while len(lines)>0:
        try:
            line=get_next_line(lines)
            if len(line) == 0:
                conved += '\n'
            elif line[0:2] == '/*':
                colline = line
                while '*/' not in line:
                    line = get_next_line(lines)
                    colline += '\n' + line
                conved += commentconv_func(colline)
            elif line[0:2] == '//':
                conved += '# ' + line[2:] +'\n'
            elif line[0:len('HPSOCKET_API')] == 'HPSOCKET_API':
                line =  re.subn(r'\/\*.*?\*\/',' ', line)[0]
                hadapi=True
                conved += apidefconv_func(line)
            elif line[0:len('typedef')] == 'typedef':
                if re.match(r'^typedef\s+\w+\s*\(\s*__stdcall\s*\*', line):
                    conved += callbackdefconv_func(line)
                elif re.match(r'typedef\s+enum\s+(\w+)', line):
                    colline = line
                    while ';' not in line:
                        line = get_next_line(lines)
                        colline += '\n'+line
                    conved += enumconv_func(colline)
                elif re.match(r'typedef\s+struct\s+(\w+)', line):
                    colline = line
                    bracket_found = False
                    semicolon_found = False
                    if re.match(r'\}[^;]*;', line) != None:
                        bracket_found = True
                        semicolon_found = True
                    while not (bracket_found and semicolon_found):
                        line = get_next_line(lines)
                        colline += '\n'+line
                        if '}' in line:
                            bracket_found = True
                        if ';' in line and bracket_found == True:
                            semicolon_found = True
                    conved += structconv_func(colline)
                elif re.match(r'typedef\s+\w+\s+\w+', line):
                    conved += typedefconv_func(line)
                else:
                    raise Exception('Typedef 的目的不明确')
            elif line[0] == '#':
                conved += '\n'
        except Exception as e:
            traceback.print_exc()
            print("引起错误的内容：[%d]%s"%(lineno,realline))
            break

    if hadapi:
        conved = apiprev + conved
    else:
        conved = compatibility + conved
    outputbox.delete(0.0, tk.END)
    outputbox.insert(tk.END, header + conved)


benumconv = tk.Button(master=root, text="Enum转换", command=enumconv)
bstructconv = tk.Button(master=root, text="Struct转换", command=structconv)
btypedefconv = tk.Button(master=root, text="Typedef转换", command=typedefconv)
bcommentconv = tk.Button(master=root, text="注释转换", command=commentconv)
bcallbackdefconv = tk.Button(master=root, text="回调定义转换", command=callbackdefconv)
bapidefconv = tk.Button(master=root, text="API定义转换", command=apidefconv)
bautoconv = tk.Button(master=root, text='自动转换', command=autoconv)


inputbox.pack()
outputbox.pack()

benumconv.pack(side=tk.LEFT,expand=tk.YES,fill=tk.Y)
bstructconv.pack(side=tk.LEFT,expand=tk.YES,fill=tk.Y)
btypedefconv.pack(side=tk.LEFT,expand=tk.YES,fill=tk.Y)
bcommentconv.pack(side=tk.LEFT,expand=tk.YES,fill=tk.Y)
bcallbackdefconv.pack(side=tk.LEFT,expand=tk.YES,fill=tk.Y)
bapidefconv.pack(side=tk.LEFT,expand=tk.YES,fill=tk.Y)
bautoconv.pack(side=tk.LEFT,expand=tk.YES,fill=tk.Y)


root.mainloop()
