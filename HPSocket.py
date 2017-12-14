# coding: utf-8

####################################
# Converter: codeblock-conv-gui.py #
# Version: 1.2 Developer Edition   #
# Author: Rexfield                 #
####################################


from HPTypeDef import *
import multiplatforms
# HPSocketDLL = ctypes.windll.LoadLibrary('HPSocket4C_x64.dll')
HPSocketDLL = multiplatforms.LoadHPSocketLibrary()
CONNID = ctypes.c_ulong
HP_CONNID = ctypes.c_ulong

#
#  * Copyright: JessMA Open Source (ldcsaa@gmail.com)
#  *
#  * Author	: Bruce Liang
#  * Website	: http://www.jessma.org
#  * Project	: https://github.com/ldcsaa
#  * Blog		: http://www.cnblogs.com/ldcsaa
#  * Wiki		: http://www.oschina.net/p/hp-socket
#  * QQ Group	: 75375912, 44636872
#  *
#  * Licensed under the Apache License, Version 2.0 (the "License");
#  * you may not use this file except in compliance with the License.
#  * You may obtain a copy of the License at
#  *
#  *      http://www.apache.org/licenses/LICENSE-2.0
#  *
#  * Unless required by applicable law or agreed to in writing, software
#  * distributed under the License is distributed on an "AS IS" BASIS,
#  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  * See the License for the specific language governing permissions and
#  * limitations under the License.
#

# *****************************************************************************
# Module:  HPSocket for C
#
# Desc: 导出纯 C 函数，让其它语言（如：C / C# / Delphi 等）能方便地使用 HPSocket
#
# Usage:
# 		方法一：
# 		--------------------------------------------------------------------------------------
# 		0. （C/C++ 程序）包含 HPTypeDef.h / HPSocket4C.h 头文件
# 		1. 调用 ::Create_HP_XxxListener() 函数创建监听器对象
# 		2. 调用 ::Create_HP_Xxx(pListener) 函数创建 HPSocket 对象
# 		3. 调用 ::HP_Set_FN_Xxx_OnYyy(pListener, ...) 函数设置监听器的回调函数
# 		4. 调用相关导出函数操作 HPSocket 对象
# 		5. ...... ......
# 		6. 调用 ::Destroy_HP_Xxx(pSocket) 函数销毁 HPSocket 对象
# 		7. 调用 ::Destroy_HP_XxxListener(pListener) 函数销毁监听器对象
#
# 		方法二：
# 		--------------------------------------------------------------------------------------
# 		1. 应用程序把需要用到的导出函数封装到特定语言的包装类中
# 		2. 通过包装类封装后，以面向对象的方式使用 HPSocket
#
# Release:
# 		<-- 动态链接库 -->
# 		1. x86/HPSocket4C.dll			- (32位/MBCS/Release)
# 		2. x86/HPSocket4C_D.dll			- (32位/MBCS/DeBug)
# 		3. x86/HPSocket4C_U.dll			- (32位/UNICODE/Release)
# 		4. x86/HPSocket4C_UD.dll		- (32位/UNICODE/DeBug)
# 		5. x64/HPSocket4C.dll			- (64位/MBCS/Release)
# 		6. x64/HPSocket4C_D.dll			- (64位/MBCS/DeBug)
# 		7. x64/HPSocket4C_U.dll			- (64位/UNICODE/Release)
# 		8. x64/HPSocket4C_UD.dll		- (64位/UNICODE/DeBug)
#
# 		<-- 静态链接库 -->
# 		!!注意!!：使用 HPSocket 静态库时，需要在工程属性中定义预处理宏 -> HPSOCKET_STATIC_LIB
# 		1. x86/static/HPSocket4C.lib	- (32位/MBCS/Release)
# 		2. x86/static/HPSocket4C_D.lib	- (32位/MBCS/DeBug)
# 		3. x86/static/HPSocket4C_U.lib	- (32位/UNICODE/Release)
# 		4. x86/static/HPSocket4C_UD.lib	- (32位/UNICODE/DeBug)
# 		5. x64/static/HPSocket4C.lib	- (64位/MBCS/Release)
# 		6. x64/static/HPSocket4C_D.lib	- (64位/MBCS/DeBug)
# 		7. x64/static/HPSocket4C_U.lib	- (64位/UNICODE/Release)
# 		8. x64/static/HPSocket4C_UD.lib	- (64位/UNICODE/DeBug)
#
# *****************************************************************************







# ************************************************
# ********* imports / exports HPSocket4C *********





# ***********************************************************************
# 名称：定义 Socket 对象指针类型别名
# 描述：把 Socket 对象指针定义为更直观的别名
# ***********************************************************************

# typedef PVOID  HP_Object;
HP_Object = PVOID

# typedef HP_Object HP_Server;
HP_Server = HP_Object
# typedef HP_Object HP_Agent;
HP_Agent = HP_Object
# typedef HP_Object HP_Client;
HP_Client = HP_Object
# typedef HP_Object HP_TcpServer;
HP_TcpServer = HP_Object
# typedef HP_Object HP_TcpAgent;
HP_TcpAgent = HP_Object
# typedef HP_Object HP_TcpClient;
HP_TcpClient = HP_Object
# typedef HP_Object HP_PullSocket;
HP_PullSocket = HP_Object
# typedef HP_Object HP_PullClient;
HP_PullClient = HP_Object
# typedef HP_Object HP_TcpPullServer;
HP_TcpPullServer = HP_Object
# typedef HP_Object HP_TcpPullAgent;
HP_TcpPullAgent = HP_Object
# typedef HP_Object HP_TcpPullClient;
HP_TcpPullClient = HP_Object
# typedef HP_Object HP_PackSocket;
HP_PackSocket = HP_Object
# typedef HP_Object HP_PackClient;
HP_PackClient = HP_Object
# typedef HP_Object HP_TcpPackServer;
HP_TcpPackServer = HP_Object
# typedef HP_Object HP_TcpPackAgent;
HP_TcpPackAgent = HP_Object
# typedef HP_Object HP_TcpPackClient;
HP_TcpPackClient = HP_Object
# typedef HP_Object HP_UdpServer;
HP_UdpServer = HP_Object
# typedef HP_Object HP_UdpClient;
HP_UdpClient = HP_Object
# typedef HP_Object HP_UdpCast;
HP_UdpCast = HP_Object

# typedef HP_Object HP_Listener;
HP_Listener = HP_Object
# typedef HP_Object HP_ServerListener;
HP_ServerListener = HP_Object
# typedef HP_Object HP_AgentListener;
HP_AgentListener = HP_Object
# typedef HP_Object HP_ClientListener;
HP_ClientListener = HP_Object
# typedef HP_Object HP_TcpServerListener;
HP_TcpServerListener = HP_Object
# typedef HP_Object HP_TcpAgentListener;
HP_TcpAgentListener = HP_Object
# typedef HP_Object HP_TcpClientListener;
HP_TcpClientListener = HP_Object
# typedef HP_Object HP_PullSocketListener;
HP_PullSocketListener = HP_Object
# typedef HP_Object HP_PullClientListener;
HP_PullClientListener = HP_Object
# typedef HP_Object HP_TcpPullServerListener;
HP_TcpPullServerListener = HP_Object
# typedef HP_Object HP_TcpPullAgentListener;
HP_TcpPullAgentListener = HP_Object
# typedef HP_Object HP_TcpPullClientListener;
HP_TcpPullClientListener = HP_Object
# typedef HP_Object HP_PackSocketListener;
HP_PackSocketListener = HP_Object
# typedef HP_Object HP_PackClientListener;
HP_PackClientListener = HP_Object
# typedef HP_Object HP_TcpPackServerListener;
HP_TcpPackServerListener = HP_Object
# typedef HP_Object HP_TcpPackAgentListener;
HP_TcpPackAgentListener = HP_Object
# typedef HP_Object HP_TcpPackClientListener;
HP_TcpPackClientListener = HP_Object
# typedef HP_Object HP_UdpServerListener;
HP_UdpServerListener = HP_Object
# typedef HP_Object HP_UdpClientListener;
HP_UdpClientListener = HP_Object
# typedef HP_Object HP_UdpCastListener;
HP_UdpCastListener = HP_Object

# typedef HP_Object HP_Http;
HP_Http = HP_Object
# typedef HP_Object HP_HttpServer;
HP_HttpServer = HP_Object
# typedef HP_Object HP_HttpAgent;
HP_HttpAgent = HP_Object
# typedef HP_Object HP_HttpClient;
HP_HttpClient = HP_Object
# typedef HP_Object HP_HttpSyncClient;
HP_HttpSyncClient = HP_Object

# typedef HP_Object HP_HttpServerListener;
HP_HttpServerListener = HP_Object
# typedef HP_Object HP_HttpAgentListener;
HP_HttpAgentListener = HP_Object
# typedef HP_Object HP_HttpClientListener;
HP_HttpClientListener = HP_Object

# ***************************************************************************************************************************************************
# ***************************************************************** TCP/UDP Exports *****************************************************************
# ***************************************************************************************************************************************************

# **************************************************
# **************** TCP/UDP 回调函数 *****************

#  Server 回调函数
# typedef En_HP_HandleResult (__stdcall *HP_FN_Server_OnPrepareListen)	(HP_Server pSender, UINT_PTR soListen);
HP_FN_Server_OnPrepareListen = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Server, UINT_PTR)
#  如果为 TCP 连接，pClient为 SOCKET 句柄；如果为 UDP 连接，pClient为 SOCKADDR 指针；
# typedef En_HP_HandleResult (__stdcall *HP_FN_Server_OnAccept)			(HP_Server pSender, HP_CONNID dwConnID, UINT_PTR pClient);
HP_FN_Server_OnAccept = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Server, HP_CONNID, UINT_PTR)
# typedef En_HP_HandleResult (__stdcall *HP_FN_Server_OnHandShake)		(HP_Server pSender, HP_CONNID dwConnID);
HP_FN_Server_OnHandShake = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Server, HP_CONNID)
# typedef En_HP_HandleResult (__stdcall *HP_FN_Server_OnSend)				(HP_Server pSender, HP_CONNID dwConnID, const BYTE* pData, int iLength);
HP_FN_Server_OnSend = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Server, HP_CONNID, ctypes.POINTER(ctypes.c_byte), ctypes.c_int)
# typedef En_HP_HandleResult (__stdcall *HP_FN_Server_OnReceive)			(HP_Server pSender, HP_CONNID dwConnID, const BYTE* pData, int iLength);
HP_FN_Server_OnReceive = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Server, HP_CONNID, ctypes.POINTER(ctypes.c_byte), ctypes.c_int)
# typedef En_HP_HandleResult (__stdcall *HP_FN_Server_OnPullReceive)		(HP_Server pSender, HP_CONNID dwConnID, int iLength);
HP_FN_Server_OnPullReceive = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Server, HP_CONNID, ctypes.c_int)
# typedef En_HP_HandleResult (__stdcall *HP_FN_Server_OnClose)			(HP_Server pSender, HP_CONNID dwConnID, En_HP_SocketOperation enOperation, int iErrorCode);
HP_FN_Server_OnClose = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Server, HP_CONNID, En_HP_SocketOperation, ctypes.c_int)
# typedef En_HP_HandleResult (__stdcall *HP_FN_Server_OnShutdown)			(HP_Server pSender);
HP_FN_Server_OnShutdown = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Server)

#  Agent 回调函数
# typedef En_HP_HandleResult (__stdcall *HP_FN_Agent_OnPrepareConnect)	(HP_Agent pSender, HP_CONNID dwConnID, UINT_PTR socket);
HP_FN_Agent_OnPrepareConnect = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Agent, HP_CONNID, UINT_PTR)
# typedef En_HP_HandleResult (__stdcall *HP_FN_Agent_OnConnect)			(HP_Agent pSender, HP_CONNID dwConnID);
HP_FN_Agent_OnConnect = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Agent, HP_CONNID)
# typedef En_HP_HandleResult (__stdcall *HP_FN_Agent_OnHandShake)			(HP_Agent pSender, HP_CONNID dwConnID);
HP_FN_Agent_OnHandShake = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Agent, HP_CONNID)
# typedef En_HP_HandleResult (__stdcall *HP_FN_Agent_OnSend)				(HP_Agent pSender, HP_CONNID dwConnID, const BYTE* pData, int iLength);
HP_FN_Agent_OnSend = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Agent, HP_CONNID, ctypes.POINTER(ctypes.c_byte), ctypes.c_int)
# typedef En_HP_HandleResult (__stdcall *HP_FN_Agent_OnReceive)			(HP_Agent pSender, HP_CONNID dwConnID, const BYTE* pData, int iLength);
HP_FN_Agent_OnReceive = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Agent, HP_CONNID, ctypes.POINTER(ctypes.c_byte), ctypes.c_int)
# typedef En_HP_HandleResult (__stdcall *HP_FN_Agent_OnPullReceive)		(HP_Agent pSender, HP_CONNID dwConnID, int iLength);
HP_FN_Agent_OnPullReceive = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Agent, HP_CONNID, ctypes.c_int)
# typedef En_HP_HandleResult (__stdcall *HP_FN_Agent_OnClose)				(HP_Agent pSender, HP_CONNID dwConnID, En_HP_SocketOperation enOperation, int iErrorCode);
HP_FN_Agent_OnClose = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Agent, HP_CONNID, En_HP_SocketOperation, ctypes.c_int)
# typedef En_HP_HandleResult (__stdcall *HP_FN_Agent_OnShutdown)			(HP_Agent pSender);
HP_FN_Agent_OnShutdown = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Agent)

#  Client 回调函数
# typedef En_HP_HandleResult (__stdcall *HP_FN_Client_OnPrepareConnect)	(HP_Client pSender, HP_CONNID dwConnID, UINT_PTR socket);
HP_FN_Client_OnPrepareConnect = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Client, HP_CONNID, UINT_PTR)
# typedef En_HP_HandleResult (__stdcall *HP_FN_Client_OnConnect)			(HP_Client pSender, HP_CONNID dwConnID);
HP_FN_Client_OnConnect = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Client, HP_CONNID)
# typedef En_HP_HandleResult (__stdcall *HP_FN_Client_OnHandShake)		(HP_Client pSender, HP_CONNID dwConnID);
HP_FN_Client_OnHandShake = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Client, HP_CONNID)
# typedef En_HP_HandleResult (__stdcall *HP_FN_Client_OnSend)				(HP_Client pSender, HP_CONNID dwConnID, const BYTE* pData, int iLength);
HP_FN_Client_OnSend = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Client, HP_CONNID, ctypes.POINTER(ctypes.c_byte), ctypes.c_int)
# typedef En_HP_HandleResult (__stdcall *HP_FN_Client_OnReceive)			(HP_Client pSender, HP_CONNID dwConnID, const BYTE* pData, int iLength);
HP_FN_Client_OnReceive = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Client, HP_CONNID, ctypes.POINTER(ctypes.c_byte), ctypes.c_int)
# typedef En_HP_HandleResult (__stdcall *HP_FN_Client_OnPullReceive)		(HP_Client pSender, HP_CONNID dwConnID, int iLength);
HP_FN_Client_OnPullReceive = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Client, HP_CONNID, ctypes.c_int)
# typedef En_HP_HandleResult (__stdcall *HP_FN_Client_OnClose)			(HP_Client pSender, HP_CONNID dwConnID, En_HP_SocketOperation enOperation, int iErrorCode);
HP_FN_Client_OnClose = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Client, HP_CONNID, En_HP_SocketOperation, ctypes.c_int)

# **************************************************
# ************** TCP/UDP 对象创建函数 ***************

#  创建 HP_TcpServer 对象
# HPSOCKET_API HP_TcpServer __stdcall Create_HP_TcpServer(HP_TcpServerListener pListener);
Create_HP_TcpServer = HPSocketDLL.Create_HP_TcpServer if hasattr(HPSocketDLL, "Create_HP_TcpServer") else None
if Create_HP_TcpServer:
    Create_HP_TcpServer.restype = HP_TcpServer
    Create_HP_TcpServer.argtypes = [HP_TcpServerListener]
#  创建 HP_TcpAgent 对象
# HPSOCKET_API HP_TcpAgent __stdcall Create_HP_TcpAgent(HP_TcpAgentListener pListener);
Create_HP_TcpAgent = HPSocketDLL.Create_HP_TcpAgent if hasattr(HPSocketDLL, "Create_HP_TcpAgent") else None
if Create_HP_TcpAgent:
    Create_HP_TcpAgent.restype = HP_TcpAgent
    Create_HP_TcpAgent.argtypes = [HP_TcpAgentListener]
#  创建 HP_TcpClient 对象
# HPSOCKET_API HP_TcpClient __stdcall Create_HP_TcpClient(HP_TcpClientListener pListener);
Create_HP_TcpClient = HPSocketDLL.Create_HP_TcpClient if hasattr(HPSocketDLL, "Create_HP_TcpClient") else None
if Create_HP_TcpClient:
    Create_HP_TcpClient.restype = HP_TcpClient
    Create_HP_TcpClient.argtypes = [HP_TcpClientListener]
#  创建 HP_TcpPullServer 对象
# HPSOCKET_API HP_TcpPullServer __stdcall Create_HP_TcpPullServer(HP_TcpPullServerListener pListener);
Create_HP_TcpPullServer = HPSocketDLL.Create_HP_TcpPullServer if hasattr(HPSocketDLL, "Create_HP_TcpPullServer") else None
if Create_HP_TcpPullServer:
    Create_HP_TcpPullServer.restype = HP_TcpPullServer
    Create_HP_TcpPullServer.argtypes = [HP_TcpPullServerListener]
#  创建 HP_TcpPullAgent 对象
# HPSOCKET_API HP_TcpPullAgent __stdcall Create_HP_TcpPullAgent(HP_TcpPullAgentListener pListener);
Create_HP_TcpPullAgent = HPSocketDLL.Create_HP_TcpPullAgent if hasattr(HPSocketDLL, "Create_HP_TcpPullAgent") else None
if Create_HP_TcpPullAgent:
    Create_HP_TcpPullAgent.restype = HP_TcpPullAgent
    Create_HP_TcpPullAgent.argtypes = [HP_TcpPullAgentListener]
#  创建 HP_TcpPullClient 对象
# HPSOCKET_API HP_TcpPullClient __stdcall Create_HP_TcpPullClient(HP_TcpPullClientListener pListener);
Create_HP_TcpPullClient = HPSocketDLL.Create_HP_TcpPullClient if hasattr(HPSocketDLL, "Create_HP_TcpPullClient") else None
if Create_HP_TcpPullClient:
    Create_HP_TcpPullClient.restype = HP_TcpPullClient
    Create_HP_TcpPullClient.argtypes = [HP_TcpPullClientListener]
#  创建 HP_TcpPackServer 对象
# HPSOCKET_API HP_TcpPackServer __stdcall Create_HP_TcpPackServer(HP_TcpServerListener pListener);
Create_HP_TcpPackServer = HPSocketDLL.Create_HP_TcpPackServer if hasattr(HPSocketDLL, "Create_HP_TcpPackServer") else None
if Create_HP_TcpPackServer:
    Create_HP_TcpPackServer.restype = HP_TcpPackServer
    Create_HP_TcpPackServer.argtypes = [HP_TcpServerListener]
#  创建 HP_TcpPackAgent 对象
# HPSOCKET_API HP_TcpPackAgent __stdcall Create_HP_TcpPackAgent(HP_TcpAgentListener pListener);
Create_HP_TcpPackAgent = HPSocketDLL.Create_HP_TcpPackAgent if hasattr(HPSocketDLL, "Create_HP_TcpPackAgent") else None
if Create_HP_TcpPackAgent:
    Create_HP_TcpPackAgent.restype = HP_TcpPackAgent
    Create_HP_TcpPackAgent.argtypes = [HP_TcpAgentListener]
#  创建 HP_TcpPackClient 对象
# HPSOCKET_API HP_TcpPackClient __stdcall Create_HP_TcpPackClient(HP_TcpClientListener pListener);
Create_HP_TcpPackClient = HPSocketDLL.Create_HP_TcpPackClient if hasattr(HPSocketDLL, "Create_HP_TcpPackClient") else None
if Create_HP_TcpPackClient:
    Create_HP_TcpPackClient.restype = HP_TcpPackClient
    Create_HP_TcpPackClient.argtypes = [HP_TcpClientListener]
#  创建 HP_UdpServer 对象
# HPSOCKET_API HP_UdpServer __stdcall Create_HP_UdpServer(HP_UdpServerListener pListener);
Create_HP_UdpServer = HPSocketDLL.Create_HP_UdpServer if hasattr(HPSocketDLL, "Create_HP_UdpServer") else None
if Create_HP_UdpServer:
    Create_HP_UdpServer.restype = HP_UdpServer
    Create_HP_UdpServer.argtypes = [HP_UdpServerListener]
#  创建 HP_UdpClient 对象
# HPSOCKET_API HP_UdpClient __stdcall Create_HP_UdpClient(HP_UdpClientListener pListener);
Create_HP_UdpClient = HPSocketDLL.Create_HP_UdpClient if hasattr(HPSocketDLL, "Create_HP_UdpClient") else None
if Create_HP_UdpClient:
    Create_HP_UdpClient.restype = HP_UdpClient
    Create_HP_UdpClient.argtypes = [HP_UdpClientListener]
#  创建 HP_UdpCast 对象
# HPSOCKET_API HP_UdpCast __stdcall Create_HP_UdpCast(HP_UdpCastListener pListener);
Create_HP_UdpCast = HPSocketDLL.Create_HP_UdpCast if hasattr(HPSocketDLL, "Create_HP_UdpCast") else None
if Create_HP_UdpCast:
    Create_HP_UdpCast.restype = HP_UdpCast
    Create_HP_UdpCast.argtypes = [HP_UdpCastListener]

#  销毁 HP_TcpServer 对象
# HPSOCKET_API void __stdcall Destroy_HP_TcpServer(HP_TcpServer pServer);
Destroy_HP_TcpServer = HPSocketDLL.Destroy_HP_TcpServer if hasattr(HPSocketDLL, "Destroy_HP_TcpServer") else None
if Destroy_HP_TcpServer:
    Destroy_HP_TcpServer.restype = None
    Destroy_HP_TcpServer.argtypes = [HP_TcpServer]
#  销毁 HP_TcpAgent 对象
# HPSOCKET_API void __stdcall Destroy_HP_TcpAgent(HP_TcpAgent pAgent);
Destroy_HP_TcpAgent = HPSocketDLL.Destroy_HP_TcpAgent if hasattr(HPSocketDLL, "Destroy_HP_TcpAgent") else None
if Destroy_HP_TcpAgent:
    Destroy_HP_TcpAgent.restype = None
    Destroy_HP_TcpAgent.argtypes = [HP_TcpAgent]
#  销毁 HP_TcpClient 对象
# HPSOCKET_API void __stdcall Destroy_HP_TcpClient(HP_TcpClient pClient);
Destroy_HP_TcpClient = HPSocketDLL.Destroy_HP_TcpClient if hasattr(HPSocketDLL, "Destroy_HP_TcpClient") else None
if Destroy_HP_TcpClient:
    Destroy_HP_TcpClient.restype = None
    Destroy_HP_TcpClient.argtypes = [HP_TcpClient]
#  销毁 HP_TcpPullServer 对象
# HPSOCKET_API void __stdcall Destroy_HP_TcpPullServer(HP_TcpPullServer pServer);
Destroy_HP_TcpPullServer = HPSocketDLL.Destroy_HP_TcpPullServer if hasattr(HPSocketDLL, "Destroy_HP_TcpPullServer") else None
if Destroy_HP_TcpPullServer:
    Destroy_HP_TcpPullServer.restype = None
    Destroy_HP_TcpPullServer.argtypes = [HP_TcpPullServer]
#  销毁 HP_TcpPullAgent 对象
# HPSOCKET_API void __stdcall Destroy_HP_TcpPullAgent(HP_TcpPullAgent pAgent);
Destroy_HP_TcpPullAgent = HPSocketDLL.Destroy_HP_TcpPullAgent if hasattr(HPSocketDLL, "Destroy_HP_TcpPullAgent") else None
if Destroy_HP_TcpPullAgent:
    Destroy_HP_TcpPullAgent.restype = None
    Destroy_HP_TcpPullAgent.argtypes = [HP_TcpPullAgent]
#  销毁 HP_TcpPullClient 对象
# HPSOCKET_API void __stdcall Destroy_HP_TcpPullClient(HP_TcpPullClient pClient);
Destroy_HP_TcpPullClient = HPSocketDLL.Destroy_HP_TcpPullClient if hasattr(HPSocketDLL, "Destroy_HP_TcpPullClient") else None
if Destroy_HP_TcpPullClient:
    Destroy_HP_TcpPullClient.restype = None
    Destroy_HP_TcpPullClient.argtypes = [HP_TcpPullClient]
#  销毁 HP_TcpPackServer 对象
# HPSOCKET_API void __stdcall Destroy_HP_TcpPackServer(HP_TcpPackServer pServer);
Destroy_HP_TcpPackServer = HPSocketDLL.Destroy_HP_TcpPackServer if hasattr(HPSocketDLL, "Destroy_HP_TcpPackServer") else None
if Destroy_HP_TcpPackServer:
    Destroy_HP_TcpPackServer.restype = None
    Destroy_HP_TcpPackServer.argtypes = [HP_TcpPackServer]
#  销毁 HP_TcpPackAgent 对象
# HPSOCKET_API void __stdcall Destroy_HP_TcpPackAgent(HP_TcpPackAgent pAgent);
Destroy_HP_TcpPackAgent = HPSocketDLL.Destroy_HP_TcpPackAgent if hasattr(HPSocketDLL, "Destroy_HP_TcpPackAgent") else None
if Destroy_HP_TcpPackAgent:
    Destroy_HP_TcpPackAgent.restype = None
    Destroy_HP_TcpPackAgent.argtypes = [HP_TcpPackAgent]
#  销毁 HP_TcpPackClient 对象
# HPSOCKET_API void __stdcall Destroy_HP_TcpPackClient(HP_TcpPackClient pClient);
Destroy_HP_TcpPackClient = HPSocketDLL.Destroy_HP_TcpPackClient if hasattr(HPSocketDLL, "Destroy_HP_TcpPackClient") else None
if Destroy_HP_TcpPackClient:
    Destroy_HP_TcpPackClient.restype = None
    Destroy_HP_TcpPackClient.argtypes = [HP_TcpPackClient]
#  销毁 HP_UdpServer 对象
# HPSOCKET_API void __stdcall Destroy_HP_UdpServer(HP_UdpServer pServer);
Destroy_HP_UdpServer = HPSocketDLL.Destroy_HP_UdpServer if hasattr(HPSocketDLL, "Destroy_HP_UdpServer") else None
if Destroy_HP_UdpServer:
    Destroy_HP_UdpServer.restype = None
    Destroy_HP_UdpServer.argtypes = [HP_UdpServer]
#  销毁 HP_UdpClient 对象
# HPSOCKET_API void __stdcall Destroy_HP_UdpClient(HP_UdpClient pClient);
Destroy_HP_UdpClient = HPSocketDLL.Destroy_HP_UdpClient if hasattr(HPSocketDLL, "Destroy_HP_UdpClient") else None
if Destroy_HP_UdpClient:
    Destroy_HP_UdpClient.restype = None
    Destroy_HP_UdpClient.argtypes = [HP_UdpClient]
#  销毁 HP_UdpCast 对象
# HPSOCKET_API void __stdcall Destroy_HP_UdpCast(HP_UdpCast pCast);
Destroy_HP_UdpCast = HPSocketDLL.Destroy_HP_UdpCast if hasattr(HPSocketDLL, "Destroy_HP_UdpCast") else None
if Destroy_HP_UdpCast:
    Destroy_HP_UdpCast.restype = None
    Destroy_HP_UdpCast.argtypes = [HP_UdpCast]

#  创建 HP_TcpServerListener 对象
# HPSOCKET_API HP_TcpServerListener __stdcall Create_HP_TcpServerListener();
Create_HP_TcpServerListener = HPSocketDLL.Create_HP_TcpServerListener if hasattr(HPSocketDLL, "Create_HP_TcpServerListener") else None
if Create_HP_TcpServerListener:
    Create_HP_TcpServerListener.restype = HP_TcpServerListener
    Create_HP_TcpServerListener.argtypes = []
#  创建 HP_TcpAgentListener 对象
# HPSOCKET_API HP_TcpAgentListener __stdcall Create_HP_TcpAgentListener();
Create_HP_TcpAgentListener = HPSocketDLL.Create_HP_TcpAgentListener if hasattr(HPSocketDLL, "Create_HP_TcpAgentListener") else None
if Create_HP_TcpAgentListener:
    Create_HP_TcpAgentListener.restype = HP_TcpAgentListener
    Create_HP_TcpAgentListener.argtypes = []
#  创建 HP_TcpClientListener 对象
# HPSOCKET_API HP_TcpClientListener __stdcall Create_HP_TcpClientListener();
Create_HP_TcpClientListener = HPSocketDLL.Create_HP_TcpClientListener if hasattr(HPSocketDLL, "Create_HP_TcpClientListener") else None
if Create_HP_TcpClientListener:
    Create_HP_TcpClientListener.restype = HP_TcpClientListener
    Create_HP_TcpClientListener.argtypes = []
#  创建 HP_TcpPullServerListener 对象
# HPSOCKET_API HP_TcpPullServerListener __stdcall Create_HP_TcpPullServerListener();
Create_HP_TcpPullServerListener = HPSocketDLL.Create_HP_TcpPullServerListener if hasattr(HPSocketDLL, "Create_HP_TcpPullServerListener") else None
if Create_HP_TcpPullServerListener:
    Create_HP_TcpPullServerListener.restype = HP_TcpPullServerListener
    Create_HP_TcpPullServerListener.argtypes = []
#  创建 HP_TcpPullAgentListener 对象
# HPSOCKET_API HP_TcpPullAgentListener __stdcall Create_HP_TcpPullAgentListener();
Create_HP_TcpPullAgentListener = HPSocketDLL.Create_HP_TcpPullAgentListener if hasattr(HPSocketDLL, "Create_HP_TcpPullAgentListener") else None
if Create_HP_TcpPullAgentListener:
    Create_HP_TcpPullAgentListener.restype = HP_TcpPullAgentListener
    Create_HP_TcpPullAgentListener.argtypes = []
#  创建 HP_TcpPullClientListener 对象
# HPSOCKET_API HP_TcpPullClientListener __stdcall Create_HP_TcpPullClientListener();
Create_HP_TcpPullClientListener = HPSocketDLL.Create_HP_TcpPullClientListener if hasattr(HPSocketDLL, "Create_HP_TcpPullClientListener") else None
if Create_HP_TcpPullClientListener:
    Create_HP_TcpPullClientListener.restype = HP_TcpPullClientListener
    Create_HP_TcpPullClientListener.argtypes = []
#  创建 HP_TcpPackServerListener 对象
# HPSOCKET_API HP_TcpPackServerListener __stdcall Create_HP_TcpPackServerListener();
Create_HP_TcpPackServerListener = HPSocketDLL.Create_HP_TcpPackServerListener if hasattr(HPSocketDLL, "Create_HP_TcpPackServerListener") else None
if Create_HP_TcpPackServerListener:
    Create_HP_TcpPackServerListener.restype = HP_TcpPackServerListener
    Create_HP_TcpPackServerListener.argtypes = []
#  创建 HP_TcpPackAgentListener 对象
# HPSOCKET_API HP_TcpPackAgentListener __stdcall Create_HP_TcpPackAgentListener();
Create_HP_TcpPackAgentListener = HPSocketDLL.Create_HP_TcpPackAgentListener if hasattr(HPSocketDLL, "Create_HP_TcpPackAgentListener") else None
if Create_HP_TcpPackAgentListener:
    Create_HP_TcpPackAgentListener.restype = HP_TcpPackAgentListener
    Create_HP_TcpPackAgentListener.argtypes = []
#  创建 HP_TcpPackClientListener 对象
# HPSOCKET_API HP_TcpPackClientListener __stdcall Create_HP_TcpPackClientListener();
Create_HP_TcpPackClientListener = HPSocketDLL.Create_HP_TcpPackClientListener if hasattr(HPSocketDLL, "Create_HP_TcpPackClientListener") else None
if Create_HP_TcpPackClientListener:
    Create_HP_TcpPackClientListener.restype = HP_TcpPackClientListener
    Create_HP_TcpPackClientListener.argtypes = []
#  创建 HP_UdpServerListener 对象
# HPSOCKET_API HP_UdpServerListener __stdcall Create_HP_UdpServerListener();
Create_HP_UdpServerListener = HPSocketDLL.Create_HP_UdpServerListener if hasattr(HPSocketDLL, "Create_HP_UdpServerListener") else None
if Create_HP_UdpServerListener:
    Create_HP_UdpServerListener.restype = HP_UdpServerListener
    Create_HP_UdpServerListener.argtypes = []
#  创建 HP_UdpClientListener 对象
# HPSOCKET_API HP_UdpClientListener __stdcall Create_HP_UdpClientListener();
Create_HP_UdpClientListener = HPSocketDLL.Create_HP_UdpClientListener if hasattr(HPSocketDLL, "Create_HP_UdpClientListener") else None
if Create_HP_UdpClientListener:
    Create_HP_UdpClientListener.restype = HP_UdpClientListener
    Create_HP_UdpClientListener.argtypes = []
#  创建 HP_UdpCastListener 对象
# HPSOCKET_API HP_UdpCastListener __stdcall Create_HP_UdpCastListener();
Create_HP_UdpCastListener = HPSocketDLL.Create_HP_UdpCastListener if hasattr(HPSocketDLL, "Create_HP_UdpCastListener") else None
if Create_HP_UdpCastListener:
    Create_HP_UdpCastListener.restype = HP_UdpCastListener
    Create_HP_UdpCastListener.argtypes = []

#  销毁 HP_TcpServerListener 对象
# HPSOCKET_API void __stdcall Destroy_HP_TcpServerListener(HP_TcpServerListener pListener);
Destroy_HP_TcpServerListener = HPSocketDLL.Destroy_HP_TcpServerListener if hasattr(HPSocketDLL, "Destroy_HP_TcpServerListener") else None
if Destroy_HP_TcpServerListener:
    Destroy_HP_TcpServerListener.restype = None
    Destroy_HP_TcpServerListener.argtypes = [HP_TcpServerListener]
#  销毁 HP_TcpAgentListener 对象
# HPSOCKET_API void __stdcall Destroy_HP_TcpAgentListener(HP_TcpAgentListener pListener);
Destroy_HP_TcpAgentListener = HPSocketDLL.Destroy_HP_TcpAgentListener if hasattr(HPSocketDLL, "Destroy_HP_TcpAgentListener") else None
if Destroy_HP_TcpAgentListener:
    Destroy_HP_TcpAgentListener.restype = None
    Destroy_HP_TcpAgentListener.argtypes = [HP_TcpAgentListener]
#  销毁 HP_TcpClientListener 对象
# HPSOCKET_API void __stdcall Destroy_HP_TcpClientListener(HP_TcpClientListener pListener);
Destroy_HP_TcpClientListener = HPSocketDLL.Destroy_HP_TcpClientListener if hasattr(HPSocketDLL, "Destroy_HP_TcpClientListener") else None
if Destroy_HP_TcpClientListener:
    Destroy_HP_TcpClientListener.restype = None
    Destroy_HP_TcpClientListener.argtypes = [HP_TcpClientListener]
#  销毁 HP_TcpPullServerListener 对象
# HPSOCKET_API void __stdcall Destroy_HP_TcpPullServerListener(HP_TcpPullServerListener pListener);
Destroy_HP_TcpPullServerListener = HPSocketDLL.Destroy_HP_TcpPullServerListener if hasattr(HPSocketDLL, "Destroy_HP_TcpPullServerListener") else None
if Destroy_HP_TcpPullServerListener:
    Destroy_HP_TcpPullServerListener.restype = None
    Destroy_HP_TcpPullServerListener.argtypes = [HP_TcpPullServerListener]
#  销毁 HP_TcpPullAgentListener 对象
# HPSOCKET_API void __stdcall Destroy_HP_TcpPullAgentListener(HP_TcpPullAgentListener pListener);
Destroy_HP_TcpPullAgentListener = HPSocketDLL.Destroy_HP_TcpPullAgentListener if hasattr(HPSocketDLL, "Destroy_HP_TcpPullAgentListener") else None
if Destroy_HP_TcpPullAgentListener:
    Destroy_HP_TcpPullAgentListener.restype = None
    Destroy_HP_TcpPullAgentListener.argtypes = [HP_TcpPullAgentListener]
#  销毁 HP_TcpPullClientListener 对象
# HPSOCKET_API void __stdcall Destroy_HP_TcpPullClientListener(HP_TcpPullClientListener pListener);
Destroy_HP_TcpPullClientListener = HPSocketDLL.Destroy_HP_TcpPullClientListener if hasattr(HPSocketDLL, "Destroy_HP_TcpPullClientListener") else None
if Destroy_HP_TcpPullClientListener:
    Destroy_HP_TcpPullClientListener.restype = None
    Destroy_HP_TcpPullClientListener.argtypes = [HP_TcpPullClientListener]
#  销毁 HP_TcpPackServerListener 对象
# HPSOCKET_API void __stdcall Destroy_HP_TcpPackServerListener(HP_TcpPackServerListener pListener);
Destroy_HP_TcpPackServerListener = HPSocketDLL.Destroy_HP_TcpPackServerListener if hasattr(HPSocketDLL, "Destroy_HP_TcpPackServerListener") else None
if Destroy_HP_TcpPackServerListener:
    Destroy_HP_TcpPackServerListener.restype = None
    Destroy_HP_TcpPackServerListener.argtypes = [HP_TcpPackServerListener]
#  销毁 HP_TcpPackAgentListener 对象
# HPSOCKET_API void __stdcall Destroy_HP_TcpPackAgentListener(HP_TcpPackAgentListener pListener);
Destroy_HP_TcpPackAgentListener = HPSocketDLL.Destroy_HP_TcpPackAgentListener if hasattr(HPSocketDLL, "Destroy_HP_TcpPackAgentListener") else None
if Destroy_HP_TcpPackAgentListener:
    Destroy_HP_TcpPackAgentListener.restype = None
    Destroy_HP_TcpPackAgentListener.argtypes = [HP_TcpPackAgentListener]
#  销毁 HP_TcpPackClientListener 对象
# HPSOCKET_API void __stdcall Destroy_HP_TcpPackClientListener(HP_TcpPackClientListener pListener);
Destroy_HP_TcpPackClientListener = HPSocketDLL.Destroy_HP_TcpPackClientListener if hasattr(HPSocketDLL, "Destroy_HP_TcpPackClientListener") else None
if Destroy_HP_TcpPackClientListener:
    Destroy_HP_TcpPackClientListener.restype = None
    Destroy_HP_TcpPackClientListener.argtypes = [HP_TcpPackClientListener]
#  销毁 HP_UdpServerListener 对象
# HPSOCKET_API void __stdcall Destroy_HP_UdpServerListener(HP_UdpServerListener pListener);
Destroy_HP_UdpServerListener = HPSocketDLL.Destroy_HP_UdpServerListener if hasattr(HPSocketDLL, "Destroy_HP_UdpServerListener") else None
if Destroy_HP_UdpServerListener:
    Destroy_HP_UdpServerListener.restype = None
    Destroy_HP_UdpServerListener.argtypes = [HP_UdpServerListener]
#  销毁 HP_UdpClientListener 对象
# HPSOCKET_API void __stdcall Destroy_HP_UdpClientListener(HP_UdpClientListener pListener);
Destroy_HP_UdpClientListener = HPSocketDLL.Destroy_HP_UdpClientListener if hasattr(HPSocketDLL, "Destroy_HP_UdpClientListener") else None
if Destroy_HP_UdpClientListener:
    Destroy_HP_UdpClientListener.restype = None
    Destroy_HP_UdpClientListener.argtypes = [HP_UdpClientListener]
#  销毁 HP_UdpCastListener 对象
# HPSOCKET_API void __stdcall Destroy_HP_UdpCastListener(HP_UdpCastListener pListener);
Destroy_HP_UdpCastListener = HPSocketDLL.Destroy_HP_UdpCastListener if hasattr(HPSocketDLL, "Destroy_HP_UdpCastListener") else None
if Destroy_HP_UdpCastListener:
    Destroy_HP_UdpCastListener.restype = None
    Destroy_HP_UdpCastListener.argtypes = [HP_UdpCastListener]

# ********************************************************************************
# **************************** Server 回调函数设置方法 ****************************

# HPSOCKET_API void __stdcall HP_Set_FN_Server_OnPrepareListen(HP_ServerListener pListener	, HP_FN_Server_OnPrepareListen fn);
HP_Set_FN_Server_OnPrepareListen = HPSocketDLL.HP_Set_FN_Server_OnPrepareListen if hasattr(HPSocketDLL, "HP_Set_FN_Server_OnPrepareListen") else None
if HP_Set_FN_Server_OnPrepareListen:
    HP_Set_FN_Server_OnPrepareListen.restype = None
    HP_Set_FN_Server_OnPrepareListen.argtypes = [HP_ServerListener, HP_FN_Server_OnPrepareListen]
# HPSOCKET_API void __stdcall HP_Set_FN_Server_OnAccept(HP_ServerListener pListener			, HP_FN_Server_OnAccept fn);
HP_Set_FN_Server_OnAccept = HPSocketDLL.HP_Set_FN_Server_OnAccept if hasattr(HPSocketDLL, "HP_Set_FN_Server_OnAccept") else None
if HP_Set_FN_Server_OnAccept:
    HP_Set_FN_Server_OnAccept.restype = None
    HP_Set_FN_Server_OnAccept.argtypes = [HP_ServerListener, HP_FN_Server_OnAccept]
# HPSOCKET_API void __stdcall HP_Set_FN_Server_OnHandShake(HP_ServerListener pListener		, HP_FN_Server_OnHandShake fn);
HP_Set_FN_Server_OnHandShake = HPSocketDLL.HP_Set_FN_Server_OnHandShake if hasattr(HPSocketDLL, "HP_Set_FN_Server_OnHandShake") else None
if HP_Set_FN_Server_OnHandShake:
    HP_Set_FN_Server_OnHandShake.restype = None
    HP_Set_FN_Server_OnHandShake.argtypes = [HP_ServerListener, HP_FN_Server_OnHandShake]
# HPSOCKET_API void __stdcall HP_Set_FN_Server_OnSend(HP_ServerListener pListener				, HP_FN_Server_OnSend fn);
HP_Set_FN_Server_OnSend = HPSocketDLL.HP_Set_FN_Server_OnSend if hasattr(HPSocketDLL, "HP_Set_FN_Server_OnSend") else None
if HP_Set_FN_Server_OnSend:
    HP_Set_FN_Server_OnSend.restype = None
    HP_Set_FN_Server_OnSend.argtypes = [HP_ServerListener, HP_FN_Server_OnSend]
# HPSOCKET_API void __stdcall HP_Set_FN_Server_OnReceive(HP_ServerListener pListener			, HP_FN_Server_OnReceive fn);
HP_Set_FN_Server_OnReceive = HPSocketDLL.HP_Set_FN_Server_OnReceive if hasattr(HPSocketDLL, "HP_Set_FN_Server_OnReceive") else None
if HP_Set_FN_Server_OnReceive:
    HP_Set_FN_Server_OnReceive.restype = None
    HP_Set_FN_Server_OnReceive.argtypes = [HP_ServerListener, HP_FN_Server_OnReceive]
# HPSOCKET_API void __stdcall HP_Set_FN_Server_OnPullReceive(HP_ServerListener pListener		, HP_FN_Server_OnPullReceive fn);
HP_Set_FN_Server_OnPullReceive = HPSocketDLL.HP_Set_FN_Server_OnPullReceive if hasattr(HPSocketDLL, "HP_Set_FN_Server_OnPullReceive") else None
if HP_Set_FN_Server_OnPullReceive:
    HP_Set_FN_Server_OnPullReceive.restype = None
    HP_Set_FN_Server_OnPullReceive.argtypes = [HP_ServerListener, HP_FN_Server_OnPullReceive]
# HPSOCKET_API void __stdcall HP_Set_FN_Server_OnClose(HP_ServerListener pListener			, HP_FN_Server_OnClose fn);
HP_Set_FN_Server_OnClose = HPSocketDLL.HP_Set_FN_Server_OnClose if hasattr(HPSocketDLL, "HP_Set_FN_Server_OnClose") else None
if HP_Set_FN_Server_OnClose:
    HP_Set_FN_Server_OnClose.restype = None
    HP_Set_FN_Server_OnClose.argtypes = [HP_ServerListener, HP_FN_Server_OnClose]
# HPSOCKET_API void __stdcall HP_Set_FN_Server_OnShutdown(HP_ServerListener pListener			, HP_FN_Server_OnShutdown fn);
HP_Set_FN_Server_OnShutdown = HPSocketDLL.HP_Set_FN_Server_OnShutdown if hasattr(HPSocketDLL, "HP_Set_FN_Server_OnShutdown") else None
if HP_Set_FN_Server_OnShutdown:
    HP_Set_FN_Server_OnShutdown.restype = None
    HP_Set_FN_Server_OnShutdown.argtypes = [HP_ServerListener, HP_FN_Server_OnShutdown]

# ********************************************************************************
# ***************************** Agent 回调函数设置方法 ****************************

# HPSOCKET_API void __stdcall HP_Set_FN_Agent_OnPrepareConnect(HP_AgentListener pListener		, HP_FN_Agent_OnPrepareConnect fn);
HP_Set_FN_Agent_OnPrepareConnect = HPSocketDLL.HP_Set_FN_Agent_OnPrepareConnect if hasattr(HPSocketDLL, "HP_Set_FN_Agent_OnPrepareConnect") else None
if HP_Set_FN_Agent_OnPrepareConnect:
    HP_Set_FN_Agent_OnPrepareConnect.restype = None
    HP_Set_FN_Agent_OnPrepareConnect.argtypes = [HP_AgentListener, HP_FN_Agent_OnPrepareConnect]
# HPSOCKET_API void __stdcall HP_Set_FN_Agent_OnConnect(HP_AgentListener pListener			, HP_FN_Agent_OnConnect fn);
HP_Set_FN_Agent_OnConnect = HPSocketDLL.HP_Set_FN_Agent_OnConnect if hasattr(HPSocketDLL, "HP_Set_FN_Agent_OnConnect") else None
if HP_Set_FN_Agent_OnConnect:
    HP_Set_FN_Agent_OnConnect.restype = None
    HP_Set_FN_Agent_OnConnect.argtypes = [HP_AgentListener, HP_FN_Agent_OnConnect]
# HPSOCKET_API void __stdcall HP_Set_FN_Agent_OnHandShake(HP_AgentListener pListener			, HP_FN_Agent_OnHandShake fn);
HP_Set_FN_Agent_OnHandShake = HPSocketDLL.HP_Set_FN_Agent_OnHandShake if hasattr(HPSocketDLL, "HP_Set_FN_Agent_OnHandShake") else None
if HP_Set_FN_Agent_OnHandShake:
    HP_Set_FN_Agent_OnHandShake.restype = None
    HP_Set_FN_Agent_OnHandShake.argtypes = [HP_AgentListener, HP_FN_Agent_OnHandShake]
# HPSOCKET_API void __stdcall HP_Set_FN_Agent_OnSend(HP_AgentListener pListener				, HP_FN_Agent_OnSend fn);
HP_Set_FN_Agent_OnSend = HPSocketDLL.HP_Set_FN_Agent_OnSend if hasattr(HPSocketDLL, "HP_Set_FN_Agent_OnSend") else None
if HP_Set_FN_Agent_OnSend:
    HP_Set_FN_Agent_OnSend.restype = None
    HP_Set_FN_Agent_OnSend.argtypes = [HP_AgentListener, HP_FN_Agent_OnSend]
# HPSOCKET_API void __stdcall HP_Set_FN_Agent_OnReceive(HP_AgentListener pListener			, HP_FN_Agent_OnReceive fn);
HP_Set_FN_Agent_OnReceive = HPSocketDLL.HP_Set_FN_Agent_OnReceive if hasattr(HPSocketDLL, "HP_Set_FN_Agent_OnReceive") else None
if HP_Set_FN_Agent_OnReceive:
    HP_Set_FN_Agent_OnReceive.restype = None
    HP_Set_FN_Agent_OnReceive.argtypes = [HP_AgentListener, HP_FN_Agent_OnReceive]
# HPSOCKET_API void __stdcall HP_Set_FN_Agent_OnPullReceive(HP_AgentListener pListener		, HP_FN_Agent_OnPullReceive fn);
HP_Set_FN_Agent_OnPullReceive = HPSocketDLL.HP_Set_FN_Agent_OnPullReceive if hasattr(HPSocketDLL, "HP_Set_FN_Agent_OnPullReceive") else None
if HP_Set_FN_Agent_OnPullReceive:
    HP_Set_FN_Agent_OnPullReceive.restype = None
    HP_Set_FN_Agent_OnPullReceive.argtypes = [HP_AgentListener, HP_FN_Agent_OnPullReceive]
# HPSOCKET_API void __stdcall HP_Set_FN_Agent_OnClose(HP_AgentListener pListener				, HP_FN_Agent_OnClose fn);
HP_Set_FN_Agent_OnClose = HPSocketDLL.HP_Set_FN_Agent_OnClose if hasattr(HPSocketDLL, "HP_Set_FN_Agent_OnClose") else None
if HP_Set_FN_Agent_OnClose:
    HP_Set_FN_Agent_OnClose.restype = None
    HP_Set_FN_Agent_OnClose.argtypes = [HP_AgentListener, HP_FN_Agent_OnClose]
# HPSOCKET_API void __stdcall HP_Set_FN_Agent_OnShutdown(HP_AgentListener pListener			, HP_FN_Agent_OnShutdown fn);
HP_Set_FN_Agent_OnShutdown = HPSocketDLL.HP_Set_FN_Agent_OnShutdown if hasattr(HPSocketDLL, "HP_Set_FN_Agent_OnShutdown") else None
if HP_Set_FN_Agent_OnShutdown:
    HP_Set_FN_Agent_OnShutdown.restype = None
    HP_Set_FN_Agent_OnShutdown.argtypes = [HP_AgentListener, HP_FN_Agent_OnShutdown]

# ********************************************************************************
# **************************** Client 回调函数设置方法 ****************************

# HPSOCKET_API void __stdcall HP_Set_FN_Client_OnPrepareConnect(HP_ClientListener pListener	, HP_FN_Client_OnPrepareConnect fn);
HP_Set_FN_Client_OnPrepareConnect = HPSocketDLL.HP_Set_FN_Client_OnPrepareConnect if hasattr(HPSocketDLL, "HP_Set_FN_Client_OnPrepareConnect") else None
if HP_Set_FN_Client_OnPrepareConnect:
    HP_Set_FN_Client_OnPrepareConnect.restype = None
    HP_Set_FN_Client_OnPrepareConnect.argtypes = [HP_ClientListener, HP_FN_Client_OnPrepareConnect]
# HPSOCKET_API void __stdcall HP_Set_FN_Client_OnConnect(HP_ClientListener pListener			, HP_FN_Client_OnConnect fn);
HP_Set_FN_Client_OnConnect = HPSocketDLL.HP_Set_FN_Client_OnConnect if hasattr(HPSocketDLL, "HP_Set_FN_Client_OnConnect") else None
if HP_Set_FN_Client_OnConnect:
    HP_Set_FN_Client_OnConnect.restype = None
    HP_Set_FN_Client_OnConnect.argtypes = [HP_ClientListener, HP_FN_Client_OnConnect]
# HPSOCKET_API void __stdcall HP_Set_FN_Client_OnHandShake(HP_ClientListener pListener		, HP_FN_Client_OnHandShake fn);
HP_Set_FN_Client_OnHandShake = HPSocketDLL.HP_Set_FN_Client_OnHandShake if hasattr(HPSocketDLL, "HP_Set_FN_Client_OnHandShake") else None
if HP_Set_FN_Client_OnHandShake:
    HP_Set_FN_Client_OnHandShake.restype = None
    HP_Set_FN_Client_OnHandShake.argtypes = [HP_ClientListener, HP_FN_Client_OnHandShake]
# HPSOCKET_API void __stdcall HP_Set_FN_Client_OnSend(HP_ClientListener pListener				, HP_FN_Client_OnSend fn);
HP_Set_FN_Client_OnSend = HPSocketDLL.HP_Set_FN_Client_OnSend if hasattr(HPSocketDLL, "HP_Set_FN_Client_OnSend") else None
if HP_Set_FN_Client_OnSend:
    HP_Set_FN_Client_OnSend.restype = None
    HP_Set_FN_Client_OnSend.argtypes = [HP_ClientListener, HP_FN_Client_OnSend]
# HPSOCKET_API void __stdcall HP_Set_FN_Client_OnReceive(HP_ClientListener pListener			, HP_FN_Client_OnReceive fn);
HP_Set_FN_Client_OnReceive = HPSocketDLL.HP_Set_FN_Client_OnReceive if hasattr(HPSocketDLL, "HP_Set_FN_Client_OnReceive") else None
if HP_Set_FN_Client_OnReceive:
    HP_Set_FN_Client_OnReceive.restype = None
    HP_Set_FN_Client_OnReceive.argtypes = [HP_ClientListener, HP_FN_Client_OnReceive]
# HPSOCKET_API void __stdcall HP_Set_FN_Client_OnPullReceive(HP_ClientListener pListener		, HP_FN_Client_OnPullReceive fn);
HP_Set_FN_Client_OnPullReceive = HPSocketDLL.HP_Set_FN_Client_OnPullReceive if hasattr(HPSocketDLL, "HP_Set_FN_Client_OnPullReceive") else None
if HP_Set_FN_Client_OnPullReceive:
    HP_Set_FN_Client_OnPullReceive.restype = None
    HP_Set_FN_Client_OnPullReceive.argtypes = [HP_ClientListener, HP_FN_Client_OnPullReceive]
# HPSOCKET_API void __stdcall HP_Set_FN_Client_OnClose(HP_ClientListener pListener			, HP_FN_Client_OnClose fn);
HP_Set_FN_Client_OnClose = HPSocketDLL.HP_Set_FN_Client_OnClose if hasattr(HPSocketDLL, "HP_Set_FN_Client_OnClose") else None
if HP_Set_FN_Client_OnClose:
    HP_Set_FN_Client_OnClose.restype = None
    HP_Set_FN_Client_OnClose.argtypes = [HP_ClientListener, HP_FN_Client_OnClose]

# ************************************************************************
# **************************** Server 操作方法 ****************************

#
# * 名称：启动通信组件
# * 描述：启动服务端通信组件，启动完成后可开始接收客户端连接并收发数据
# *
# * 参数：		lpszBindAddress	-- 监听地址
# *			usPort			-- 监听端口
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败，可通过 HP_Server_GetLastError() 获取错误代码
#
# HPSOCKET_API BOOL __stdcall HP_Server_Start(HP_Server pServer, LPCTSTR lpszBindAddress, USHORT usPort);
HP_Server_Start = HPSocketDLL.HP_Server_Start if hasattr(HPSocketDLL, "HP_Server_Start") else None
if HP_Server_Start:
    HP_Server_Start.restype = ctypes.c_bool
    HP_Server_Start.argtypes = [HP_Server, ctypes.c_char_p, ctypes.c_ushort]

#
# * 名称：关闭通信组件
# * 描述：关闭服务端通信组件，关闭完成后断开所有客户端连接并释放所有资源
# *
# * 参数：
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败，可通过 HP_Server_GetLastError() 获取错误代码
#
# HPSOCKET_API BOOL __stdcall HP_Server_Stop(HP_Server pServer);
HP_Server_Stop = HPSocketDLL.HP_Server_Stop if hasattr(HPSocketDLL, "HP_Server_Stop") else None
if HP_Server_Stop:
    HP_Server_Stop.restype = ctypes.c_bool
    HP_Server_Stop.argtypes = [HP_Server]

#
# * 名称：发送数据
# * 描述：向指定连接发送数据
# *
# * 参数：		dwConnID	-- 连接 ID
# *			pBuffer		-- 发送缓冲区
# *			iLength		-- 发送缓冲区长度
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败，可通过 SYS_GetLastError() 获取 Windows 错误代码
#
# HPSOCKET_API BOOL __stdcall HP_Server_Send(HP_Server pServer, HP_CONNID dwConnID, const BYTE* pBuffer, int iLength);
HP_Server_Send = HPSocketDLL.HP_Server_Send if hasattr(HPSocketDLL, "HP_Server_Send") else None
if HP_Server_Send:
    HP_Server_Send.restype = ctypes.c_bool
    HP_Server_Send.argtypes = [HP_Server, HP_CONNID, ctypes.POINTER(ctypes.c_byte), ctypes.c_int]

#
# * 名称：发送数据
# * 描述：向指定连接发送数据
# *
# * 参数：		dwConnID	-- 连接 ID
# *			pBuffer		-- 发送缓冲区
# *			iLength		-- 发送缓冲区长度
# *			iOffset		-- 发送缓冲区指针偏移量
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败，可通过 SYS_GetLastError() 获取 Windows 错误代码
#
# HPSOCKET_API BOOL __stdcall HP_Server_SendPart(HP_Server pServer, HP_CONNID dwConnID, const BYTE* pBuffer, int iLength, int iOffset);
HP_Server_SendPart = HPSocketDLL.HP_Server_SendPart if hasattr(HPSocketDLL, "HP_Server_SendPart") else None
if HP_Server_SendPart:
    HP_Server_SendPart.restype = ctypes.c_bool
    HP_Server_SendPart.argtypes = [HP_Server, HP_CONNID, ctypes.POINTER(ctypes.c_byte), ctypes.c_int, ctypes.c_int]

#
# * 名称：发送多组数据
# * 描述：向指定连接发送多组数据
# *		TCP - 顺序发送所有数据包
# *		UDP - 把所有数据包组合成一个数据包发送（数据包的总长度不能大于设置的 UDP 包最大长度）
# *
# * 参数：		dwConnID	-- 连接 ID
# *			pBuffers	-- 发送缓冲区数组
# *			iCount		-- 发送缓冲区数目
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败，可通过 SYS_GetLastError() 获取 Windows 错误代码
#
# HPSOCKET_API BOOL __stdcall HP_Server_SendPackets(HP_Server pServer, HP_CONNID dwConnID, const WSABUF pBuffers[], int iCount);
HP_Server_SendPackets = HPSocketDLL.HP_Server_SendPackets if hasattr(HPSocketDLL, "HP_Server_SendPackets") else None
if HP_Server_SendPackets:
    HP_Server_SendPackets.restype = ctypes.c_bool
    HP_Server_SendPackets.argtypes = [HP_Server, HP_CONNID, ctypes.POINTER(WSABUF), ctypes.c_int]

#
# * 名称：暂停/恢复接收
# * 描述：暂停/恢复某个连接的数据接收工作
# *
# * 参数：		dwConnID	-- 连接 ID
# *			bPause		-- TRUE - 暂停, FALSE - 恢复
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败
#
# HPSOCKET_API BOOL __stdcall HP_Server_PauseReceive(HP_Server pServer, HP_CONNID dwConnID, BOOL bPause);
HP_Server_PauseReceive = HPSocketDLL.HP_Server_PauseReceive if hasattr(HPSocketDLL, "HP_Server_PauseReceive") else None
if HP_Server_PauseReceive:
    HP_Server_PauseReceive.restype = ctypes.c_bool
    HP_Server_PauseReceive.argtypes = [HP_Server, HP_CONNID, ctypes.c_bool]

#
# * 名称：断开连接
# * 描述：断开与某个客户端的连接
# *
# * 参数：		dwConnID	-- 连接 ID
# *			bForce		-- 是否强制断开连接
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败
#
# HPSOCKET_API BOOL __stdcall HP_Server_Disconnect(HP_Server pServer, HP_CONNID dwConnID, BOOL bForce);
HP_Server_Disconnect = HPSocketDLL.HP_Server_Disconnect if hasattr(HPSocketDLL, "HP_Server_Disconnect") else None
if HP_Server_Disconnect:
    HP_Server_Disconnect.restype = ctypes.c_bool
    HP_Server_Disconnect.argtypes = [HP_Server, HP_CONNID, ctypes.c_bool]

#
# * 名称：断开超时连接
# * 描述：断开超过指定时长的连接
# *
# * 参数：		dwPeriod	-- 时长（毫秒）
# *			bForce		-- 是否强制断开连接
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败
#
# HPSOCKET_API BOOL __stdcall HP_Server_DisconnectLongConnections(HP_Server pServer, DWORD dwPeriod, BOOL bForce);
HP_Server_DisconnectLongConnections = HPSocketDLL.HP_Server_DisconnectLongConnections if hasattr(HPSocketDLL, "HP_Server_DisconnectLongConnections") else None
if HP_Server_DisconnectLongConnections:
    HP_Server_DisconnectLongConnections.restype = ctypes.c_bool
    HP_Server_DisconnectLongConnections.argtypes = [HP_Server, ctypes.c_uint, ctypes.c_bool]

#
# * 名称：断开静默连接
# * 描述：断开超过指定时长的静默连接
# *
# * 参数：		dwPeriod	-- 时长（毫秒）
# *			bForce		-- 是否强制断开连接
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败
#
# HPSOCKET_API BOOL __stdcall HP_Server_DisconnectSilenceConnections(HP_Server pServer, DWORD dwPeriod, BOOL bForce);
HP_Server_DisconnectSilenceConnections = HPSocketDLL.HP_Server_DisconnectSilenceConnections if hasattr(HPSocketDLL, "HP_Server_DisconnectSilenceConnections") else None
if HP_Server_DisconnectSilenceConnections:
    HP_Server_DisconnectSilenceConnections.restype = ctypes.c_bool
    HP_Server_DisconnectSilenceConnections.argtypes = [HP_Server, ctypes.c_uint, ctypes.c_bool]

# ****************************************************************************
# **************************** Server 属性访问方法 ****************************

#
# * 名称：设置连接的附加数据
# * 描述：是否为连接绑定附加数据或者绑定什么样的数据，均由应用程序只身决定
# *
# * 参数：		dwConnID	-- 连接 ID
# *			pv			-- 数据
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败（无效的连接 ID）
#
# HPSOCKET_API BOOL __stdcall HP_Server_SetConnectionExtra(HP_Server pServer, HP_CONNID dwConnID, PVOID pExtra);
HP_Server_SetConnectionExtra = HPSocketDLL.HP_Server_SetConnectionExtra if hasattr(HPSocketDLL, "HP_Server_SetConnectionExtra") else None
if HP_Server_SetConnectionExtra:
    HP_Server_SetConnectionExtra.restype = ctypes.c_bool
    HP_Server_SetConnectionExtra.argtypes = [HP_Server, HP_CONNID, PVOID]

#
# * 名称：获取连接的附加数据
# * 描述：是否为连接绑定附加数据或者绑定什么样的数据，均由应用程序只身决定
# *
# * 参数：		dwConnID	-- 连接 ID
# *			ppv			-- 数据指针
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败（无效的连接 ID）
#
# HPSOCKET_API BOOL __stdcall HP_Server_GetConnectionExtra(HP_Server pServer, HP_CONNID dwConnID, PVOID* ppExtra);
HP_Server_GetConnectionExtra = HPSocketDLL.HP_Server_GetConnectionExtra if hasattr(HPSocketDLL, "HP_Server_GetConnectionExtra") else None
if HP_Server_GetConnectionExtra:
    HP_Server_GetConnectionExtra.restype = ctypes.c_bool
    HP_Server_GetConnectionExtra.argtypes = [HP_Server, HP_CONNID, ctypes.POINTER(PVOID)]

#  检测是否为安全连接（SSL/HTTPS）
# HPSOCKET_API BOOL __stdcall HP_Server_IsSecure(HP_Server pServer);
HP_Server_IsSecure = HPSocketDLL.HP_Server_IsSecure if hasattr(HPSocketDLL, "HP_Server_IsSecure") else None
if HP_Server_IsSecure:
    HP_Server_IsSecure.restype = ctypes.c_bool
    HP_Server_IsSecure.argtypes = [HP_Server]
#  检查通信组件是否已启动
# HPSOCKET_API BOOL __stdcall HP_Server_HasStarted(HP_Server pServer);
HP_Server_HasStarted = HPSocketDLL.HP_Server_HasStarted if hasattr(HPSocketDLL, "HP_Server_HasStarted") else None
if HP_Server_HasStarted:
    HP_Server_HasStarted.restype = ctypes.c_bool
    HP_Server_HasStarted.argtypes = [HP_Server]
#  查看通信组件当前状态
# HPSOCKET_API En_HP_ServiceState __stdcall HP_Server_GetState(HP_Server pServer);
HP_Server_GetState = HPSocketDLL.HP_Server_GetState if hasattr(HPSocketDLL, "HP_Server_GetState") else None
if HP_Server_GetState:
    HP_Server_GetState.restype = En_HP_ServiceState
    HP_Server_GetState.argtypes = [HP_Server]
#  获取最近一次失败操作的错误代码
# HPSOCKET_API En_HP_SocketError __stdcall HP_Server_GetLastError(HP_Server pServer);
HP_Server_GetLastError = HPSocketDLL.HP_Server_GetLastError if hasattr(HPSocketDLL, "HP_Server_GetLastError") else None
if HP_Server_GetLastError:
    HP_Server_GetLastError.restype = En_HP_SocketError
    HP_Server_GetLastError.argtypes = [HP_Server]
#  获取最近一次失败操作的错误描述
# HPSOCKET_API LPCTSTR __stdcall HP_Server_GetLastErrorDesc(HP_Server pServer);
HP_Server_GetLastErrorDesc = HPSocketDLL.HP_Server_GetLastErrorDesc if hasattr(HPSocketDLL, "HP_Server_GetLastErrorDesc") else None
if HP_Server_GetLastErrorDesc:
    HP_Server_GetLastErrorDesc.restype = ctypes.c_char_p
    HP_Server_GetLastErrorDesc.argtypes = [HP_Server]
#  获取连接中未发出数据的长度
# HPSOCKET_API BOOL __stdcall HP_Server_GetPendingDataLength(HP_Server pServer, HP_CONNID dwConnID, int* piPending);
HP_Server_GetPendingDataLength = HPSocketDLL.HP_Server_GetPendingDataLength if hasattr(HPSocketDLL, "HP_Server_GetPendingDataLength") else None
if HP_Server_GetPendingDataLength:
    HP_Server_GetPendingDataLength.restype = ctypes.c_bool
    HP_Server_GetPendingDataLength.argtypes = [HP_Server, HP_CONNID, ctypes.POINTER(ctypes.c_int)]
#  获取连接的数据接收状态
# HPSOCKET_API BOOL __stdcall HP_Server_IsPauseReceive(HP_Server pServer, HP_CONNID dwConnID, BOOL* pbPaused);
HP_Server_IsPauseReceive = HPSocketDLL.HP_Server_IsPauseReceive if hasattr(HPSocketDLL, "HP_Server_IsPauseReceive") else None
if HP_Server_IsPauseReceive:
    HP_Server_IsPauseReceive.restype = ctypes.c_bool
    HP_Server_IsPauseReceive.argtypes = [HP_Server, HP_CONNID, ctypes.POINTER(ctypes.c_bool)]
#  获取客户端连接数
# HPSOCKET_API DWORD __stdcall HP_Server_GetConnectionCount(HP_Server pServer);
HP_Server_GetConnectionCount = HPSocketDLL.HP_Server_GetConnectionCount if hasattr(HPSocketDLL, "HP_Server_GetConnectionCount") else None
if HP_Server_GetConnectionCount:
    HP_Server_GetConnectionCount.restype = ctypes.c_uint
    HP_Server_GetConnectionCount.argtypes = [HP_Server]
#  获取所有连接的 HP_CONNID
# HPSOCKET_API BOOL __stdcall HP_Server_GetAllConnectionIDs(HP_Server pServer, HP_CONNID pIDs[], DWORD* pdwCount);
HP_Server_GetAllConnectionIDs = HPSocketDLL.HP_Server_GetAllConnectionIDs if hasattr(HPSocketDLL, "HP_Server_GetAllConnectionIDs") else None
if HP_Server_GetAllConnectionIDs:
    HP_Server_GetAllConnectionIDs.restype = ctypes.c_bool
    HP_Server_GetAllConnectionIDs.argtypes = [HP_Server, ctypes.POINTER(HP_CONNID), ctypes.POINTER(ctypes.c_uint)]
#  获取某个客户端连接时长（毫秒）
# HPSOCKET_API BOOL __stdcall HP_Server_GetConnectPeriod(HP_Server pServer, HP_CONNID dwConnID, DWORD* pdwPeriod);
HP_Server_GetConnectPeriod = HPSocketDLL.HP_Server_GetConnectPeriod if hasattr(HPSocketDLL, "HP_Server_GetConnectPeriod") else None
if HP_Server_GetConnectPeriod:
    HP_Server_GetConnectPeriod.restype = ctypes.c_bool
    HP_Server_GetConnectPeriod.argtypes = [HP_Server, HP_CONNID, ctypes.POINTER(ctypes.c_uint)]
#  获取某个连接静默时间（毫秒）
# HPSOCKET_API BOOL __stdcall HP_Server_GetSilencePeriod(HP_Server pServer, HP_CONNID dwConnID, DWORD* pdwPeriod);
HP_Server_GetSilencePeriod = HPSocketDLL.HP_Server_GetSilencePeriod if hasattr(HPSocketDLL, "HP_Server_GetSilencePeriod") else None
if HP_Server_GetSilencePeriod:
    HP_Server_GetSilencePeriod.restype = ctypes.c_bool
    HP_Server_GetSilencePeriod.argtypes = [HP_Server, HP_CONNID, ctypes.POINTER(ctypes.c_uint)]
#  获取监听 Socket 的地址信息
# HPSOCKET_API BOOL __stdcall HP_Server_GetListenAddress(HP_Server pServer, TCHAR lpszAddress[], int* piAddressLen, USHORT* pusPort);
HP_Server_GetListenAddress = HPSocketDLL.HP_Server_GetListenAddress if hasattr(HPSocketDLL, "HP_Server_GetListenAddress") else None
if HP_Server_GetListenAddress:
    HP_Server_GetListenAddress.restype = ctypes.c_bool
    HP_Server_GetListenAddress.argtypes = [HP_Server, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_ushort)]
#  获取某个连接的本地地址信息
# HPSOCKET_API BOOL __stdcall HP_Server_GetLocalAddress(HP_Server pServer, HP_CONNID dwConnID, TCHAR lpszAddress[], int* piAddressLen, USHORT* pusPort);
HP_Server_GetLocalAddress = HPSocketDLL.HP_Server_GetLocalAddress if hasattr(HPSocketDLL, "HP_Server_GetLocalAddress") else None
if HP_Server_GetLocalAddress:
    HP_Server_GetLocalAddress.restype = ctypes.c_bool
    HP_Server_GetLocalAddress.argtypes = [HP_Server, HP_CONNID, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_ushort)]
#  获取某个连接的远程地址信息
# HPSOCKET_API BOOL __stdcall HP_Server_GetRemoteAddress(HP_Server pServer, HP_CONNID dwConnID, TCHAR lpszAddress[], int* piAddressLen, USHORT* pusPort);
HP_Server_GetRemoteAddress = HPSocketDLL.HP_Server_GetRemoteAddress if hasattr(HPSocketDLL, "HP_Server_GetRemoteAddress") else None
if HP_Server_GetRemoteAddress:
    HP_Server_GetRemoteAddress.restype = ctypes.c_bool
    HP_Server_GetRemoteAddress.argtypes = [HP_Server, HP_CONNID, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_ushort)]

#  设置数据发送策略
# HPSOCKET_API void __stdcall HP_Server_SetSendPolicy(HP_Server pServer, En_HP_SendPolicy enSendPolicy);
HP_Server_SetSendPolicy = HPSocketDLL.HP_Server_SetSendPolicy if hasattr(HPSocketDLL, "HP_Server_SetSendPolicy") else None
if HP_Server_SetSendPolicy:
    HP_Server_SetSendPolicy.restype = None
    HP_Server_SetSendPolicy.argtypes = [HP_Server, En_HP_SendPolicy]
#  设置 Socket 缓存对象锁定时间（毫秒，在锁定期间该 Socket 缓存对象不能被获取使用）
# HPSOCKET_API void __stdcall HP_Server_SetFreeSocketObjLockTime(HP_Server pServer, DWORD dwFreeSocketObjLockTime);
HP_Server_SetFreeSocketObjLockTime = HPSocketDLL.HP_Server_SetFreeSocketObjLockTime if hasattr(HPSocketDLL, "HP_Server_SetFreeSocketObjLockTime") else None
if HP_Server_SetFreeSocketObjLockTime:
    HP_Server_SetFreeSocketObjLockTime.restype = None
    HP_Server_SetFreeSocketObjLockTime.argtypes = [HP_Server, ctypes.c_uint]
#  设置 Socket 缓存池大小（通常设置为平均并发连接数量的 1/3 - 1/2）
# HPSOCKET_API void __stdcall HP_Server_SetFreeSocketObjPool(HP_Server pServer, DWORD dwFreeSocketObjPool);
HP_Server_SetFreeSocketObjPool = HPSocketDLL.HP_Server_SetFreeSocketObjPool if hasattr(HPSocketDLL, "HP_Server_SetFreeSocketObjPool") else None
if HP_Server_SetFreeSocketObjPool:
    HP_Server_SetFreeSocketObjPool.restype = None
    HP_Server_SetFreeSocketObjPool.argtypes = [HP_Server, ctypes.c_uint]
#  设置内存块缓存池大小（通常设置为 Socket 缓存池大小的 2 - 3 倍）
# HPSOCKET_API void __stdcall HP_Server_SetFreeBufferObjPool(HP_Server pServer, DWORD dwFreeBufferObjPool);
HP_Server_SetFreeBufferObjPool = HPSocketDLL.HP_Server_SetFreeBufferObjPool if hasattr(HPSocketDLL, "HP_Server_SetFreeBufferObjPool") else None
if HP_Server_SetFreeBufferObjPool:
    HP_Server_SetFreeBufferObjPool.restype = None
    HP_Server_SetFreeBufferObjPool.argtypes = [HP_Server, ctypes.c_uint]
#  设置 Socket 缓存池回收阀值（通常设置为 Socket 缓存池大小的 3 倍）
# HPSOCKET_API void __stdcall HP_Server_SetFreeSocketObjHold(HP_Server pServer, DWORD dwFreeSocketObjHold);
HP_Server_SetFreeSocketObjHold = HPSocketDLL.HP_Server_SetFreeSocketObjHold if hasattr(HPSocketDLL, "HP_Server_SetFreeSocketObjHold") else None
if HP_Server_SetFreeSocketObjHold:
    HP_Server_SetFreeSocketObjHold.restype = None
    HP_Server_SetFreeSocketObjHold.argtypes = [HP_Server, ctypes.c_uint]
#  设置内存块缓存池回收阀值（通常设置为内存块缓存池大小的 3 倍）
# HPSOCKET_API void __stdcall HP_Server_SetFreeBufferObjHold(HP_Server pServer, DWORD dwFreeBufferObjHold);
HP_Server_SetFreeBufferObjHold = HPSocketDLL.HP_Server_SetFreeBufferObjHold if hasattr(HPSocketDLL, "HP_Server_SetFreeBufferObjHold") else None
if HP_Server_SetFreeBufferObjHold:
    HP_Server_SetFreeBufferObjHold.restype = None
    HP_Server_SetFreeBufferObjHold.argtypes = [HP_Server, ctypes.c_uint]
#  设置最大连接数（组件会根据设置值预分配内存，因此需要根据实际情况设置，不宜过大）
# HPSOCKET_API void __stdcall HP_Server_SetMaxConnectionCount(HP_Server pServer, DWORD dwMaxConnectionCount);
HP_Server_SetMaxConnectionCount = HPSocketDLL.HP_Server_SetMaxConnectionCount if hasattr(HPSocketDLL, "HP_Server_SetMaxConnectionCount") else None
if HP_Server_SetMaxConnectionCount:
    HP_Server_SetMaxConnectionCount.restype = None
    HP_Server_SetMaxConnectionCount.argtypes = [HP_Server, ctypes.c_uint]
#  设置工作线程数量（通常设置为 2 * CPU + 2）
# HPSOCKET_API void __stdcall HP_Server_SetWorkerThreadCount(HP_Server pServer, DWORD dwWorkerThreadCount);
HP_Server_SetWorkerThreadCount = HPSocketDLL.HP_Server_SetWorkerThreadCount if hasattr(HPSocketDLL, "HP_Server_SetWorkerThreadCount") else None
if HP_Server_SetWorkerThreadCount:
    HP_Server_SetWorkerThreadCount.restype = None
    HP_Server_SetWorkerThreadCount.argtypes = [HP_Server, ctypes.c_uint]
#  设置是否标记静默时间（设置为 TRUE 时 DisconnectSilenceConnections() 和 GetSilencePeriod() 才有效，默认：TRUE）
# HPSOCKET_API void __stdcall HP_Server_SetMarkSilence(HP_Server pServer, BOOL bMarkSilence);
HP_Server_SetMarkSilence = HPSocketDLL.HP_Server_SetMarkSilence if hasattr(HPSocketDLL, "HP_Server_SetMarkSilence") else None
if HP_Server_SetMarkSilence:
    HP_Server_SetMarkSilence.restype = None
    HP_Server_SetMarkSilence.argtypes = [HP_Server, ctypes.c_bool]

#  获取数据发送策略
# HPSOCKET_API En_HP_SendPolicy __stdcall HP_Server_GetSendPolicy(HP_Server pServer);
HP_Server_GetSendPolicy = HPSocketDLL.HP_Server_GetSendPolicy if hasattr(HPSocketDLL, "HP_Server_GetSendPolicy") else None
if HP_Server_GetSendPolicy:
    HP_Server_GetSendPolicy.restype = En_HP_SendPolicy
    HP_Server_GetSendPolicy.argtypes = [HP_Server]
#  获取 Socket 缓存对象锁定时间
# HPSOCKET_API DWORD __stdcall HP_Server_GetFreeSocketObjLockTime(HP_Server pServer);
HP_Server_GetFreeSocketObjLockTime = HPSocketDLL.HP_Server_GetFreeSocketObjLockTime if hasattr(HPSocketDLL, "HP_Server_GetFreeSocketObjLockTime") else None
if HP_Server_GetFreeSocketObjLockTime:
    HP_Server_GetFreeSocketObjLockTime.restype = ctypes.c_uint
    HP_Server_GetFreeSocketObjLockTime.argtypes = [HP_Server]
#  获取 Socket 缓存池大小
# HPSOCKET_API DWORD __stdcall HP_Server_GetFreeSocketObjPool(HP_Server pServer);
HP_Server_GetFreeSocketObjPool = HPSocketDLL.HP_Server_GetFreeSocketObjPool if hasattr(HPSocketDLL, "HP_Server_GetFreeSocketObjPool") else None
if HP_Server_GetFreeSocketObjPool:
    HP_Server_GetFreeSocketObjPool.restype = ctypes.c_uint
    HP_Server_GetFreeSocketObjPool.argtypes = [HP_Server]
#  获取内存块缓存池大小
# HPSOCKET_API DWORD __stdcall HP_Server_GetFreeBufferObjPool(HP_Server pServer);
HP_Server_GetFreeBufferObjPool = HPSocketDLL.HP_Server_GetFreeBufferObjPool if hasattr(HPSocketDLL, "HP_Server_GetFreeBufferObjPool") else None
if HP_Server_GetFreeBufferObjPool:
    HP_Server_GetFreeBufferObjPool.restype = ctypes.c_uint
    HP_Server_GetFreeBufferObjPool.argtypes = [HP_Server]
#  获取 Socket 缓存池回收阀值
# HPSOCKET_API DWORD __stdcall HP_Server_GetFreeSocketObjHold(HP_Server pServer);
HP_Server_GetFreeSocketObjHold = HPSocketDLL.HP_Server_GetFreeSocketObjHold if hasattr(HPSocketDLL, "HP_Server_GetFreeSocketObjHold") else None
if HP_Server_GetFreeSocketObjHold:
    HP_Server_GetFreeSocketObjHold.restype = ctypes.c_uint
    HP_Server_GetFreeSocketObjHold.argtypes = [HP_Server]
#  获取内存块缓存池回收阀值
# HPSOCKET_API DWORD __stdcall HP_Server_GetFreeBufferObjHold(HP_Server pServer);
HP_Server_GetFreeBufferObjHold = HPSocketDLL.HP_Server_GetFreeBufferObjHold if hasattr(HPSocketDLL, "HP_Server_GetFreeBufferObjHold") else None
if HP_Server_GetFreeBufferObjHold:
    HP_Server_GetFreeBufferObjHold.restype = ctypes.c_uint
    HP_Server_GetFreeBufferObjHold.argtypes = [HP_Server]
#  获取最大连接数
# HPSOCKET_API DWORD __stdcall HP_Server_GetMaxConnectionCount(HP_Server pServer);
HP_Server_GetMaxConnectionCount = HPSocketDLL.HP_Server_GetMaxConnectionCount if hasattr(HPSocketDLL, "HP_Server_GetMaxConnectionCount") else None
if HP_Server_GetMaxConnectionCount:
    HP_Server_GetMaxConnectionCount.restype = ctypes.c_uint
    HP_Server_GetMaxConnectionCount.argtypes = [HP_Server]
#  获取工作线程数量
# HPSOCKET_API DWORD __stdcall HP_Server_GetWorkerThreadCount(HP_Server pServer);
HP_Server_GetWorkerThreadCount = HPSocketDLL.HP_Server_GetWorkerThreadCount if hasattr(HPSocketDLL, "HP_Server_GetWorkerThreadCount") else None
if HP_Server_GetWorkerThreadCount:
    HP_Server_GetWorkerThreadCount.restype = ctypes.c_uint
    HP_Server_GetWorkerThreadCount.argtypes = [HP_Server]
#  检测是否标记静默时间
# HPSOCKET_API BOOL __stdcall HP_Server_IsMarkSilence(HP_Server pServer);
HP_Server_IsMarkSilence = HPSocketDLL.HP_Server_IsMarkSilence if hasattr(HPSocketDLL, "HP_Server_IsMarkSilence") else None
if HP_Server_IsMarkSilence:
    HP_Server_IsMarkSilence.restype = ctypes.c_bool
    HP_Server_IsMarkSilence.argtypes = [HP_Server]

# ********************************************************************************
# ****************************** TCP Server 操作方法 ******************************

#
# * 名称：发送小文件
# * 描述：向指定连接发送 4096 KB 以下的小文件
# *
# * 参数：		dwConnID		-- 连接 ID
# *			lpszFileName	-- 文件路径
# *			pHead			-- 头部附加数据
# *			pTail			-- 尾部附加数据
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败，可通过 SYS_GetLastError() 获取 Windows 错误代码
#
# HPSOCKET_API BOOL __stdcall HP_TcpServer_SendSmallFile(HP_Server pServer, HP_CONNID dwConnID, LPCTSTR lpszFileName, const LPWSABUF pHead, const LPWSABUF pTail);
HP_TcpServer_SendSmallFile = HPSocketDLL.HP_TcpServer_SendSmallFile if hasattr(HPSocketDLL, "HP_TcpServer_SendSmallFile") else None
if HP_TcpServer_SendSmallFile:
    HP_TcpServer_SendSmallFile.restype = ctypes.c_bool
    HP_TcpServer_SendSmallFile.argtypes = [HP_Server, HP_CONNID, ctypes.c_char_p, LPWSABUF, LPWSABUF]

# ********************************************************************************
# **************************** TCP Server 属性访问方法 ****************************

#  设置监听 Socket 的等候队列大小（根据并发连接数量调整设置）
# HPSOCKET_API void __stdcall HP_TcpServer_SetSocketListenQueue(HP_TcpServer pServer, DWORD dwSocketListenQueue);
HP_TcpServer_SetSocketListenQueue = HPSocketDLL.HP_TcpServer_SetSocketListenQueue if hasattr(HPSocketDLL, "HP_TcpServer_SetSocketListenQueue") else None
if HP_TcpServer_SetSocketListenQueue:
    HP_TcpServer_SetSocketListenQueue.restype = None
    HP_TcpServer_SetSocketListenQueue.argtypes = [HP_TcpServer, ctypes.c_uint]
#  设置 Accept 预投递数量（根据负载调整设置，Accept 预投递数量越大则支持的并发连接请求越多）
# HPSOCKET_API void __stdcall HP_TcpServer_SetAcceptSocketCount(HP_TcpServer pServer, DWORD dwAcceptSocketCount);
HP_TcpServer_SetAcceptSocketCount = HPSocketDLL.HP_TcpServer_SetAcceptSocketCount if hasattr(HPSocketDLL, "HP_TcpServer_SetAcceptSocketCount") else None
if HP_TcpServer_SetAcceptSocketCount:
    HP_TcpServer_SetAcceptSocketCount.restype = None
    HP_TcpServer_SetAcceptSocketCount.argtypes = [HP_TcpServer, ctypes.c_uint]
#  设置通信数据缓冲区大小（根据平均通信数据包大小调整设置，通常设置为 1024 的倍数）
# HPSOCKET_API void __stdcall HP_TcpServer_SetSocketBufferSize(HP_TcpServer pServer, DWORD dwSocketBufferSize);
HP_TcpServer_SetSocketBufferSize = HPSocketDLL.HP_TcpServer_SetSocketBufferSize if hasattr(HPSocketDLL, "HP_TcpServer_SetSocketBufferSize") else None
if HP_TcpServer_SetSocketBufferSize:
    HP_TcpServer_SetSocketBufferSize.restype = None
    HP_TcpServer_SetSocketBufferSize.argtypes = [HP_TcpServer, ctypes.c_uint]
#  设置正常心跳包间隔（毫秒，0 则不发送心跳包，默认：30 * 1000）
# HPSOCKET_API void __stdcall HP_TcpServer_SetKeepAliveTime(HP_TcpServer pServer, DWORD dwKeepAliveTime);
HP_TcpServer_SetKeepAliveTime = HPSocketDLL.HP_TcpServer_SetKeepAliveTime if hasattr(HPSocketDLL, "HP_TcpServer_SetKeepAliveTime") else None
if HP_TcpServer_SetKeepAliveTime:
    HP_TcpServer_SetKeepAliveTime.restype = None
    HP_TcpServer_SetKeepAliveTime.argtypes = [HP_TcpServer, ctypes.c_uint]
#  设置异常心跳包间隔（毫秒，0 不发送心跳包，，默认：10 * 1000，如果超过若干次 [默认：WinXP 5 次, Win7 10 次] 检测不到心跳确认包则认为已断线）
# HPSOCKET_API void __stdcall HP_TcpServer_SetKeepAliveInterval(HP_TcpServer pServer, DWORD dwKeepAliveInterval);
HP_TcpServer_SetKeepAliveInterval = HPSocketDLL.HP_TcpServer_SetKeepAliveInterval if hasattr(HPSocketDLL, "HP_TcpServer_SetKeepAliveInterval") else None
if HP_TcpServer_SetKeepAliveInterval:
    HP_TcpServer_SetKeepAliveInterval.restype = None
    HP_TcpServer_SetKeepAliveInterval.argtypes = [HP_TcpServer, ctypes.c_uint]

#  获取 Accept 预投递数量
# HPSOCKET_API DWORD __stdcall HP_TcpServer_GetAcceptSocketCount(HP_TcpServer pServer);
HP_TcpServer_GetAcceptSocketCount = HPSocketDLL.HP_TcpServer_GetAcceptSocketCount if hasattr(HPSocketDLL, "HP_TcpServer_GetAcceptSocketCount") else None
if HP_TcpServer_GetAcceptSocketCount:
    HP_TcpServer_GetAcceptSocketCount.restype = ctypes.c_uint
    HP_TcpServer_GetAcceptSocketCount.argtypes = [HP_TcpServer]
#  获取通信数据缓冲区大小
# HPSOCKET_API DWORD __stdcall HP_TcpServer_GetSocketBufferSize(HP_TcpServer pServer);
HP_TcpServer_GetSocketBufferSize = HPSocketDLL.HP_TcpServer_GetSocketBufferSize if hasattr(HPSocketDLL, "HP_TcpServer_GetSocketBufferSize") else None
if HP_TcpServer_GetSocketBufferSize:
    HP_TcpServer_GetSocketBufferSize.restype = ctypes.c_uint
    HP_TcpServer_GetSocketBufferSize.argtypes = [HP_TcpServer]
#  获取监听 Socket 的等候队列大小
# HPSOCKET_API DWORD __stdcall HP_TcpServer_GetSocketListenQueue(HP_TcpServer pServer);
HP_TcpServer_GetSocketListenQueue = HPSocketDLL.HP_TcpServer_GetSocketListenQueue if hasattr(HPSocketDLL, "HP_TcpServer_GetSocketListenQueue") else None
if HP_TcpServer_GetSocketListenQueue:
    HP_TcpServer_GetSocketListenQueue.restype = ctypes.c_uint
    HP_TcpServer_GetSocketListenQueue.argtypes = [HP_TcpServer]
#  获取正常心跳包间隔
# HPSOCKET_API DWORD __stdcall HP_TcpServer_GetKeepAliveTime(HP_TcpServer pServer);
HP_TcpServer_GetKeepAliveTime = HPSocketDLL.HP_TcpServer_GetKeepAliveTime if hasattr(HPSocketDLL, "HP_TcpServer_GetKeepAliveTime") else None
if HP_TcpServer_GetKeepAliveTime:
    HP_TcpServer_GetKeepAliveTime.restype = ctypes.c_uint
    HP_TcpServer_GetKeepAliveTime.argtypes = [HP_TcpServer]
#  获取异常心跳包间隔
# HPSOCKET_API DWORD __stdcall HP_TcpServer_GetKeepAliveInterval(HP_TcpServer pServer);
HP_TcpServer_GetKeepAliveInterval = HPSocketDLL.HP_TcpServer_GetKeepAliveInterval if hasattr(HPSocketDLL, "HP_TcpServer_GetKeepAliveInterval") else None
if HP_TcpServer_GetKeepAliveInterval:
    HP_TcpServer_GetKeepAliveInterval.restype = ctypes.c_uint
    HP_TcpServer_GetKeepAliveInterval.argtypes = [HP_TcpServer]

# ********************************************************************************
# **************************** UDP Server 属性访问方法 ****************************

#  设置数据报文最大长度（建议在局域网环境下不超过 1472 字节，在广域网环境下不超过 548 字节）
# HPSOCKET_API void __stdcall HP_UdpServer_SetMaxDatagramSize(HP_UdpServer pServer, DWORD dwMaxDatagramSize);
HP_UdpServer_SetMaxDatagramSize = HPSocketDLL.HP_UdpServer_SetMaxDatagramSize if hasattr(HPSocketDLL, "HP_UdpServer_SetMaxDatagramSize") else None
if HP_UdpServer_SetMaxDatagramSize:
    HP_UdpServer_SetMaxDatagramSize.restype = None
    HP_UdpServer_SetMaxDatagramSize.argtypes = [HP_UdpServer, ctypes.c_uint]
#  获取数据报文最大长度
# HPSOCKET_API DWORD __stdcall HP_UdpServer_GetMaxDatagramSize(HP_UdpServer pServer);
HP_UdpServer_GetMaxDatagramSize = HPSocketDLL.HP_UdpServer_GetMaxDatagramSize if hasattr(HPSocketDLL, "HP_UdpServer_GetMaxDatagramSize") else None
if HP_UdpServer_GetMaxDatagramSize:
    HP_UdpServer_GetMaxDatagramSize.restype = ctypes.c_uint
    HP_UdpServer_GetMaxDatagramSize.argtypes = [HP_UdpServer]

#  设置 Receive 预投递数量（根据负载调整设置，Receive 预投递数量越大则丢包概率越小）
# HPSOCKET_API void __stdcall HP_UdpServer_SetPostReceiveCount(HP_UdpServer pServer, DWORD dwPostReceiveCount);
HP_UdpServer_SetPostReceiveCount = HPSocketDLL.HP_UdpServer_SetPostReceiveCount if hasattr(HPSocketDLL, "HP_UdpServer_SetPostReceiveCount") else None
if HP_UdpServer_SetPostReceiveCount:
    HP_UdpServer_SetPostReceiveCount.restype = None
    HP_UdpServer_SetPostReceiveCount.argtypes = [HP_UdpServer, ctypes.c_uint]
#  获取 Receive 预投递数量
# HPSOCKET_API DWORD __stdcall HP_UdpServer_GetPostReceiveCount(HP_UdpServer pServer);
HP_UdpServer_GetPostReceiveCount = HPSocketDLL.HP_UdpServer_GetPostReceiveCount if hasattr(HPSocketDLL, "HP_UdpServer_GetPostReceiveCount") else None
if HP_UdpServer_GetPostReceiveCount:
    HP_UdpServer_GetPostReceiveCount.restype = ctypes.c_uint
    HP_UdpServer_GetPostReceiveCount.argtypes = [HP_UdpServer]

#  设置监测包尝试次数（0 则不发送监测跳包，如果超过最大尝试次数则认为已断线）
# HPSOCKET_API void __stdcall HP_UdpServer_SetDetectAttempts(HP_UdpServer pServer, DWORD dwDetectAttempts);
HP_UdpServer_SetDetectAttempts = HPSocketDLL.HP_UdpServer_SetDetectAttempts if hasattr(HPSocketDLL, "HP_UdpServer_SetDetectAttempts") else None
if HP_UdpServer_SetDetectAttempts:
    HP_UdpServer_SetDetectAttempts.restype = None
    HP_UdpServer_SetDetectAttempts.argtypes = [HP_UdpServer, ctypes.c_uint]
#  设置监测包发送间隔（秒，0 不发送监测包）
# HPSOCKET_API void __stdcall HP_UdpServer_SetDetectInterval(HP_UdpServer pServer, DWORD dwDetectInterval);
HP_UdpServer_SetDetectInterval = HPSocketDLL.HP_UdpServer_SetDetectInterval if hasattr(HPSocketDLL, "HP_UdpServer_SetDetectInterval") else None
if HP_UdpServer_SetDetectInterval:
    HP_UdpServer_SetDetectInterval.restype = None
    HP_UdpServer_SetDetectInterval.argtypes = [HP_UdpServer, ctypes.c_uint]
#  获取心跳检查次数
# HPSOCKET_API DWORD __stdcall HP_UdpServer_GetDetectAttempts(HP_UdpServer pServer);
HP_UdpServer_GetDetectAttempts = HPSocketDLL.HP_UdpServer_GetDetectAttempts if hasattr(HPSocketDLL, "HP_UdpServer_GetDetectAttempts") else None
if HP_UdpServer_GetDetectAttempts:
    HP_UdpServer_GetDetectAttempts.restype = ctypes.c_uint
    HP_UdpServer_GetDetectAttempts.argtypes = [HP_UdpServer]
#  获取心跳检查间隔
# HPSOCKET_API DWORD __stdcall HP_UdpServer_GetDetectInterval(HP_UdpServer pServer);
HP_UdpServer_GetDetectInterval = HPSocketDLL.HP_UdpServer_GetDetectInterval if hasattr(HPSocketDLL, "HP_UdpServer_GetDetectInterval") else None
if HP_UdpServer_GetDetectInterval:
    HP_UdpServer_GetDetectInterval.restype = ctypes.c_uint
    HP_UdpServer_GetDetectInterval.argtypes = [HP_UdpServer]

# ************************************************************************
# **************************** Agent 操作方法 ****************************

#
# * 名称：启动通信组件
# * 描述：启动通信代理组件，启动完成后可开始连接远程服务器
# *
# * 参数：		lpszBindAddress	-- 绑定地址（默认：nullptr，绑定任意地址）
# *			bAsyncConnect	-- 是否采用异步 Connect
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败，可通过 HP_Agent_GetLastError() 获取错误代码
#
# HPSOCKET_API BOOL __stdcall HP_Agent_Start(HP_Agent pAgent, LPCTSTR lpszBindAddress, BOOL bAsyncConnect);
HP_Agent_Start = HPSocketDLL.HP_Agent_Start if hasattr(HPSocketDLL, "HP_Agent_Start") else None
if HP_Agent_Start:
    HP_Agent_Start.restype = ctypes.c_bool
    HP_Agent_Start.argtypes = [HP_Agent, ctypes.c_char_p, ctypes.c_bool]

#
# * 名称：关闭通信组件
# * 描述：关闭通信组件，关闭完成后断开所有连接并释放所有资源
# *
# * 参数：
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败，可通过 HP_Agent_GetLastError() 获取错误代码
#
# HPSOCKET_API BOOL __stdcall HP_Agent_Stop(HP_Agent pAgent);
HP_Agent_Stop = HPSocketDLL.HP_Agent_Stop if hasattr(HPSocketDLL, "HP_Agent_Stop") else None
if HP_Agent_Stop:
    HP_Agent_Stop.restype = ctypes.c_bool
    HP_Agent_Stop.argtypes = [HP_Agent]

#
# * 名称：连接服务器
# * 描述：连接服务器，连接成功后 IAgentListener 会接收到 OnConnect() / OnHandShake() 事件
# *
# * 参数：		lpszRemoteAddress	-- 服务端地址
# *			usPort				-- 服务端端口
# *			pdwConnID			-- 连接 ID（默认：nullptr，不获取连接 ID）
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败，可通过函数 SYS_GetLastError() 获取 Windows 错误代码
#
# HPSOCKET_API BOOL __stdcall HP_Agent_Connect(HP_Agent pAgent, LPCTSTR lpszRemoteAddress, USHORT usPort, HP_CONNID* pdwConnID);
HP_Agent_Connect = HPSocketDLL.HP_Agent_Connect if hasattr(HPSocketDLL, "HP_Agent_Connect") else None
if HP_Agent_Connect:
    HP_Agent_Connect.restype = ctypes.c_bool
    HP_Agent_Connect.argtypes = [HP_Agent, ctypes.c_char_p, ctypes.c_ushort, ctypes.POINTER(HP_CONNID)]

#
# * 名称：连接服务器
# * 描述：连接服务器，连接成功后 IAgentListener 会接收到 OnConnect() / OnHandShake() 事件
# *
# * 参数：		lpszRemoteAddress	-- 服务端地址
# *			usPort				-- 服务端端口
# *			pdwConnID			-- 连接 ID（默认：nullptr，不获取连接 ID）
# *			pExtra				-- 连接附加数据（默认：nullptr）
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败，可通过函数 SYS_GetLastError() 获取 Windows 错误代码
#
# HPSOCKET_API BOOL __stdcall HP_Agent_ConnectWithExtra(HP_Agent pAgent, LPCTSTR lpszRemoteAddress, USHORT usPort, HP_CONNID* pdwConnID, PVOID pExtra);
HP_Agent_ConnectWithExtra = HPSocketDLL.HP_Agent_ConnectWithExtra if hasattr(HPSocketDLL, "HP_Agent_ConnectWithExtra") else None
if HP_Agent_ConnectWithExtra:
    HP_Agent_ConnectWithExtra.restype = ctypes.c_bool
    HP_Agent_ConnectWithExtra.argtypes = [HP_Agent, ctypes.c_char_p, ctypes.c_ushort, ctypes.POINTER(HP_CONNID), PVOID]

#
# * 名称：发送数据
# * 描述：向指定连接发送数据
# *
# * 参数：		dwConnID	-- 连接 ID
# *			pBuffer		-- 发送缓冲区
# *			iLength		-- 发送缓冲区长度
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败，可通过 SYS_GetLastError() 获取 Windows 错误代码
#
# HPSOCKET_API BOOL __stdcall HP_Agent_Send(HP_Agent pAgent, HP_CONNID dwConnID, const BYTE* pBuffer, int iLength);
HP_Agent_Send = HPSocketDLL.HP_Agent_Send if hasattr(HPSocketDLL, "HP_Agent_Send") else None
if HP_Agent_Send:
    HP_Agent_Send.restype = ctypes.c_bool
    HP_Agent_Send.argtypes = [HP_Agent, HP_CONNID, ctypes.POINTER(ctypes.c_byte), ctypes.c_int]

#
# * 名称：发送数据
# * 描述：向指定连接发送数据
# *
# * 参数：		dwConnID	-- 连接 ID
# *			pBuffer		-- 发送缓冲区
# *			iLength		-- 发送缓冲区长度
# *			iOffset		-- 发送缓冲区指针偏移量
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败，可通过 SYS_GetLastError() 获取 Windows 错误代码
#
# HPSOCKET_API BOOL __stdcall HP_Agent_SendPart(HP_Agent pAgent, HP_CONNID dwConnID, const BYTE* pBuffer, int iLength, int iOffset);
HP_Agent_SendPart = HPSocketDLL.HP_Agent_SendPart if hasattr(HPSocketDLL, "HP_Agent_SendPart") else None
if HP_Agent_SendPart:
    HP_Agent_SendPart.restype = ctypes.c_bool
    HP_Agent_SendPart.argtypes = [HP_Agent, HP_CONNID, ctypes.POINTER(ctypes.c_byte), ctypes.c_int, ctypes.c_int]

#
# * 名称：发送多组数据
# * 描述：向指定连接发送多组数据
# *		TCP - 顺序发送所有数据包
# *		UDP - 把所有数据包组合成一个数据包发送（数据包的总长度不能大于设置的 UDP 包最大长度）
# *
# * 参数：		dwConnID	-- 连接 ID
# *			pBuffers	-- 发送缓冲区数组
# *			iCount		-- 发送缓冲区数目
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败，可通过 SYS_GetLastError() 获取 Windows 错误代码
#
# HPSOCKET_API BOOL __stdcall HP_Agent_SendPackets(HP_Agent pAgent, HP_CONNID dwConnID, const WSABUF pBuffers[], int iCount);
HP_Agent_SendPackets = HPSocketDLL.HP_Agent_SendPackets if hasattr(HPSocketDLL, "HP_Agent_SendPackets") else None
if HP_Agent_SendPackets:
    HP_Agent_SendPackets.restype = ctypes.c_bool
    HP_Agent_SendPackets.argtypes = [HP_Agent, HP_CONNID, ctypes.POINTER(WSABUF), ctypes.c_int]

#
# * 名称：暂停/恢复接收
# * 描述：暂停/恢复某个连接的数据接收工作
# *
# * 参数：		dwConnID	-- 连接 ID
# *			bPause		-- TRUE - 暂停, FALSE - 恢复
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败
#
# HPSOCKET_API BOOL __stdcall HP_Agent_PauseReceive(HP_Agent pAgent, HP_CONNID dwConnID, BOOL bPause);
HP_Agent_PauseReceive = HPSocketDLL.HP_Agent_PauseReceive if hasattr(HPSocketDLL, "HP_Agent_PauseReceive") else None
if HP_Agent_PauseReceive:
    HP_Agent_PauseReceive.restype = ctypes.c_bool
    HP_Agent_PauseReceive.argtypes = [HP_Agent, HP_CONNID, ctypes.c_bool]

#
# * 名称：断开连接
# * 描述：断开某个连接
# *
# * 参数：		dwConnID	-- 连接 ID
# *			bForce		-- 是否强制断开连接
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败
#
# HPSOCKET_API BOOL __stdcall HP_Agent_Disconnect(HP_Agent pAgent, HP_CONNID dwConnID, BOOL bForce);
HP_Agent_Disconnect = HPSocketDLL.HP_Agent_Disconnect if hasattr(HPSocketDLL, "HP_Agent_Disconnect") else None
if HP_Agent_Disconnect:
    HP_Agent_Disconnect.restype = ctypes.c_bool
    HP_Agent_Disconnect.argtypes = [HP_Agent, HP_CONNID, ctypes.c_bool]

#
# * 名称：断开超时连接
# * 描述：断开超过指定时长的连接
# *
# * 参数：		dwPeriod	-- 时长（毫秒）
# *			bForce		-- 是否强制断开连接
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败
#
# HPSOCKET_API BOOL __stdcall HP_Agent_DisconnectLongConnections(HP_Agent pAgent, DWORD dwPeriod, BOOL bForce);
HP_Agent_DisconnectLongConnections = HPSocketDLL.HP_Agent_DisconnectLongConnections if hasattr(HPSocketDLL, "HP_Agent_DisconnectLongConnections") else None
if HP_Agent_DisconnectLongConnections:
    HP_Agent_DisconnectLongConnections.restype = ctypes.c_bool
    HP_Agent_DisconnectLongConnections.argtypes = [HP_Agent, ctypes.c_uint, ctypes.c_bool]

#
# * 名称：断开静默连接
# * 描述：断开超过指定时长的静默连接
# *
# * 参数：		dwPeriod	-- 时长（毫秒）
# *			bForce		-- 是否强制断开连接
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败
#
# HPSOCKET_API BOOL __stdcall HP_Agent_DisconnectSilenceConnections(HP_Agent pAgent, DWORD dwPeriod, BOOL bForce);
HP_Agent_DisconnectSilenceConnections = HPSocketDLL.HP_Agent_DisconnectSilenceConnections if hasattr(HPSocketDLL, "HP_Agent_DisconnectSilenceConnections") else None
if HP_Agent_DisconnectSilenceConnections:
    HP_Agent_DisconnectSilenceConnections.restype = ctypes.c_bool
    HP_Agent_DisconnectSilenceConnections.argtypes = [HP_Agent, ctypes.c_uint, ctypes.c_bool]

# ****************************************************************************
# **************************** Agent 属性访问方法 ****************************

#
# * 名称：设置连接的附加数据
# * 描述：是否为连接绑定附加数据或者绑定什么样的数据，均由应用程序只身决定
# *
# * 参数：		dwConnID	-- 连接 ID
# *			pv			-- 数据
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败（无效的连接 ID）
#
# HPSOCKET_API BOOL __stdcall HP_Agent_SetConnectionExtra(HP_Agent pAgent, HP_CONNID dwConnID, PVOID pExtra);
HP_Agent_SetConnectionExtra = HPSocketDLL.HP_Agent_SetConnectionExtra if hasattr(HPSocketDLL, "HP_Agent_SetConnectionExtra") else None
if HP_Agent_SetConnectionExtra:
    HP_Agent_SetConnectionExtra.restype = ctypes.c_bool
    HP_Agent_SetConnectionExtra.argtypes = [HP_Agent, HP_CONNID, PVOID]

#
# * 名称：获取连接的附加数据
# * 描述：是否为连接绑定附加数据或者绑定什么样的数据，均由应用程序只身决定
# *
# * 参数：		dwConnID	-- 连接 ID
# *			ppv			-- 数据指针
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败（无效的连接 ID）
#
# HPSOCKET_API BOOL __stdcall HP_Agent_GetConnectionExtra(HP_Agent pAgent, HP_CONNID dwConnID, PVOID* ppExtra);
HP_Agent_GetConnectionExtra = HPSocketDLL.HP_Agent_GetConnectionExtra if hasattr(HPSocketDLL, "HP_Agent_GetConnectionExtra") else None
if HP_Agent_GetConnectionExtra:
    HP_Agent_GetConnectionExtra.restype = ctypes.c_bool
    HP_Agent_GetConnectionExtra.argtypes = [HP_Agent, HP_CONNID, ctypes.POINTER(PVOID)]

#  检测是否为安全连接（SSL/HTTPS）
# HPSOCKET_API BOOL __stdcall HP_Agent_IsSecure(HP_Agent pAgent);
HP_Agent_IsSecure = HPSocketDLL.HP_Agent_IsSecure if hasattr(HPSocketDLL, "HP_Agent_IsSecure") else None
if HP_Agent_IsSecure:
    HP_Agent_IsSecure.restype = ctypes.c_bool
    HP_Agent_IsSecure.argtypes = [HP_Agent]
#  检查通信组件是否已启动
# HPSOCKET_API BOOL __stdcall HP_Agent_HasStarted(HP_Agent pAgent);
HP_Agent_HasStarted = HPSocketDLL.HP_Agent_HasStarted if hasattr(HPSocketDLL, "HP_Agent_HasStarted") else None
if HP_Agent_HasStarted:
    HP_Agent_HasStarted.restype = ctypes.c_bool
    HP_Agent_HasStarted.argtypes = [HP_Agent]
#  查看通信组件当前状态
# HPSOCKET_API En_HP_ServiceState __stdcall HP_Agent_GetState(HP_Agent pAgent);
HP_Agent_GetState = HPSocketDLL.HP_Agent_GetState if hasattr(HPSocketDLL, "HP_Agent_GetState") else None
if HP_Agent_GetState:
    HP_Agent_GetState.restype = En_HP_ServiceState
    HP_Agent_GetState.argtypes = [HP_Agent]
#  获取连接数
# HPSOCKET_API DWORD __stdcall HP_Agent_GetConnectionCount(HP_Agent pAgent);
HP_Agent_GetConnectionCount = HPSocketDLL.HP_Agent_GetConnectionCount if hasattr(HPSocketDLL, "HP_Agent_GetConnectionCount") else None
if HP_Agent_GetConnectionCount:
    HP_Agent_GetConnectionCount.restype = ctypes.c_uint
    HP_Agent_GetConnectionCount.argtypes = [HP_Agent]
#  获取所有连接的 HP_CONNID
# HPSOCKET_API BOOL __stdcall HP_Agent_GetAllConnectionIDs(HP_Agent pAgent, HP_CONNID pIDs[], DWORD* pdwCount);
HP_Agent_GetAllConnectionIDs = HPSocketDLL.HP_Agent_GetAllConnectionIDs if hasattr(HPSocketDLL, "HP_Agent_GetAllConnectionIDs") else None
if HP_Agent_GetAllConnectionIDs:
    HP_Agent_GetAllConnectionIDs.restype = ctypes.c_bool
    HP_Agent_GetAllConnectionIDs.argtypes = [HP_Agent, ctypes.POINTER(HP_CONNID), ctypes.POINTER(ctypes.c_uint)]
#  获取某个连接时长（毫秒）
# HPSOCKET_API BOOL __stdcall HP_Agent_GetConnectPeriod(HP_Agent pAgent, HP_CONNID dwConnID, DWORD* pdwPeriod);
HP_Agent_GetConnectPeriod = HPSocketDLL.HP_Agent_GetConnectPeriod if hasattr(HPSocketDLL, "HP_Agent_GetConnectPeriod") else None
if HP_Agent_GetConnectPeriod:
    HP_Agent_GetConnectPeriod.restype = ctypes.c_bool
    HP_Agent_GetConnectPeriod.argtypes = [HP_Agent, HP_CONNID, ctypes.POINTER(ctypes.c_uint)]
#  获取某个连接静默时间（毫秒）
# HPSOCKET_API BOOL __stdcall HP_Agent_GetSilencePeriod(HP_Agent pAgent, HP_CONNID dwConnID, DWORD* pdwPeriod);
HP_Agent_GetSilencePeriod = HPSocketDLL.HP_Agent_GetSilencePeriod if hasattr(HPSocketDLL, "HP_Agent_GetSilencePeriod") else None
if HP_Agent_GetSilencePeriod:
    HP_Agent_GetSilencePeriod.restype = ctypes.c_bool
    HP_Agent_GetSilencePeriod.argtypes = [HP_Agent, HP_CONNID, ctypes.POINTER(ctypes.c_uint)]
#  获取某个连接的本地地址信息
# HPSOCKET_API BOOL __stdcall HP_Agent_GetLocalAddress(HP_Agent pAgent, HP_CONNID dwConnID, TCHAR lpszAddress[], int* piAddressLen, USHORT* pusPort);
HP_Agent_GetLocalAddress = HPSocketDLL.HP_Agent_GetLocalAddress if hasattr(HPSocketDLL, "HP_Agent_GetLocalAddress") else None
if HP_Agent_GetLocalAddress:
    HP_Agent_GetLocalAddress.restype = ctypes.c_bool
    HP_Agent_GetLocalAddress.argtypes = [HP_Agent, HP_CONNID, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_ushort)]
#  获取某个连接的远程地址信息
# HPSOCKET_API BOOL __stdcall HP_Agent_GetRemoteAddress(HP_Agent pAgent, HP_CONNID dwConnID, TCHAR lpszAddress[], int* piAddressLen, USHORT* pusPort);
HP_Agent_GetRemoteAddress = HPSocketDLL.HP_Agent_GetRemoteAddress if hasattr(HPSocketDLL, "HP_Agent_GetRemoteAddress") else None
if HP_Agent_GetRemoteAddress:
    HP_Agent_GetRemoteAddress.restype = ctypes.c_bool
    HP_Agent_GetRemoteAddress.argtypes = [HP_Agent, HP_CONNID, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_ushort)]
#  获取某个连接的远程主机信息
# HPSOCKET_API BOOL __stdcall HP_Agent_GetRemoteHost(HP_Agent pAgent, HP_CONNID dwConnID, TCHAR lpszHost[], int* piHostLen, USHORT* pusPort);
HP_Agent_GetRemoteHost = HPSocketDLL.HP_Agent_GetRemoteHost if hasattr(HPSocketDLL, "HP_Agent_GetRemoteHost") else None
if HP_Agent_GetRemoteHost:
    HP_Agent_GetRemoteHost.restype = ctypes.c_bool
    HP_Agent_GetRemoteHost.argtypes = [HP_Agent, HP_CONNID, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_ushort)]
#  获取最近一次失败操作的错误代码
# HPSOCKET_API En_HP_SocketError __stdcall HP_Agent_GetLastError(HP_Agent pAgent);
HP_Agent_GetLastError = HPSocketDLL.HP_Agent_GetLastError if hasattr(HPSocketDLL, "HP_Agent_GetLastError") else None
if HP_Agent_GetLastError:
    HP_Agent_GetLastError.restype = En_HP_SocketError
    HP_Agent_GetLastError.argtypes = [HP_Agent]
#  获取最近一次失败操作的错误描述
# HPSOCKET_API LPCTSTR __stdcall HP_Agent_GetLastErrorDesc(HP_Agent pAgent);
HP_Agent_GetLastErrorDesc = HPSocketDLL.HP_Agent_GetLastErrorDesc if hasattr(HPSocketDLL, "HP_Agent_GetLastErrorDesc") else None
if HP_Agent_GetLastErrorDesc:
    HP_Agent_GetLastErrorDesc.restype = ctypes.c_char_p
    HP_Agent_GetLastErrorDesc.argtypes = [HP_Agent]
#  获取连接中未发出数据的长度
# HPSOCKET_API BOOL __stdcall HP_Agent_GetPendingDataLength(HP_Agent pAgent, HP_CONNID dwConnID, int* piPending);
HP_Agent_GetPendingDataLength = HPSocketDLL.HP_Agent_GetPendingDataLength if hasattr(HPSocketDLL, "HP_Agent_GetPendingDataLength") else None
if HP_Agent_GetPendingDataLength:
    HP_Agent_GetPendingDataLength.restype = ctypes.c_bool
    HP_Agent_GetPendingDataLength.argtypes = [HP_Agent, HP_CONNID, ctypes.POINTER(ctypes.c_int)]
#  获取连接的数据接收状态
# HPSOCKET_API BOOL __stdcall HP_Agent_IsPauseReceive(HP_Agent pAgent, HP_CONNID dwConnID, BOOL* pbPaused);
HP_Agent_IsPauseReceive = HPSocketDLL.HP_Agent_IsPauseReceive if hasattr(HPSocketDLL, "HP_Agent_IsPauseReceive") else None
if HP_Agent_IsPauseReceive:
    HP_Agent_IsPauseReceive.restype = ctypes.c_bool
    HP_Agent_IsPauseReceive.argtypes = [HP_Agent, HP_CONNID, ctypes.POINTER(ctypes.c_bool)]

#  设置数据发送策略
# HPSOCKET_API void __stdcall HP_Agent_SetSendPolicy(HP_Agent pAgent, En_HP_SendPolicy enSendPolicy);
HP_Agent_SetSendPolicy = HPSocketDLL.HP_Agent_SetSendPolicy if hasattr(HPSocketDLL, "HP_Agent_SetSendPolicy") else None
if HP_Agent_SetSendPolicy:
    HP_Agent_SetSendPolicy.restype = None
    HP_Agent_SetSendPolicy.argtypes = [HP_Agent, En_HP_SendPolicy]
#  设置 Socket 缓存对象锁定时间（毫秒，在锁定期间该 Socket 缓存对象不能被获取使用）
# HPSOCKET_API void __stdcall HP_Agent_SetFreeSocketObjLockTime(HP_Agent pAgent, DWORD dwFreeSocketObjLockTime);
HP_Agent_SetFreeSocketObjLockTime = HPSocketDLL.HP_Agent_SetFreeSocketObjLockTime if hasattr(HPSocketDLL, "HP_Agent_SetFreeSocketObjLockTime") else None
if HP_Agent_SetFreeSocketObjLockTime:
    HP_Agent_SetFreeSocketObjLockTime.restype = None
    HP_Agent_SetFreeSocketObjLockTime.argtypes = [HP_Agent, ctypes.c_uint]
#  设置 Socket 缓存池大小（通常设置为平均并发连接数量的 1/3 - 1/2）
# HPSOCKET_API void __stdcall HP_Agent_SetFreeSocketObjPool(HP_Agent pAgent, DWORD dwFreeSocketObjPool);
HP_Agent_SetFreeSocketObjPool = HPSocketDLL.HP_Agent_SetFreeSocketObjPool if hasattr(HPSocketDLL, "HP_Agent_SetFreeSocketObjPool") else None
if HP_Agent_SetFreeSocketObjPool:
    HP_Agent_SetFreeSocketObjPool.restype = None
    HP_Agent_SetFreeSocketObjPool.argtypes = [HP_Agent, ctypes.c_uint]
#  设置内存块缓存池大小（通常设置为 Socket 缓存池大小的 2 - 3 倍）
# HPSOCKET_API void __stdcall HP_Agent_SetFreeBufferObjPool(HP_Agent pAgent, DWORD dwFreeBufferObjPool);
HP_Agent_SetFreeBufferObjPool = HPSocketDLL.HP_Agent_SetFreeBufferObjPool if hasattr(HPSocketDLL, "HP_Agent_SetFreeBufferObjPool") else None
if HP_Agent_SetFreeBufferObjPool:
    HP_Agent_SetFreeBufferObjPool.restype = None
    HP_Agent_SetFreeBufferObjPool.argtypes = [HP_Agent, ctypes.c_uint]
#  设置 Socket 缓存池回收阀值（通常设置为 Socket 缓存池大小的 3 倍）
# HPSOCKET_API void __stdcall HP_Agent_SetFreeSocketObjHold(HP_Agent pAgent, DWORD dwFreeSocketObjHold);
HP_Agent_SetFreeSocketObjHold = HPSocketDLL.HP_Agent_SetFreeSocketObjHold if hasattr(HPSocketDLL, "HP_Agent_SetFreeSocketObjHold") else None
if HP_Agent_SetFreeSocketObjHold:
    HP_Agent_SetFreeSocketObjHold.restype = None
    HP_Agent_SetFreeSocketObjHold.argtypes = [HP_Agent, ctypes.c_uint]
#  设置内存块缓存池回收阀值（通常设置为内存块缓存池大小的 3 倍）
# HPSOCKET_API void __stdcall HP_Agent_SetFreeBufferObjHold(HP_Agent pAgent, DWORD dwFreeBufferObjHold);
HP_Agent_SetFreeBufferObjHold = HPSocketDLL.HP_Agent_SetFreeBufferObjHold if hasattr(HPSocketDLL, "HP_Agent_SetFreeBufferObjHold") else None
if HP_Agent_SetFreeBufferObjHold:
    HP_Agent_SetFreeBufferObjHold.restype = None
    HP_Agent_SetFreeBufferObjHold.argtypes = [HP_Agent, ctypes.c_uint]
#  设置最大连接数（组件会根据设置值预分配内存，因此需要根据实际情况设置，不宜过大）
# HPSOCKET_API void __stdcall HP_Agent_SetMaxConnectionCount(HP_Agent pAgent, DWORD dwMaxConnectionCount);
HP_Agent_SetMaxConnectionCount = HPSocketDLL.HP_Agent_SetMaxConnectionCount if hasattr(HPSocketDLL, "HP_Agent_SetMaxConnectionCount") else None
if HP_Agent_SetMaxConnectionCount:
    HP_Agent_SetMaxConnectionCount.restype = None
    HP_Agent_SetMaxConnectionCount.argtypes = [HP_Agent, ctypes.c_uint]
#  设置工作线程数量（通常设置为 2 * CPU + 2）
# HPSOCKET_API void __stdcall HP_Agent_SetWorkerThreadCount(HP_Agent pAgent, DWORD dwWorkerThreadCount);
HP_Agent_SetWorkerThreadCount = HPSocketDLL.HP_Agent_SetWorkerThreadCount if hasattr(HPSocketDLL, "HP_Agent_SetWorkerThreadCount") else None
if HP_Agent_SetWorkerThreadCount:
    HP_Agent_SetWorkerThreadCount.restype = None
    HP_Agent_SetWorkerThreadCount.argtypes = [HP_Agent, ctypes.c_uint]
#  设置是否标记静默时间（设置为 TRUE 时 DisconnectSilenceConnections() 和 GetSilencePeriod() 才有效，默认：TRUE）
# HPSOCKET_API void __stdcall HP_Agent_SetMarkSilence(HP_Agent pAgent, BOOL bMarkSilence);
HP_Agent_SetMarkSilence = HPSocketDLL.HP_Agent_SetMarkSilence if hasattr(HPSocketDLL, "HP_Agent_SetMarkSilence") else None
if HP_Agent_SetMarkSilence:
    HP_Agent_SetMarkSilence.restype = None
    HP_Agent_SetMarkSilence.argtypes = [HP_Agent, ctypes.c_bool]

#  获取数据发送策略
# HPSOCKET_API En_HP_SendPolicy __stdcall HP_Agent_GetSendPolicy(HP_Agent pAgent);
HP_Agent_GetSendPolicy = HPSocketDLL.HP_Agent_GetSendPolicy if hasattr(HPSocketDLL, "HP_Agent_GetSendPolicy") else None
if HP_Agent_GetSendPolicy:
    HP_Agent_GetSendPolicy.restype = En_HP_SendPolicy
    HP_Agent_GetSendPolicy.argtypes = [HP_Agent]
#  获取 Socket 缓存对象锁定时间
# HPSOCKET_API DWORD __stdcall HP_Agent_GetFreeSocketObjLockTime(HP_Agent pAgent);
HP_Agent_GetFreeSocketObjLockTime = HPSocketDLL.HP_Agent_GetFreeSocketObjLockTime if hasattr(HPSocketDLL, "HP_Agent_GetFreeSocketObjLockTime") else None
if HP_Agent_GetFreeSocketObjLockTime:
    HP_Agent_GetFreeSocketObjLockTime.restype = ctypes.c_uint
    HP_Agent_GetFreeSocketObjLockTime.argtypes = [HP_Agent]
#  获取 Socket 缓存池大小
# HPSOCKET_API DWORD __stdcall HP_Agent_GetFreeSocketObjPool(HP_Agent pAgent);
HP_Agent_GetFreeSocketObjPool = HPSocketDLL.HP_Agent_GetFreeSocketObjPool if hasattr(HPSocketDLL, "HP_Agent_GetFreeSocketObjPool") else None
if HP_Agent_GetFreeSocketObjPool:
    HP_Agent_GetFreeSocketObjPool.restype = ctypes.c_uint
    HP_Agent_GetFreeSocketObjPool.argtypes = [HP_Agent]
#  获取内存块缓存池大小
# HPSOCKET_API DWORD __stdcall HP_Agent_GetFreeBufferObjPool(HP_Agent pAgent);
HP_Agent_GetFreeBufferObjPool = HPSocketDLL.HP_Agent_GetFreeBufferObjPool if hasattr(HPSocketDLL, "HP_Agent_GetFreeBufferObjPool") else None
if HP_Agent_GetFreeBufferObjPool:
    HP_Agent_GetFreeBufferObjPool.restype = ctypes.c_uint
    HP_Agent_GetFreeBufferObjPool.argtypes = [HP_Agent]
#  获取 Socket 缓存池回收阀值
# HPSOCKET_API DWORD __stdcall HP_Agent_GetFreeSocketObjHold(HP_Agent pAgent);
HP_Agent_GetFreeSocketObjHold = HPSocketDLL.HP_Agent_GetFreeSocketObjHold if hasattr(HPSocketDLL, "HP_Agent_GetFreeSocketObjHold") else None
if HP_Agent_GetFreeSocketObjHold:
    HP_Agent_GetFreeSocketObjHold.restype = ctypes.c_uint
    HP_Agent_GetFreeSocketObjHold.argtypes = [HP_Agent]
#  获取内存块缓存池回收阀值
# HPSOCKET_API DWORD __stdcall HP_Agent_GetFreeBufferObjHold(HP_Agent pAgent);
HP_Agent_GetFreeBufferObjHold = HPSocketDLL.HP_Agent_GetFreeBufferObjHold if hasattr(HPSocketDLL, "HP_Agent_GetFreeBufferObjHold") else None
if HP_Agent_GetFreeBufferObjHold:
    HP_Agent_GetFreeBufferObjHold.restype = ctypes.c_uint
    HP_Agent_GetFreeBufferObjHold.argtypes = [HP_Agent]
#  获取最大连接数
# HPSOCKET_API DWORD __stdcall HP_Agent_GetMaxConnectionCount(HP_Agent pAgent);
HP_Agent_GetMaxConnectionCount = HPSocketDLL.HP_Agent_GetMaxConnectionCount if hasattr(HPSocketDLL, "HP_Agent_GetMaxConnectionCount") else None
if HP_Agent_GetMaxConnectionCount:
    HP_Agent_GetMaxConnectionCount.restype = ctypes.c_uint
    HP_Agent_GetMaxConnectionCount.argtypes = [HP_Agent]
#  获取工作线程数量
# HPSOCKET_API DWORD __stdcall HP_Agent_GetWorkerThreadCount(HP_Agent pAgent);
HP_Agent_GetWorkerThreadCount = HPSocketDLL.HP_Agent_GetWorkerThreadCount if hasattr(HPSocketDLL, "HP_Agent_GetWorkerThreadCount") else None
if HP_Agent_GetWorkerThreadCount:
    HP_Agent_GetWorkerThreadCount.restype = ctypes.c_uint
    HP_Agent_GetWorkerThreadCount.argtypes = [HP_Agent]
#  检测是否标记静默时间
# HPSOCKET_API BOOL __stdcall HP_Agent_IsMarkSilence(HP_Agent pAgent);
HP_Agent_IsMarkSilence = HPSocketDLL.HP_Agent_IsMarkSilence if hasattr(HPSocketDLL, "HP_Agent_IsMarkSilence") else None
if HP_Agent_IsMarkSilence:
    HP_Agent_IsMarkSilence.restype = ctypes.c_bool
    HP_Agent_IsMarkSilence.argtypes = [HP_Agent]

# ********************************************************************************
# ****************************** TCP Agent 操作方法 ******************************

#
# * 名称：发送小文件
# * 描述：向指定连接发送 4096 KB 以下的小文件
# *
# * 参数：		dwConnID		-- 连接 ID
# *			lpszFileName	-- 文件路径
# *			pHead			-- 头部附加数据
# *			pTail			-- 尾部附加数据
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败，可通过 SYS_GetLastError() 获取 Windows 错误代码
#
# HPSOCKET_API BOOL __stdcall HP_TcpAgent_SendSmallFile(HP_Agent pAgent, HP_CONNID dwConnID, LPCTSTR lpszFileName, const LPWSABUF pHead, const LPWSABUF pTail);
HP_TcpAgent_SendSmallFile = HPSocketDLL.HP_TcpAgent_SendSmallFile if hasattr(HPSocketDLL, "HP_TcpAgent_SendSmallFile") else None
if HP_TcpAgent_SendSmallFile:
    HP_TcpAgent_SendSmallFile.restype = ctypes.c_bool
    HP_TcpAgent_SendSmallFile.argtypes = [HP_Agent, HP_CONNID, ctypes.c_char_p, LPWSABUF, LPWSABUF]

# ********************************************************************************
# **************************** TCP Agent 属性访问方法 ****************************

#  设置是否启用地址重用机制（默认：不启用）
# HPSOCKET_API void __stdcall HP_TcpAgent_SetReuseAddress(HP_TcpAgent pAgent, BOOL bReuseAddress);
HP_TcpAgent_SetReuseAddress = HPSocketDLL.HP_TcpAgent_SetReuseAddress if hasattr(HPSocketDLL, "HP_TcpAgent_SetReuseAddress") else None
if HP_TcpAgent_SetReuseAddress:
    HP_TcpAgent_SetReuseAddress.restype = None
    HP_TcpAgent_SetReuseAddress.argtypes = [HP_TcpAgent, ctypes.c_bool]
#  检测是否启用地址重用机制
# HPSOCKET_API BOOL __stdcall HP_TcpAgent_IsReuseAddress(HP_TcpAgent pAgent);
HP_TcpAgent_IsReuseAddress = HPSocketDLL.HP_TcpAgent_IsReuseAddress if hasattr(HPSocketDLL, "HP_TcpAgent_IsReuseAddress") else None
if HP_TcpAgent_IsReuseAddress:
    HP_TcpAgent_IsReuseAddress.restype = ctypes.c_bool
    HP_TcpAgent_IsReuseAddress.argtypes = [HP_TcpAgent]

#  设置通信数据缓冲区大小（根据平均通信数据包大小调整设置，通常设置为 1024 的倍数）
# HPSOCKET_API void __stdcall HP_TcpAgent_SetSocketBufferSize(HP_TcpAgent pAgent, DWORD dwSocketBufferSize);
HP_TcpAgent_SetSocketBufferSize = HPSocketDLL.HP_TcpAgent_SetSocketBufferSize if hasattr(HPSocketDLL, "HP_TcpAgent_SetSocketBufferSize") else None
if HP_TcpAgent_SetSocketBufferSize:
    HP_TcpAgent_SetSocketBufferSize.restype = None
    HP_TcpAgent_SetSocketBufferSize.argtypes = [HP_TcpAgent, ctypes.c_uint]
#  设置正常心跳包间隔（毫秒，0 则不发送心跳包，默认：30 * 1000）
# HPSOCKET_API void __stdcall HP_TcpAgent_SetKeepAliveTime(HP_TcpAgent pAgent, DWORD dwKeepAliveTime);
HP_TcpAgent_SetKeepAliveTime = HPSocketDLL.HP_TcpAgent_SetKeepAliveTime if hasattr(HPSocketDLL, "HP_TcpAgent_SetKeepAliveTime") else None
if HP_TcpAgent_SetKeepAliveTime:
    HP_TcpAgent_SetKeepAliveTime.restype = None
    HP_TcpAgent_SetKeepAliveTime.argtypes = [HP_TcpAgent, ctypes.c_uint]
#  设置异常心跳包间隔（毫秒，0 不发送心跳包，，默认：10 * 1000，如果超过若干次 [默认：WinXP 5 次, Win7 10 次] 检测不到心跳确认包则认为已断线）
# HPSOCKET_API void __stdcall HP_TcpAgent_SetKeepAliveInterval(HP_TcpAgent pAgent, DWORD dwKeepAliveInterval);
HP_TcpAgent_SetKeepAliveInterval = HPSocketDLL.HP_TcpAgent_SetKeepAliveInterval if hasattr(HPSocketDLL, "HP_TcpAgent_SetKeepAliveInterval") else None
if HP_TcpAgent_SetKeepAliveInterval:
    HP_TcpAgent_SetKeepAliveInterval.restype = None
    HP_TcpAgent_SetKeepAliveInterval.argtypes = [HP_TcpAgent, ctypes.c_uint]

#  获取通信数据缓冲区大小
# HPSOCKET_API DWORD __stdcall HP_TcpAgent_GetSocketBufferSize(HP_TcpAgent pAgent);
HP_TcpAgent_GetSocketBufferSize = HPSocketDLL.HP_TcpAgent_GetSocketBufferSize if hasattr(HPSocketDLL, "HP_TcpAgent_GetSocketBufferSize") else None
if HP_TcpAgent_GetSocketBufferSize:
    HP_TcpAgent_GetSocketBufferSize.restype = ctypes.c_uint
    HP_TcpAgent_GetSocketBufferSize.argtypes = [HP_TcpAgent]
#  获取正常心跳包间隔
# HPSOCKET_API DWORD __stdcall HP_TcpAgent_GetKeepAliveTime(HP_TcpAgent pAgent);
HP_TcpAgent_GetKeepAliveTime = HPSocketDLL.HP_TcpAgent_GetKeepAliveTime if hasattr(HPSocketDLL, "HP_TcpAgent_GetKeepAliveTime") else None
if HP_TcpAgent_GetKeepAliveTime:
    HP_TcpAgent_GetKeepAliveTime.restype = ctypes.c_uint
    HP_TcpAgent_GetKeepAliveTime.argtypes = [HP_TcpAgent]
#  获取异常心跳包间隔
# HPSOCKET_API DWORD __stdcall HP_TcpAgent_GetKeepAliveInterval(HP_TcpAgent pAgent);
HP_TcpAgent_GetKeepAliveInterval = HPSocketDLL.HP_TcpAgent_GetKeepAliveInterval if hasattr(HPSocketDLL, "HP_TcpAgent_GetKeepAliveInterval") else None
if HP_TcpAgent_GetKeepAliveInterval:
    HP_TcpAgent_GetKeepAliveInterval.restype = ctypes.c_uint
    HP_TcpAgent_GetKeepAliveInterval.argtypes = [HP_TcpAgent]

# ****************************************************************************
# **************************** Client 组件操作方法 ****************************

#
# * 名称：启动通信组件
# * 描述：启动客户端通信组件并连接服务端，启动完成后可开始收发数据
# *
# * 参数：		lpszRemoteAddress	-- 服务端地址
# *			usPort				-- 服务端端口
# *			bAsyncConnect		-- 是否采用异步 Connect
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败，可通过 HP_Client_GetLastError() 获取错误代码
#
# HPSOCKET_API BOOL __stdcall HP_Client_Start(HP_Client pClient, LPCTSTR lpszRemoteAddress, USHORT usPort, BOOL bAsyncConnect);
HP_Client_Start = HPSocketDLL.HP_Client_Start if hasattr(HPSocketDLL, "HP_Client_Start") else None
if HP_Client_Start:
    HP_Client_Start.restype = ctypes.c_bool
    HP_Client_Start.argtypes = [HP_Client, ctypes.c_char_p, ctypes.c_ushort, ctypes.c_bool]

#
# * 名称：启动通信组件（并指定绑定地址）
# * 描述：启动客户端通信组件并连接服务端，启动完成后可开始收发数据
# *
# * 参数：		lpszRemoteAddress	-- 服务端地址
# *			usPort				-- 服务端端口
# *			bAsyncConnect		-- 是否采用异步 Connect
# *			lpszBindAddress		-- 绑定地址（默认：nullptr，TcpClient/UdpClient -> 不执行绑定操作，UdpCast 绑定 -> 任意地址）
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败，可通过 HP_Client_GetLastError() 获取错误代码
#
# HPSOCKET_API BOOL __stdcall HP_Client_StartWithBindAddress(HP_Client pClient, LPCTSTR lpszRemoteAddress, USHORT usPort, BOOL bAsyncConnect, LPCTSTR lpszBindAddress);
HP_Client_StartWithBindAddress = HPSocketDLL.HP_Client_StartWithBindAddress if hasattr(HPSocketDLL, "HP_Client_StartWithBindAddress") else None
if HP_Client_StartWithBindAddress:
    HP_Client_StartWithBindAddress.restype = ctypes.c_bool
    HP_Client_StartWithBindAddress.argtypes = [HP_Client, ctypes.c_char_p, ctypes.c_ushort, ctypes.c_bool, ctypes.c_char_p]

#
# * 名称：关闭通信组件
# * 描述：关闭客户端通信组件，关闭完成后断开与服务端的连接并释放所有资源
# *
# * 参数：
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败，可通过 HP_Client_GetLastError() 获取错误代码
#
# HPSOCKET_API BOOL __stdcall HP_Client_Stop(HP_Client pClient);
HP_Client_Stop = HPSocketDLL.HP_Client_Stop if hasattr(HPSocketDLL, "HP_Client_Stop") else None
if HP_Client_Stop:
    HP_Client_Stop.restype = ctypes.c_bool
    HP_Client_Stop.argtypes = [HP_Client]

#
# * 名称：发送数据
# * 描述：向服务端发送数据
# *
# * 参数：		pBuffer		-- 发送缓冲区
# *			iLength		-- 发送缓冲区长度
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败，可通过 SYS_GetLastError() 获取 Windows 错误代码
#
# HPSOCKET_API BOOL __stdcall HP_Client_Send(HP_Client pClient, const BYTE* pBuffer, int iLength);
HP_Client_Send = HPSocketDLL.HP_Client_Send if hasattr(HPSocketDLL, "HP_Client_Send") else None
if HP_Client_Send:
    HP_Client_Send.restype = ctypes.c_bool
    HP_Client_Send.argtypes = [HP_Client, ctypes.POINTER(ctypes.c_byte), ctypes.c_int]

#
# * 名称：发送数据
# * 描述：向服务端发送数据
# *
# * 参数：		pBuffer		-- 发送缓冲区
# *			iLength		-- 发送缓冲区长度
# *			iOffset		-- 发送缓冲区指针偏移量
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败，可通过 SYS_GetLastError() 获取 Windows 错误代码
#
# HPSOCKET_API BOOL __stdcall HP_Client_SendPart(HP_Client pClient, const BYTE* pBuffer, int iLength, int iOffset);
HP_Client_SendPart = HPSocketDLL.HP_Client_SendPart if hasattr(HPSocketDLL, "HP_Client_SendPart") else None
if HP_Client_SendPart:
    HP_Client_SendPart.restype = ctypes.c_bool
    HP_Client_SendPart.argtypes = [HP_Client, ctypes.POINTER(ctypes.c_byte), ctypes.c_int, ctypes.c_int]

#
# * 名称：发送多组数据
# * 描述：向服务端发送多组数据
# *		TCP - 顺序发送所有数据包
# *		UDP - 把所有数据包组合成一个数据包发送（数据包的总长度不能大于设置的 UDP 包最大长度）
# *
# * 参数：		pBuffers	-- 发送缓冲区数组
# *			iCount		-- 发送缓冲区数目
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败，可通过 SYS_GetLastError() 获取 Windows 错误代码
#
# HPSOCKET_API BOOL __stdcall HP_Client_SendPackets(HP_Client pClient, const WSABUF pBuffers[], int iCount);
HP_Client_SendPackets = HPSocketDLL.HP_Client_SendPackets if hasattr(HPSocketDLL, "HP_Client_SendPackets") else None
if HP_Client_SendPackets:
    HP_Client_SendPackets.restype = ctypes.c_bool
    HP_Client_SendPackets.argtypes = [HP_Client, ctypes.POINTER(WSABUF), ctypes.c_int]

#
# * 名称：暂停/恢复接收
# * 描述：暂停/恢复某个连接的数据接收工作
# *
# *			bPause	-- TRUE - 暂停, FALSE - 恢复
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败
#
# HPSOCKET_API BOOL __stdcall HP_Client_PauseReceive(HP_Client pClient, BOOL bPause);
HP_Client_PauseReceive = HPSocketDLL.HP_Client_PauseReceive if hasattr(HPSocketDLL, "HP_Client_PauseReceive") else None
if HP_Client_PauseReceive:
    HP_Client_PauseReceive.restype = ctypes.c_bool
    HP_Client_PauseReceive.argtypes = [HP_Client, ctypes.c_bool]

# ****************************************************************************
# **************************** Client 属性访问方法 ****************************

#  设置连接的附加数据
# HPSOCKET_API void __stdcall HP_Client_SetExtra(HP_Client pClient, PVOID pExtra);
HP_Client_SetExtra = HPSocketDLL.HP_Client_SetExtra if hasattr(HPSocketDLL, "HP_Client_SetExtra") else None
if HP_Client_SetExtra:
    HP_Client_SetExtra.restype = None
    HP_Client_SetExtra.argtypes = [HP_Client, PVOID]
#  获取连接的附加数据
# HPSOCKET_API PVOID __stdcall HP_Client_GetExtra(HP_Client pClient);
HP_Client_GetExtra = HPSocketDLL.HP_Client_GetExtra if hasattr(HPSocketDLL, "HP_Client_GetExtra") else None
if HP_Client_GetExtra:
    HP_Client_GetExtra.restype = PVOID
    HP_Client_GetExtra.argtypes = [HP_Client]

#  检测是否为安全连接（SSL/HTTPS）
# HPSOCKET_API BOOL __stdcall HP_Client_IsSecure(HP_Client pClient);
HP_Client_IsSecure = HPSocketDLL.HP_Client_IsSecure if hasattr(HPSocketDLL, "HP_Client_IsSecure") else None
if HP_Client_IsSecure:
    HP_Client_IsSecure.restype = ctypes.c_bool
    HP_Client_IsSecure.argtypes = [HP_Client]
#  检查通信组件是否已启动
# HPSOCKET_API BOOL __stdcall HP_Client_HasStarted(HP_Client pClient);
HP_Client_HasStarted = HPSocketDLL.HP_Client_HasStarted if hasattr(HPSocketDLL, "HP_Client_HasStarted") else None
if HP_Client_HasStarted:
    HP_Client_HasStarted.restype = ctypes.c_bool
    HP_Client_HasStarted.argtypes = [HP_Client]
#  查看通信组件当前状态
# HPSOCKET_API En_HP_ServiceState	__stdcall HP_Client_GetState(HP_Client pClient);
HP_Client_GetState = HPSocketDLL.HP_Client_GetState if hasattr(HPSocketDLL, "HP_Client_GetState") else None
if HP_Client_GetState:
    HP_Client_GetState.restype = En_HP_ServiceState
    HP_Client_GetState.argtypes = [HP_Client]
#  获取最近一次失败操作的错误代码
# HPSOCKET_API En_HP_SocketError	__stdcall HP_Client_GetLastError(HP_Client pClient);
HP_Client_GetLastError = HPSocketDLL.HP_Client_GetLastError if hasattr(HPSocketDLL, "HP_Client_GetLastError") else None
if HP_Client_GetLastError:
    HP_Client_GetLastError.restype = En_HP_SocketError
    HP_Client_GetLastError.argtypes = [HP_Client]
#  获取最近一次失败操作的错误描述
# HPSOCKET_API LPCTSTR __stdcall HP_Client_GetLastErrorDesc(HP_Client pClient);
HP_Client_GetLastErrorDesc = HPSocketDLL.HP_Client_GetLastErrorDesc if hasattr(HPSocketDLL, "HP_Client_GetLastErrorDesc") else None
if HP_Client_GetLastErrorDesc:
    HP_Client_GetLastErrorDesc.restype = ctypes.c_char_p
    HP_Client_GetLastErrorDesc.argtypes = [HP_Client]
#  获取该组件对象的连接 ID
# HPSOCKET_API HP_CONNID __stdcall HP_Client_GetConnectionID(HP_Client pClient);
HP_Client_GetConnectionID = HPSocketDLL.HP_Client_GetConnectionID if hasattr(HPSocketDLL, "HP_Client_GetConnectionID") else None
if HP_Client_GetConnectionID:
    HP_Client_GetConnectionID.restype = HP_CONNID
    HP_Client_GetConnectionID.argtypes = [HP_Client]
#  获取 Client Socket 的地址信息
# HPSOCKET_API BOOL __stdcall HP_Client_GetLocalAddress(HP_Client pClient, TCHAR lpszAddress[], int* piAddressLen, USHORT* pusPort);
HP_Client_GetLocalAddress = HPSocketDLL.HP_Client_GetLocalAddress if hasattr(HPSocketDLL, "HP_Client_GetLocalAddress") else None
if HP_Client_GetLocalAddress:
    HP_Client_GetLocalAddress.restype = ctypes.c_bool
    HP_Client_GetLocalAddress.argtypes = [HP_Client, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_ushort)]
#  获取连接的远程主机信息
# HPSOCKET_API BOOL __stdcall HP_Client_GetRemoteHost(HP_Client pClient, TCHAR lpszHost[], int* piHostLen, USHORT* pusPort);
HP_Client_GetRemoteHost = HPSocketDLL.HP_Client_GetRemoteHost if hasattr(HPSocketDLL, "HP_Client_GetRemoteHost") else None
if HP_Client_GetRemoteHost:
    HP_Client_GetRemoteHost.restype = ctypes.c_bool
    HP_Client_GetRemoteHost.argtypes = [HP_Client, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_ushort)]
#  获取连接中未发出数据的长度
# HPSOCKET_API BOOL __stdcall HP_Client_GetPendingDataLength(HP_Client pClient, int* piPending);
HP_Client_GetPendingDataLength = HPSocketDLL.HP_Client_GetPendingDataLength if hasattr(HPSocketDLL, "HP_Client_GetPendingDataLength") else None
if HP_Client_GetPendingDataLength:
    HP_Client_GetPendingDataLength.restype = ctypes.c_bool
    HP_Client_GetPendingDataLength.argtypes = [HP_Client, ctypes.POINTER(ctypes.c_int)]
#  获取连接的数据接收状态
# HPSOCKET_API BOOL __stdcall HP_Client_IsPauseReceive(HP_Client pClient, BOOL* pbPaused);
HP_Client_IsPauseReceive = HPSocketDLL.HP_Client_IsPauseReceive if hasattr(HPSocketDLL, "HP_Client_IsPauseReceive") else None
if HP_Client_IsPauseReceive:
    HP_Client_IsPauseReceive.restype = ctypes.c_bool
    HP_Client_IsPauseReceive.argtypes = [HP_Client, ctypes.POINTER(ctypes.c_bool)]
#  设置内存块缓存池大小（通常设置为 -> PUSH 模型：5 - 10；PULL 模型：10 - 20 ）
# HPSOCKET_API void __stdcall HP_Client_SetFreeBufferPoolSize(HP_Client pClient, DWORD dwFreeBufferPoolSize);
HP_Client_SetFreeBufferPoolSize = HPSocketDLL.HP_Client_SetFreeBufferPoolSize if hasattr(HPSocketDLL, "HP_Client_SetFreeBufferPoolSize") else None
if HP_Client_SetFreeBufferPoolSize:
    HP_Client_SetFreeBufferPoolSize.restype = None
    HP_Client_SetFreeBufferPoolSize.argtypes = [HP_Client, ctypes.c_uint]
#  设置内存块缓存池回收阀值（通常设置为内存块缓存池大小的 3 倍）
# HPSOCKET_API void __stdcall HP_Client_SetFreeBufferPoolHold(HP_Client pClient, DWORD dwFreeBufferPoolHold);
HP_Client_SetFreeBufferPoolHold = HPSocketDLL.HP_Client_SetFreeBufferPoolHold if hasattr(HPSocketDLL, "HP_Client_SetFreeBufferPoolHold") else None
if HP_Client_SetFreeBufferPoolHold:
    HP_Client_SetFreeBufferPoolHold.restype = None
    HP_Client_SetFreeBufferPoolHold.argtypes = [HP_Client, ctypes.c_uint]
#  获取内存块缓存池大小
# HPSOCKET_API DWORD __stdcall HP_Client_GetFreeBufferPoolSize(HP_Client pClient);
HP_Client_GetFreeBufferPoolSize = HPSocketDLL.HP_Client_GetFreeBufferPoolSize if hasattr(HPSocketDLL, "HP_Client_GetFreeBufferPoolSize") else None
if HP_Client_GetFreeBufferPoolSize:
    HP_Client_GetFreeBufferPoolSize.restype = ctypes.c_uint
    HP_Client_GetFreeBufferPoolSize.argtypes = [HP_Client]
#  获取内存块缓存池回收阀值
# HPSOCKET_API DWORD __stdcall HP_Client_GetFreeBufferPoolHold(HP_Client pClient);
HP_Client_GetFreeBufferPoolHold = HPSocketDLL.HP_Client_GetFreeBufferPoolHold if hasattr(HPSocketDLL, "HP_Client_GetFreeBufferPoolHold") else None
if HP_Client_GetFreeBufferPoolHold:
    HP_Client_GetFreeBufferPoolHold.restype = ctypes.c_uint
    HP_Client_GetFreeBufferPoolHold.argtypes = [HP_Client]

# ********************************************************************************
# ****************************** TCP Client 操作方法 ******************************

#
# * 名称：发送小文件
# * 描述：向服务端发送 4096 KB 以下的小文件
# *
# * 参数：		lpszFileName	-- 文件路径
# *			pHead			-- 头部附加数据
# *			pTail			-- 尾部附加数据
# * 返回值：	TRUE	-- 成功
# *			FALSE	-- 失败，可通过 SYS_GetLastError() 获取 Windows 错误代码
#
# HPSOCKET_API BOOL __stdcall HP_TcpClient_SendSmallFile(HP_Client pClient, LPCTSTR lpszFileName, const LPWSABUF pHead, const LPWSABUF pTail);
HP_TcpClient_SendSmallFile = HPSocketDLL.HP_TcpClient_SendSmallFile if hasattr(HPSocketDLL, "HP_TcpClient_SendSmallFile") else None
if HP_TcpClient_SendSmallFile:
    HP_TcpClient_SendSmallFile.restype = ctypes.c_bool
    HP_TcpClient_SendSmallFile.argtypes = [HP_Client, ctypes.c_char_p, LPWSABUF, LPWSABUF]

# ********************************************************************************
# **************************** TCP Client 属性访问方法 ****************************

#  设置通信数据缓冲区大小（根据平均通信数据包大小调整设置，通常设置为：(N * 1024) - sizeof(TBufferObj)）
# HPSOCKET_API void __stdcall HP_TcpClient_SetSocketBufferSize(HP_TcpClient pClient, DWORD dwSocketBufferSize);
HP_TcpClient_SetSocketBufferSize = HPSocketDLL.HP_TcpClient_SetSocketBufferSize if hasattr(HPSocketDLL, "HP_TcpClient_SetSocketBufferSize") else None
if HP_TcpClient_SetSocketBufferSize:
    HP_TcpClient_SetSocketBufferSize.restype = None
    HP_TcpClient_SetSocketBufferSize.argtypes = [HP_TcpClient, ctypes.c_uint]
#  设置正常心跳包间隔（毫秒，0 则不发送心跳包，默认：30 * 1000）
# HPSOCKET_API void __stdcall HP_TcpClient_SetKeepAliveTime(HP_TcpClient pClient, DWORD dwKeepAliveTime);
HP_TcpClient_SetKeepAliveTime = HPSocketDLL.HP_TcpClient_SetKeepAliveTime if hasattr(HPSocketDLL, "HP_TcpClient_SetKeepAliveTime") else None
if HP_TcpClient_SetKeepAliveTime:
    HP_TcpClient_SetKeepAliveTime.restype = None
    HP_TcpClient_SetKeepAliveTime.argtypes = [HP_TcpClient, ctypes.c_uint]
#  设置异常心跳包间隔（毫秒，0 不发送心跳包，，默认：10 * 1000，如果超过若干次 [默认：WinXP 5 次, Win7 10 次] 检测不到心跳确认包则认为已断线）
# HPSOCKET_API void __stdcall HP_TcpClient_SetKeepAliveInterval(HP_TcpClient pClient, DWORD dwKeepAliveInterval);
HP_TcpClient_SetKeepAliveInterval = HPSocketDLL.HP_TcpClient_SetKeepAliveInterval if hasattr(HPSocketDLL, "HP_TcpClient_SetKeepAliveInterval") else None
if HP_TcpClient_SetKeepAliveInterval:
    HP_TcpClient_SetKeepAliveInterval.restype = None
    HP_TcpClient_SetKeepAliveInterval.argtypes = [HP_TcpClient, ctypes.c_uint]

#  获取通信数据缓冲区大小
# HPSOCKET_API DWORD __stdcall HP_TcpClient_GetSocketBufferSize(HP_TcpClient pClient);
HP_TcpClient_GetSocketBufferSize = HPSocketDLL.HP_TcpClient_GetSocketBufferSize if hasattr(HPSocketDLL, "HP_TcpClient_GetSocketBufferSize") else None
if HP_TcpClient_GetSocketBufferSize:
    HP_TcpClient_GetSocketBufferSize.restype = ctypes.c_uint
    HP_TcpClient_GetSocketBufferSize.argtypes = [HP_TcpClient]
#  获取正常心跳包间隔
# HPSOCKET_API DWORD __stdcall HP_TcpClient_GetKeepAliveTime(HP_TcpClient pClient);
HP_TcpClient_GetKeepAliveTime = HPSocketDLL.HP_TcpClient_GetKeepAliveTime if hasattr(HPSocketDLL, "HP_TcpClient_GetKeepAliveTime") else None
if HP_TcpClient_GetKeepAliveTime:
    HP_TcpClient_GetKeepAliveTime.restype = ctypes.c_uint
    HP_TcpClient_GetKeepAliveTime.argtypes = [HP_TcpClient]
#  获取异常心跳包间隔
# HPSOCKET_API DWORD __stdcall HP_TcpClient_GetKeepAliveInterval(HP_TcpClient pClient);
HP_TcpClient_GetKeepAliveInterval = HPSocketDLL.HP_TcpClient_GetKeepAliveInterval if hasattr(HPSocketDLL, "HP_TcpClient_GetKeepAliveInterval") else None
if HP_TcpClient_GetKeepAliveInterval:
    HP_TcpClient_GetKeepAliveInterval.restype = ctypes.c_uint
    HP_TcpClient_GetKeepAliveInterval.argtypes = [HP_TcpClient]

# ********************************************************************************
# **************************** UDP Client 属性访问方法 ****************************

#  设置数据报文最大长度（建议在局域网环境下不超过 1472 字节，在广域网环境下不超过 548 字节）
# HPSOCKET_API void __stdcall HP_UdpClient_SetMaxDatagramSize(HP_UdpClient pClient, DWORD dwMaxDatagramSize);
HP_UdpClient_SetMaxDatagramSize = HPSocketDLL.HP_UdpClient_SetMaxDatagramSize if hasattr(HPSocketDLL, "HP_UdpClient_SetMaxDatagramSize") else None
if HP_UdpClient_SetMaxDatagramSize:
    HP_UdpClient_SetMaxDatagramSize.restype = None
    HP_UdpClient_SetMaxDatagramSize.argtypes = [HP_UdpClient, ctypes.c_uint]
#  获取数据报文最大长度
# HPSOCKET_API DWORD __stdcall HP_UdpClient_GetMaxDatagramSize(HP_UdpClient pClient);
HP_UdpClient_GetMaxDatagramSize = HPSocketDLL.HP_UdpClient_GetMaxDatagramSize if hasattr(HPSocketDLL, "HP_UdpClient_GetMaxDatagramSize") else None
if HP_UdpClient_GetMaxDatagramSize:
    HP_UdpClient_GetMaxDatagramSize.restype = ctypes.c_uint
    HP_UdpClient_GetMaxDatagramSize.argtypes = [HP_UdpClient]

#  设置监测包尝试次数（0 则不发送监测跳包，如果超过最大尝试次数则认为已断线）
# HPSOCKET_API void __stdcall HP_UdpClient_SetDetectAttempts(HP_UdpClient pClient, DWORD dwDetectAttempts);
HP_UdpClient_SetDetectAttempts = HPSocketDLL.HP_UdpClient_SetDetectAttempts if hasattr(HPSocketDLL, "HP_UdpClient_SetDetectAttempts") else None
if HP_UdpClient_SetDetectAttempts:
    HP_UdpClient_SetDetectAttempts.restype = None
    HP_UdpClient_SetDetectAttempts.argtypes = [HP_UdpClient, ctypes.c_uint]
#  设置监测包发送间隔（秒，0 不发送监测包）
# HPSOCKET_API void __stdcall HP_UdpClient_SetDetectInterval(HP_UdpClient pClient, DWORD dwDetectInterval);
HP_UdpClient_SetDetectInterval = HPSocketDLL.HP_UdpClient_SetDetectInterval if hasattr(HPSocketDLL, "HP_UdpClient_SetDetectInterval") else None
if HP_UdpClient_SetDetectInterval:
    HP_UdpClient_SetDetectInterval.restype = None
    HP_UdpClient_SetDetectInterval.argtypes = [HP_UdpClient, ctypes.c_uint]
#  获取心跳检查次数
# HPSOCKET_API DWORD __stdcall HP_UdpClient_GetDetectAttempts(HP_UdpClient pClient);
HP_UdpClient_GetDetectAttempts = HPSocketDLL.HP_UdpClient_GetDetectAttempts if hasattr(HPSocketDLL, "HP_UdpClient_GetDetectAttempts") else None
if HP_UdpClient_GetDetectAttempts:
    HP_UdpClient_GetDetectAttempts.restype = ctypes.c_uint
    HP_UdpClient_GetDetectAttempts.argtypes = [HP_UdpClient]
#  获取心跳检查间隔
# HPSOCKET_API DWORD __stdcall HP_UdpClient_GetDetectInterval(HP_UdpClient pClient);
HP_UdpClient_GetDetectInterval = HPSocketDLL.HP_UdpClient_GetDetectInterval if hasattr(HPSocketDLL, "HP_UdpClient_GetDetectInterval") else None
if HP_UdpClient_GetDetectInterval:
    HP_UdpClient_GetDetectInterval.restype = ctypes.c_uint
    HP_UdpClient_GetDetectInterval.argtypes = [HP_UdpClient]

# ********************************************************************************
# ***************************** UDP Cast 属性访问方法 *****************************

#  设置数据报文最大长度（建议在局域网环境下不超过 1472 字节，在广域网环境下不超过 548 字节）
# HPSOCKET_API void __stdcall HP_UdpCast_SetMaxDatagramSize(HP_UdpCast pCast, DWORD dwMaxDatagramSize);
HP_UdpCast_SetMaxDatagramSize = HPSocketDLL.HP_UdpCast_SetMaxDatagramSize if hasattr(HPSocketDLL, "HP_UdpCast_SetMaxDatagramSize") else None
if HP_UdpCast_SetMaxDatagramSize:
    HP_UdpCast_SetMaxDatagramSize.restype = None
    HP_UdpCast_SetMaxDatagramSize.argtypes = [HP_UdpCast, ctypes.c_uint]
#  获取数据报文最大长度
# HPSOCKET_API DWORD __stdcall HP_UdpCast_GetMaxDatagramSize(HP_UdpCast pCast);
HP_UdpCast_GetMaxDatagramSize = HPSocketDLL.HP_UdpCast_GetMaxDatagramSize if hasattr(HPSocketDLL, "HP_UdpCast_GetMaxDatagramSize") else None
if HP_UdpCast_GetMaxDatagramSize:
    HP_UdpCast_GetMaxDatagramSize.restype = ctypes.c_uint
    HP_UdpCast_GetMaxDatagramSize.argtypes = [HP_UdpCast]
#  获取当前数据报的远程地址信息（通常在 OnReceive 事件中调用）
# HPSOCKET_API BOOL __stdcall HP_UdpCast_GetRemoteAddress(HP_UdpCast pCast, TCHAR lpszAddress[], int* piAddressLen, USHORT* pusPort);
HP_UdpCast_GetRemoteAddress = HPSocketDLL.HP_UdpCast_GetRemoteAddress if hasattr(HPSocketDLL, "HP_UdpCast_GetRemoteAddress") else None
if HP_UdpCast_GetRemoteAddress:
    HP_UdpCast_GetRemoteAddress.restype = ctypes.c_bool
    HP_UdpCast_GetRemoteAddress.argtypes = [HP_UdpCast, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_ushort)]
#  设置是否启用地址重用机制（默认：不启用）
# HPSOCKET_API void __stdcall HP_UdpCast_SetReuseAddress(HP_UdpCast pCast, BOOL bReuseAddress);
HP_UdpCast_SetReuseAddress = HPSocketDLL.HP_UdpCast_SetReuseAddress if hasattr(HPSocketDLL, "HP_UdpCast_SetReuseAddress") else None
if HP_UdpCast_SetReuseAddress:
    HP_UdpCast_SetReuseAddress.restype = None
    HP_UdpCast_SetReuseAddress.argtypes = [HP_UdpCast, ctypes.c_bool]
#  检测是否启用地址重用机制
# HPSOCKET_API BOOL __stdcall HP_UdpCast_IsReuseAddress(HP_UdpCast pCast);
HP_UdpCast_IsReuseAddress = HPSocketDLL.HP_UdpCast_IsReuseAddress if hasattr(HPSocketDLL, "HP_UdpCast_IsReuseAddress") else None
if HP_UdpCast_IsReuseAddress:
    HP_UdpCast_IsReuseAddress.restype = ctypes.c_bool
    HP_UdpCast_IsReuseAddress.argtypes = [HP_UdpCast]
#  设置传播模式（组播或广播）
# HPSOCKET_API void __stdcall HP_UdpCast_SetCastMode(HP_UdpCast pCast, En_HP_CastMode enCastMode);
HP_UdpCast_SetCastMode = HPSocketDLL.HP_UdpCast_SetCastMode if hasattr(HPSocketDLL, "HP_UdpCast_SetCastMode") else None
if HP_UdpCast_SetCastMode:
    HP_UdpCast_SetCastMode.restype = None
    HP_UdpCast_SetCastMode.argtypes = [HP_UdpCast, En_HP_CastMode]
#  获取传播模式
# HPSOCKET_API En_HP_CastMode __stdcall HP_UdpCast_GetCastMode(HP_UdpCast pCast);
HP_UdpCast_GetCastMode = HPSocketDLL.HP_UdpCast_GetCastMode if hasattr(HPSocketDLL, "HP_UdpCast_GetCastMode") else None
if HP_UdpCast_GetCastMode:
    HP_UdpCast_GetCastMode.restype = En_HP_CastMode
    HP_UdpCast_GetCastMode.argtypes = [HP_UdpCast]
#  设置组播报文的 TTL（0 - 255）
# HPSOCKET_API void __stdcall HP_UdpCast_SetMultiCastTtl(HP_UdpCast pCast, int iMCTtl);
HP_UdpCast_SetMultiCastTtl = HPSocketDLL.HP_UdpCast_SetMultiCastTtl if hasattr(HPSocketDLL, "HP_UdpCast_SetMultiCastTtl") else None
if HP_UdpCast_SetMultiCastTtl:
    HP_UdpCast_SetMultiCastTtl.restype = None
    HP_UdpCast_SetMultiCastTtl.argtypes = [HP_UdpCast, ctypes.c_int]
#  获取组播报文的 TTL
# HPSOCKET_API int __stdcall HP_UdpCast_GetMultiCastTtl(HP_UdpCast pCast);
HP_UdpCast_GetMultiCastTtl = HPSocketDLL.HP_UdpCast_GetMultiCastTtl if hasattr(HPSocketDLL, "HP_UdpCast_GetMultiCastTtl") else None
if HP_UdpCast_GetMultiCastTtl:
    HP_UdpCast_GetMultiCastTtl.restype = ctypes.c_int
    HP_UdpCast_GetMultiCastTtl.argtypes = [HP_UdpCast]
#  设置是否启用组播环路（TRUE or FALSE）
# HPSOCKET_API void __stdcall HP_UdpCast_SetMultiCastLoop(HP_UdpCast pCast, BOOL bMCLoop);
HP_UdpCast_SetMultiCastLoop = HPSocketDLL.HP_UdpCast_SetMultiCastLoop if hasattr(HPSocketDLL, "HP_UdpCast_SetMultiCastLoop") else None
if HP_UdpCast_SetMultiCastLoop:
    HP_UdpCast_SetMultiCastLoop.restype = None
    HP_UdpCast_SetMultiCastLoop.argtypes = [HP_UdpCast, ctypes.c_bool]
#  检测是否启用组播环路
# HPSOCKET_API BOOL __stdcall HP_UdpCast_IsMultiCastLoop(HP_UdpCast pCast);
HP_UdpCast_IsMultiCastLoop = HPSocketDLL.HP_UdpCast_IsMultiCastLoop if hasattr(HPSocketDLL, "HP_UdpCast_IsMultiCastLoop") else None
if HP_UdpCast_IsMultiCastLoop:
    HP_UdpCast_IsMultiCastLoop.restype = ctypes.c_bool
    HP_UdpCast_IsMultiCastLoop.argtypes = [HP_UdpCast]

# *************************************************************************************
# **************************** TCP Pull Server 组件操作方法 ****************************

#
# * 名称：抓取数据
# * 描述：用户通过该方法从 Socket 组件中抓取数据
# *
# * 参数：		dwConnID	-- 连接 ID
# *			pData		-- 抓取缓冲区
# *			iLength		-- 抓取数据长度
# * 返回值：	En_HP_FetchResult
#
# HPSOCKET_API En_HP_FetchResult __stdcall HP_TcpPullServer_Fetch(HP_TcpPullServer pServer, HP_CONNID dwConnID, BYTE* pData, int iLength);
HP_TcpPullServer_Fetch = HPSocketDLL.HP_TcpPullServer_Fetch if hasattr(HPSocketDLL, "HP_TcpPullServer_Fetch") else None
if HP_TcpPullServer_Fetch:
    HP_TcpPullServer_Fetch.restype = En_HP_FetchResult
    HP_TcpPullServer_Fetch.argtypes = [HP_TcpPullServer, HP_CONNID, ctypes.POINTER(ctypes.c_byte), ctypes.c_int]

#
# * 名称：窥探数据（不会移除缓冲区数据）
# * 描述：用户通过该方法从 Socket 组件中窥探数据
# *
# * 参数：		dwConnID	-- 连接 ID
# *			pData		-- 窥探缓冲区
# *			iLength		-- 窥探数据长度
# * 返回值：	En_HP_FetchResult
#
# HPSOCKET_API En_HP_FetchResult __stdcall HP_TcpPullServer_Peek(HP_TcpPullServer pServer, HP_CONNID dwConnID, BYTE* pData, int iLength);
HP_TcpPullServer_Peek = HPSocketDLL.HP_TcpPullServer_Peek if hasattr(HPSocketDLL, "HP_TcpPullServer_Peek") else None
if HP_TcpPullServer_Peek:
    HP_TcpPullServer_Peek.restype = En_HP_FetchResult
    HP_TcpPullServer_Peek.argtypes = [HP_TcpPullServer, HP_CONNID, ctypes.POINTER(ctypes.c_byte), ctypes.c_int]

# *************************************************************************************
# **************************** TCP Pull Server 属性访问方法 ****************************

# *************************************************************************************
# **************************** TCP Pull Agent 组件操作方法 ****************************

#
# * 名称：抓取数据
# * 描述：用户通过该方法从 Socket 组件中抓取数据
# *
# * 参数：		dwConnID	-- 连接 ID
# *			pData		-- 抓取缓冲区
# *			iLength		-- 抓取数据长度
# * 返回值：	En_HP_FetchResult
#
# HPSOCKET_API En_HP_FetchResult __stdcall HP_TcpPullAgent_Fetch(HP_TcpPullAgent pAgent, HP_CONNID dwConnID, BYTE* pData, int iLength);
HP_TcpPullAgent_Fetch = HPSocketDLL.HP_TcpPullAgent_Fetch if hasattr(HPSocketDLL, "HP_TcpPullAgent_Fetch") else None
if HP_TcpPullAgent_Fetch:
    HP_TcpPullAgent_Fetch.restype = En_HP_FetchResult
    HP_TcpPullAgent_Fetch.argtypes = [HP_TcpPullAgent, HP_CONNID, ctypes.POINTER(ctypes.c_byte), ctypes.c_int]

#
# * 名称：窥探数据（不会移除缓冲区数据）
# * 描述：用户通过该方法从 Socket 组件中窥探数据
# *
# * 参数：		dwConnID	-- 连接 ID
# *			pData		-- 窥探缓冲区
# *			iLength		-- 窥探数据长度
# * 返回值：	En_HP_FetchResult
#
# HPSOCKET_API En_HP_FetchResult __stdcall HP_TcpPullAgent_Peek(HP_TcpPullAgent pAgent, HP_CONNID dwConnID, BYTE* pData, int iLength);
HP_TcpPullAgent_Peek = HPSocketDLL.HP_TcpPullAgent_Peek if hasattr(HPSocketDLL, "HP_TcpPullAgent_Peek") else None
if HP_TcpPullAgent_Peek:
    HP_TcpPullAgent_Peek.restype = En_HP_FetchResult
    HP_TcpPullAgent_Peek.argtypes = [HP_TcpPullAgent, HP_CONNID, ctypes.POINTER(ctypes.c_byte), ctypes.c_int]

# *************************************************************************************
# **************************** TCP Pull Agent 属性访问方法 ****************************

# *************************************************************************************
# **************************** TCP Pull Client 组件操作方法 ****************************

#
# * 名称：抓取数据
# * 描述：用户通过该方法从 Socket 组件中抓取数据
# *
# * 参数：		dwConnID	-- 连接 ID
# *			pData		-- 抓取缓冲区
# *			iLength		-- 抓取数据长度
# * 返回值：	En_HP_FetchResult
#
# HPSOCKET_API En_HP_FetchResult __stdcall HP_TcpPullClient_Fetch(HP_TcpPullClient pClient, BYTE* pData, int iLength);
HP_TcpPullClient_Fetch = HPSocketDLL.HP_TcpPullClient_Fetch if hasattr(HPSocketDLL, "HP_TcpPullClient_Fetch") else None
if HP_TcpPullClient_Fetch:
    HP_TcpPullClient_Fetch.restype = En_HP_FetchResult
    HP_TcpPullClient_Fetch.argtypes = [HP_TcpPullClient, ctypes.POINTER(ctypes.c_byte), ctypes.c_int]

#
# * 名称：窥探数据（不会移除缓冲区数据）
# * 描述：用户通过该方法从 Socket 组件中窥探数据
# *
# * 参数：		dwConnID	-- 连接 ID
# *			pData		-- 窥探缓冲区
# *			iLength		-- 窥探数据长度
# * 返回值：	En_HP_FetchResult
#
# HPSOCKET_API En_HP_FetchResult __stdcall HP_TcpPullClient_Peek(HP_TcpPullClient pClient, BYTE* pData, int iLength);
HP_TcpPullClient_Peek = HPSocketDLL.HP_TcpPullClient_Peek if hasattr(HPSocketDLL, "HP_TcpPullClient_Peek") else None
if HP_TcpPullClient_Peek:
    HP_TcpPullClient_Peek.restype = En_HP_FetchResult
    HP_TcpPullClient_Peek.argtypes = [HP_TcpPullClient, ctypes.POINTER(ctypes.c_byte), ctypes.c_int]

# *************************************************************************************
# **************************** TCP Pull Client 属性访问方法 ****************************

# *************************************************************************************
# **************************** TCP Pack Server 组件操作方法 ****************************

# *************************************************************************************
# **************************** TCP Pack Server 属性访问方法 ****************************

#  设置数据包最大长度（有效数据包最大长度不能超过 4194303/0x3FFFFF 字节，默认：262144/0x40000）
# HPSOCKET_API void __stdcall HP_TcpPackServer_SetMaxPackSize(HP_TcpPackServer pServer, DWORD dwMaxPackSize);
HP_TcpPackServer_SetMaxPackSize = HPSocketDLL.HP_TcpPackServer_SetMaxPackSize if hasattr(HPSocketDLL, "HP_TcpPackServer_SetMaxPackSize") else None
if HP_TcpPackServer_SetMaxPackSize:
    HP_TcpPackServer_SetMaxPackSize.restype = None
    HP_TcpPackServer_SetMaxPackSize.argtypes = [HP_TcpPackServer, ctypes.c_uint]
#  设置包头标识（有效包头标识取值范围 0 ~ 1023/0x3FF，当包头标识为 0 时不校验包头，默认：0）
# HPSOCKET_API void __stdcall HP_TcpPackServer_SetPackHeaderFlag(HP_TcpPackServer pServer, USHORT usPackHeaderFlag);
HP_TcpPackServer_SetPackHeaderFlag = HPSocketDLL.HP_TcpPackServer_SetPackHeaderFlag if hasattr(HPSocketDLL, "HP_TcpPackServer_SetPackHeaderFlag") else None
if HP_TcpPackServer_SetPackHeaderFlag:
    HP_TcpPackServer_SetPackHeaderFlag.restype = None
    HP_TcpPackServer_SetPackHeaderFlag.argtypes = [HP_TcpPackServer, ctypes.c_ushort]

#  获取数据包最大长度
# HPSOCKET_API DWORD __stdcall HP_TcpPackServer_GetMaxPackSize(HP_TcpPackServer pServer);
HP_TcpPackServer_GetMaxPackSize = HPSocketDLL.HP_TcpPackServer_GetMaxPackSize if hasattr(HPSocketDLL, "HP_TcpPackServer_GetMaxPackSize") else None
if HP_TcpPackServer_GetMaxPackSize:
    HP_TcpPackServer_GetMaxPackSize.restype = ctypes.c_uint
    HP_TcpPackServer_GetMaxPackSize.argtypes = [HP_TcpPackServer]
#  获取包头标识
# HPSOCKET_API USHORT __stdcall HP_TcpPackServer_GetPackHeaderFlag(HP_TcpPackServer pServer);
HP_TcpPackServer_GetPackHeaderFlag = HPSocketDLL.HP_TcpPackServer_GetPackHeaderFlag if hasattr(HPSocketDLL, "HP_TcpPackServer_GetPackHeaderFlag") else None
if HP_TcpPackServer_GetPackHeaderFlag:
    HP_TcpPackServer_GetPackHeaderFlag.restype = ctypes.c_ushort
    HP_TcpPackServer_GetPackHeaderFlag.argtypes = [HP_TcpPackServer]

# *************************************************************************************
# **************************** TCP Pack Agent 组件操作方法 ****************************

# *************************************************************************************
# **************************** TCP Pack Agent 属性访问方法 ****************************

#  设置数据包最大长度（有效数据包最大长度不能超过 4194303/0x3FFFFF 字节，默认：262144/0x40000）
# HPSOCKET_API void __stdcall HP_TcpPackAgent_SetMaxPackSize(HP_TcpPackAgent pAgent, DWORD dwMaxPackSize);
HP_TcpPackAgent_SetMaxPackSize = HPSocketDLL.HP_TcpPackAgent_SetMaxPackSize if hasattr(HPSocketDLL, "HP_TcpPackAgent_SetMaxPackSize") else None
if HP_TcpPackAgent_SetMaxPackSize:
    HP_TcpPackAgent_SetMaxPackSize.restype = None
    HP_TcpPackAgent_SetMaxPackSize.argtypes = [HP_TcpPackAgent, ctypes.c_uint]
#  设置包头标识（有效包头标识取值范围 0 ~ 1023/0x3FF，当包头标识为 0 时不校验包头，默认：0）
# HPSOCKET_API void __stdcall HP_TcpPackAgent_SetPackHeaderFlag(HP_TcpPackAgent pAgent, USHORT usPackHeaderFlag);
HP_TcpPackAgent_SetPackHeaderFlag = HPSocketDLL.HP_TcpPackAgent_SetPackHeaderFlag if hasattr(HPSocketDLL, "HP_TcpPackAgent_SetPackHeaderFlag") else None
if HP_TcpPackAgent_SetPackHeaderFlag:
    HP_TcpPackAgent_SetPackHeaderFlag.restype = None
    HP_TcpPackAgent_SetPackHeaderFlag.argtypes = [HP_TcpPackAgent, ctypes.c_ushort]

#  获取数据包最大长度
# HPSOCKET_API DWORD __stdcall HP_TcpPackAgent_GetMaxPackSize(HP_TcpPackAgent pAgent);
HP_TcpPackAgent_GetMaxPackSize = HPSocketDLL.HP_TcpPackAgent_GetMaxPackSize if hasattr(HPSocketDLL, "HP_TcpPackAgent_GetMaxPackSize") else None
if HP_TcpPackAgent_GetMaxPackSize:
    HP_TcpPackAgent_GetMaxPackSize.restype = ctypes.c_uint
    HP_TcpPackAgent_GetMaxPackSize.argtypes = [HP_TcpPackAgent]
#  获取包头标识
# HPSOCKET_API USHORT __stdcall HP_TcpPackAgent_GetPackHeaderFlag(HP_TcpPackAgent pAgent);
HP_TcpPackAgent_GetPackHeaderFlag = HPSocketDLL.HP_TcpPackAgent_GetPackHeaderFlag if hasattr(HPSocketDLL, "HP_TcpPackAgent_GetPackHeaderFlag") else None
if HP_TcpPackAgent_GetPackHeaderFlag:
    HP_TcpPackAgent_GetPackHeaderFlag.restype = ctypes.c_ushort
    HP_TcpPackAgent_GetPackHeaderFlag.argtypes = [HP_TcpPackAgent]

# *************************************************************************************
# **************************** TCP Pack Client 组件操作方法 ****************************

# *************************************************************************************
# **************************** TCP Pack Client 属性访问方法 ****************************

#  设置数据包最大长度（有效数据包最大长度不能超过 4194303/0x3FFFFF 字节，默认：262144/0x40000）
# HPSOCKET_API void __stdcall HP_TcpPackClient_SetMaxPackSize(HP_TcpPackClient pClient, DWORD dwMaxPackSize);
HP_TcpPackClient_SetMaxPackSize = HPSocketDLL.HP_TcpPackClient_SetMaxPackSize if hasattr(HPSocketDLL, "HP_TcpPackClient_SetMaxPackSize") else None
if HP_TcpPackClient_SetMaxPackSize:
    HP_TcpPackClient_SetMaxPackSize.restype = None
    HP_TcpPackClient_SetMaxPackSize.argtypes = [HP_TcpPackClient, ctypes.c_uint]
#  设置包头标识（有效包头标识取值范围 0 ~ 1023/0x3FF，当包头标识为 0 时不校验包头，默认：0）
# HPSOCKET_API void __stdcall HP_TcpPackClient_SetPackHeaderFlag(HP_TcpPackClient pClient, USHORT usPackHeaderFlag);
HP_TcpPackClient_SetPackHeaderFlag = HPSocketDLL.HP_TcpPackClient_SetPackHeaderFlag if hasattr(HPSocketDLL, "HP_TcpPackClient_SetPackHeaderFlag") else None
if HP_TcpPackClient_SetPackHeaderFlag:
    HP_TcpPackClient_SetPackHeaderFlag.restype = None
    HP_TcpPackClient_SetPackHeaderFlag.argtypes = [HP_TcpPackClient, ctypes.c_ushort]

#  获取数据包最大长度
# HPSOCKET_API DWORD __stdcall HP_TcpPackClient_GetMaxPackSize(HP_TcpPackClient pClient);
HP_TcpPackClient_GetMaxPackSize = HPSocketDLL.HP_TcpPackClient_GetMaxPackSize if hasattr(HPSocketDLL, "HP_TcpPackClient_GetMaxPackSize") else None
if HP_TcpPackClient_GetMaxPackSize:
    HP_TcpPackClient_GetMaxPackSize.restype = ctypes.c_uint
    HP_TcpPackClient_GetMaxPackSize.argtypes = [HP_TcpPackClient]
#  获取包头标识
# HPSOCKET_API USHORT __stdcall HP_TcpPackClient_GetPackHeaderFlag(HP_TcpPackClient pClient);
HP_TcpPackClient_GetPackHeaderFlag = HPSocketDLL.HP_TcpPackClient_GetPackHeaderFlag if hasattr(HPSocketDLL, "HP_TcpPackClient_GetPackHeaderFlag") else None
if HP_TcpPackClient_GetPackHeaderFlag:
    HP_TcpPackClient_GetPackHeaderFlag.restype = ctypes.c_ushort
    HP_TcpPackClient_GetPackHeaderFlag.argtypes = [HP_TcpPackClient]

# ***************************************************************************************************************************************************
# ******************************************************************* HTTP Exports ******************************************************************
# ***************************************************************************************************************************************************

# **************************************************
# ****************** HTTP 回调函数 ******************

#  HTTP 回调函数
# typedef En_HP_HttpParseResult (__stdcall *HP_FN_Http_OnMessageBegin)	(HP_Http pSender, HP_CONNID dwConnID);
HP_FN_Http_OnMessageBegin = ctypes.CFUNCTYPE(En_HP_HttpParseResult, HP_Http, HP_CONNID)
# typedef En_HP_HttpParseResult (__stdcall *HP_FN_Http_OnRequestLine)		(HP_Http pSender, HP_CONNID dwConnID, LPCSTR lpszMethod, LPCSTR lpszUrl);
HP_FN_Http_OnRequestLine = ctypes.CFUNCTYPE(En_HP_HttpParseResult, HP_Http, HP_CONNID, ctypes.c_char_p, ctypes.c_char_p)
# typedef En_HP_HttpParseResult (__stdcall *HP_FN_Http_OnStatusLine)		(HP_Http pSender, HP_CONNID dwConnID, USHORT usStatusCode, LPCSTR lpszDesc);
HP_FN_Http_OnStatusLine = ctypes.CFUNCTYPE(En_HP_HttpParseResult, HP_Http, HP_CONNID, ctypes.c_ushort, ctypes.c_char_p)
# typedef En_HP_HttpParseResult (__stdcall *HP_FN_Http_OnHeader)			(HP_Http pSender, HP_CONNID dwConnID, LPCSTR lpszName, LPCSTR lpszValue);
HP_FN_Http_OnHeader = ctypes.CFUNCTYPE(En_HP_HttpParseResult, HP_Http, HP_CONNID, ctypes.c_char_p, ctypes.c_char_p)
# typedef En_HP_HttpParseResult (__stdcall *HP_FN_Http_OnHeadersComplete)	(HP_Http pSender, HP_CONNID dwConnID);
HP_FN_Http_OnHeadersComplete = ctypes.CFUNCTYPE(En_HP_HttpParseResult, HP_Http, HP_CONNID)
# typedef En_HP_HttpParseResult (__stdcall *HP_FN_Http_OnBody)			(HP_Http pSender, HP_CONNID dwConnID, const BYTE* pData, int iLength);
HP_FN_Http_OnBody = ctypes.CFUNCTYPE(En_HP_HttpParseResult, HP_Http, HP_CONNID, ctypes.POINTER(ctypes.c_byte), ctypes.c_int)
# typedef En_HP_HttpParseResult (__stdcall *HP_FN_Http_OnChunkHeader)		(HP_Http pSender, HP_CONNID dwConnID, int iLength);
HP_FN_Http_OnChunkHeader = ctypes.CFUNCTYPE(En_HP_HttpParseResult, HP_Http, HP_CONNID, ctypes.c_int)
# typedef En_HP_HttpParseResult (__stdcall *HP_FN_Http_OnChunkComplete)	(HP_Http pSender, HP_CONNID dwConnID);
HP_FN_Http_OnChunkComplete = ctypes.CFUNCTYPE(En_HP_HttpParseResult, HP_Http, HP_CONNID)
# typedef En_HP_HttpParseResult (__stdcall *HP_FN_Http_OnMessageComplete)	(HP_Http pSender, HP_CONNID dwConnID);
HP_FN_Http_OnMessageComplete = ctypes.CFUNCTYPE(En_HP_HttpParseResult, HP_Http, HP_CONNID)
# typedef En_HP_HttpParseResult (__stdcall *HP_FN_Http_OnUpgrade)			(HP_Http pSender, HP_CONNID dwConnID, En_HP_HttpUpgradeType enUpgradeType);
HP_FN_Http_OnUpgrade = ctypes.CFUNCTYPE(En_HP_HttpParseResult, HP_Http, HP_CONNID, En_HP_HttpUpgradeType)
# typedef En_HP_HttpParseResult (__stdcall *HP_FN_Http_OnParseError)		(HP_Http pSender, HP_CONNID dwConnID, int iErrorCode, LPCSTR lpszErrorDesc);
HP_FN_Http_OnParseError = ctypes.CFUNCTYPE(En_HP_HttpParseResult, HP_Http, HP_CONNID, ctypes.c_int, ctypes.c_char_p)

# typedef En_HP_HandleResult	 (__stdcall *HP_FN_Http_OnWSMessageHeader)	(HP_Http pSender, HP_CONNID dwConnID, BOOL bFinal, BYTE iReserved, BYTE iOperationCode, const int lpszMask, ULONGLONG ullBodyLen);
HP_FN_Http_OnWSMessageHeader = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Http, HP_CONNID, ctypes.c_bool, ctypes.c_byte, ctypes.c_byte, ctypes.c_int, ctypes.c_ulonglong)
# typedef En_HP_HandleResult	 (__stdcall *HP_FN_Http_OnWSMessageBody)	(HP_Http pSender, HP_CONNID dwConnID, const BYTE* pData, int iLength);
HP_FN_Http_OnWSMessageBody = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Http, HP_CONNID, ctypes.POINTER(ctypes.c_byte), ctypes.c_int)
# typedef En_HP_HandleResult	 (__stdcall *HP_FN_Http_OnWSMessageComplete)(HP_Http pSender, HP_CONNID dwConnID);
HP_FN_Http_OnWSMessageComplete = ctypes.CFUNCTYPE(En_HP_HandleResult, HP_Http, HP_CONNID)

#  HTTP Server 回调函数
# typedef HP_FN_Http_OnMessageBegin   HP_FN_HttpServer_OnMessageBegin;
HP_FN_HttpServer_OnMessageBegin = HP_FN_Http_OnMessageBegin
# typedef HP_FN_Http_OnRequestLine   HP_FN_HttpServer_OnRequestLine;
HP_FN_HttpServer_OnRequestLine = HP_FN_Http_OnRequestLine
# typedef HP_FN_Http_OnHeader     HP_FN_HttpServer_OnHeader;
HP_FN_HttpServer_OnHeader = HP_FN_Http_OnHeader
# typedef HP_FN_Http_OnHeadersComplete  HP_FN_HttpServer_OnHeadersComplete;
HP_FN_HttpServer_OnHeadersComplete = HP_FN_Http_OnHeadersComplete
# typedef HP_FN_Http_OnBody     HP_FN_HttpServer_OnBody;
HP_FN_HttpServer_OnBody = HP_FN_Http_OnBody
# typedef HP_FN_Http_OnChunkHeader   HP_FN_HttpServer_OnChunkHeader;
HP_FN_HttpServer_OnChunkHeader = HP_FN_Http_OnChunkHeader
# typedef HP_FN_Http_OnChunkComplete   HP_FN_HttpServer_OnChunkComplete;
HP_FN_HttpServer_OnChunkComplete = HP_FN_Http_OnChunkComplete
# typedef HP_FN_Http_OnMessageComplete  HP_FN_HttpServer_OnMessageComplete;
HP_FN_HttpServer_OnMessageComplete = HP_FN_Http_OnMessageComplete
# typedef HP_FN_Http_OnUpgrade    HP_FN_HttpServer_OnUpgrade;
HP_FN_HttpServer_OnUpgrade = HP_FN_Http_OnUpgrade
# typedef HP_FN_Http_OnParseError    HP_FN_HttpServer_OnParseError;
HP_FN_HttpServer_OnParseError = HP_FN_Http_OnParseError

# typedef HP_FN_Http_OnWSMessageHeader  HP_FN_HttpServer_OnWSMessageHeader;
HP_FN_HttpServer_OnWSMessageHeader = HP_FN_Http_OnWSMessageHeader
# typedef HP_FN_Http_OnWSMessageBody   HP_FN_HttpServer_OnWSMessageBody;
HP_FN_HttpServer_OnWSMessageBody = HP_FN_Http_OnWSMessageBody
# typedef HP_FN_Http_OnWSMessageComplete  HP_FN_HttpServer_OnWSMessageComplete;
HP_FN_HttpServer_OnWSMessageComplete = HP_FN_Http_OnWSMessageComplete

# typedef HP_FN_Server_OnPrepareListen  HP_FN_HttpServer_OnPrepareListen;
HP_FN_HttpServer_OnPrepareListen = HP_FN_Server_OnPrepareListen
# typedef HP_FN_Server_OnAccept    HP_FN_HttpServer_OnAccept;
HP_FN_HttpServer_OnAccept = HP_FN_Server_OnAccept
# typedef HP_FN_Server_OnHandShake   HP_FN_HttpServer_OnHandShake;
HP_FN_HttpServer_OnHandShake = HP_FN_Server_OnHandShake
# typedef HP_FN_Server_OnReceive    HP_FN_HttpServer_OnReceive;
HP_FN_HttpServer_OnReceive = HP_FN_Server_OnReceive
# typedef HP_FN_Server_OnSend     HP_FN_HttpServer_OnSend;
HP_FN_HttpServer_OnSend = HP_FN_Server_OnSend
# typedef HP_FN_Server_OnClose    HP_FN_HttpServer_OnClose;
HP_FN_HttpServer_OnClose = HP_FN_Server_OnClose
# typedef HP_FN_Server_OnShutdown    HP_FN_HttpServer_OnShutdown;
HP_FN_HttpServer_OnShutdown = HP_FN_Server_OnShutdown

#  HTTP Agent 回调函数
# typedef HP_FN_Http_OnMessageBegin   HP_FN_HttpAgent_OnMessageBegin;
HP_FN_HttpAgent_OnMessageBegin = HP_FN_Http_OnMessageBegin
# typedef HP_FN_Http_OnStatusLine    HP_FN_HttpAgent_OnStatusLine;
HP_FN_HttpAgent_OnStatusLine = HP_FN_Http_OnStatusLine
# typedef HP_FN_Http_OnHeader     HP_FN_HttpAgent_OnHeader;
HP_FN_HttpAgent_OnHeader = HP_FN_Http_OnHeader
# typedef HP_FN_Http_OnHeadersComplete  HP_FN_HttpAgent_OnHeadersComplete;
HP_FN_HttpAgent_OnHeadersComplete = HP_FN_Http_OnHeadersComplete
# typedef HP_FN_Http_OnBody     HP_FN_HttpAgent_OnBody;
HP_FN_HttpAgent_OnBody = HP_FN_Http_OnBody
# typedef HP_FN_Http_OnChunkHeader   HP_FN_HttpAgent_OnChunkHeader;
HP_FN_HttpAgent_OnChunkHeader = HP_FN_Http_OnChunkHeader
# typedef HP_FN_Http_OnChunkComplete   HP_FN_HttpAgent_OnChunkComplete;
HP_FN_HttpAgent_OnChunkComplete = HP_FN_Http_OnChunkComplete
# typedef HP_FN_Http_OnMessageComplete  HP_FN_HttpAgent_OnMessageComplete;
HP_FN_HttpAgent_OnMessageComplete = HP_FN_Http_OnMessageComplete
# typedef HP_FN_Http_OnUpgrade    HP_FN_HttpAgent_OnUpgrade;
HP_FN_HttpAgent_OnUpgrade = HP_FN_Http_OnUpgrade
# typedef HP_FN_Http_OnParseError    HP_FN_HttpAgent_OnParseError;
HP_FN_HttpAgent_OnParseError = HP_FN_Http_OnParseError

# typedef HP_FN_Http_OnWSMessageHeader  HP_FN_HttpAgent_OnWSMessageHeader;
HP_FN_HttpAgent_OnWSMessageHeader = HP_FN_Http_OnWSMessageHeader
# typedef HP_FN_Http_OnWSMessageBody   HP_FN_HttpAgent_OnWSMessageBody;
HP_FN_HttpAgent_OnWSMessageBody = HP_FN_Http_OnWSMessageBody
# typedef HP_FN_Http_OnWSMessageComplete  HP_FN_HttpAgent_OnWSMessageComplete;
HP_FN_HttpAgent_OnWSMessageComplete = HP_FN_Http_OnWSMessageComplete

# typedef HP_FN_Agent_OnPrepareConnect  HP_FN_HttpAgent_OnPrepareConnect;
HP_FN_HttpAgent_OnPrepareConnect = HP_FN_Agent_OnPrepareConnect
# typedef HP_FN_Agent_OnConnect    HP_FN_HttpAgent_OnConnect;
HP_FN_HttpAgent_OnConnect = HP_FN_Agent_OnConnect
# typedef HP_FN_Agent_OnHandShake    HP_FN_HttpAgent_OnHandShake;
HP_FN_HttpAgent_OnHandShake = HP_FN_Agent_OnHandShake
# typedef HP_FN_Agent_OnReceive    HP_FN_HttpAgent_OnReceive;
HP_FN_HttpAgent_OnReceive = HP_FN_Agent_OnReceive
# typedef HP_FN_Agent_OnSend     HP_FN_HttpAgent_OnSend;
HP_FN_HttpAgent_OnSend = HP_FN_Agent_OnSend
# typedef HP_FN_Agent_OnClose     HP_FN_HttpAgent_OnClose;
HP_FN_HttpAgent_OnClose = HP_FN_Agent_OnClose
# typedef HP_FN_Agent_OnShutdown    HP_FN_HttpAgent_OnShutdown;
HP_FN_HttpAgent_OnShutdown = HP_FN_Agent_OnShutdown

#  HTTP Client 回调函数
# typedef HP_FN_Http_OnMessageBegin   HP_FN_HttpClient_OnMessageBegin;
HP_FN_HttpClient_OnMessageBegin = HP_FN_Http_OnMessageBegin
# typedef HP_FN_Http_OnStatusLine    HP_FN_HttpClient_OnStatusLine;
HP_FN_HttpClient_OnStatusLine = HP_FN_Http_OnStatusLine
# typedef HP_FN_Http_OnHeader     HP_FN_HttpClient_OnHeader;
HP_FN_HttpClient_OnHeader = HP_FN_Http_OnHeader
# typedef HP_FN_Http_OnHeadersComplete  HP_FN_HttpClient_OnHeadersComplete;
HP_FN_HttpClient_OnHeadersComplete = HP_FN_Http_OnHeadersComplete
# typedef HP_FN_Http_OnBody     HP_FN_HttpClient_OnBody;
HP_FN_HttpClient_OnBody = HP_FN_Http_OnBody
# typedef HP_FN_Http_OnChunkHeader   HP_FN_HttpClient_OnChunkHeader;
HP_FN_HttpClient_OnChunkHeader = HP_FN_Http_OnChunkHeader
# typedef HP_FN_Http_OnChunkComplete   HP_FN_HttpClient_OnChunkComplete;
HP_FN_HttpClient_OnChunkComplete = HP_FN_Http_OnChunkComplete
# typedef HP_FN_Http_OnMessageComplete  HP_FN_HttpClient_OnMessageComplete;
HP_FN_HttpClient_OnMessageComplete = HP_FN_Http_OnMessageComplete
# typedef HP_FN_Http_OnUpgrade    HP_FN_HttpClient_OnUpgrade;
HP_FN_HttpClient_OnUpgrade = HP_FN_Http_OnUpgrade
# typedef HP_FN_Http_OnParseError    HP_FN_HttpClient_OnParseError;
HP_FN_HttpClient_OnParseError = HP_FN_Http_OnParseError

# typedef HP_FN_Http_OnWSMessageHeader  HP_FN_HttpClient_OnWSMessageHeader;
HP_FN_HttpClient_OnWSMessageHeader = HP_FN_Http_OnWSMessageHeader
# typedef HP_FN_Http_OnWSMessageBody   HP_FN_HttpClient_OnWSMessageBody;
HP_FN_HttpClient_OnWSMessageBody = HP_FN_Http_OnWSMessageBody
# typedef HP_FN_Http_OnWSMessageComplete  HP_FN_HttpClient_OnWSMessageComplete;
HP_FN_HttpClient_OnWSMessageComplete = HP_FN_Http_OnWSMessageComplete

# typedef HP_FN_Client_OnPrepareConnect  HP_FN_HttpClient_OnPrepareConnect;
HP_FN_HttpClient_OnPrepareConnect = HP_FN_Client_OnPrepareConnect
# typedef HP_FN_Client_OnConnect    HP_FN_HttpClient_OnConnect;
HP_FN_HttpClient_OnConnect = HP_FN_Client_OnConnect
# typedef HP_FN_Client_OnHandShake   HP_FN_HttpClient_OnHandShake;
HP_FN_HttpClient_OnHandShake = HP_FN_Client_OnHandShake
# typedef HP_FN_Client_OnReceive    HP_FN_HttpClient_OnReceive;
HP_FN_HttpClient_OnReceive = HP_FN_Client_OnReceive
# typedef HP_FN_Client_OnSend     HP_FN_HttpClient_OnSend;
HP_FN_HttpClient_OnSend = HP_FN_Client_OnSend
# typedef HP_FN_Client_OnClose    HP_FN_HttpClient_OnClose;
HP_FN_HttpClient_OnClose = HP_FN_Client_OnClose

# **************************************************
# **************** HTTP 对象创建函数 ****************

#  创建 HP_HttpServer 对象
# HPSOCKET_API HP_HttpServer __stdcall Create_HP_HttpServer(HP_HttpServerListener pListener);
Create_HP_HttpServer = HPSocketDLL.Create_HP_HttpServer if hasattr(HPSocketDLL, "Create_HP_HttpServer") else None
if Create_HP_HttpServer:
    Create_HP_HttpServer.restype = HP_HttpServer
    Create_HP_HttpServer.argtypes = [HP_HttpServerListener]
#  创建 HP_HttpAgent 对象
# HPSOCKET_API HP_HttpAgent __stdcall Create_HP_HttpAgent(HP_HttpAgentListener pListener);
Create_HP_HttpAgent = HPSocketDLL.Create_HP_HttpAgent if hasattr(HPSocketDLL, "Create_HP_HttpAgent") else None
if Create_HP_HttpAgent:
    Create_HP_HttpAgent.restype = HP_HttpAgent
    Create_HP_HttpAgent.argtypes = [HP_HttpAgentListener]
#  创建 HP_HttpClient 对象
# HPSOCKET_API HP_HttpClient __stdcall Create_HP_HttpClient(HP_HttpClientListener pListener);
Create_HP_HttpClient = HPSocketDLL.Create_HP_HttpClient if hasattr(HPSocketDLL, "Create_HP_HttpClient") else None
if Create_HP_HttpClient:
    Create_HP_HttpClient.restype = HP_HttpClient
    Create_HP_HttpClient.argtypes = [HP_HttpClientListener]
#  创建 HP_HttpSyncClient 对象
# HPSOCKET_API HP_HttpSyncClient __stdcall Create_HP_HttpSyncClient(HP_HttpClientListener pListener);
Create_HP_HttpSyncClient = HPSocketDLL.Create_HP_HttpSyncClient if hasattr(HPSocketDLL, "Create_HP_HttpSyncClient") else None
if Create_HP_HttpSyncClient:
    Create_HP_HttpSyncClient.restype = HP_HttpSyncClient
    Create_HP_HttpSyncClient.argtypes = [HP_HttpClientListener]

#  销毁 HP_HttpServer 对象
# HPSOCKET_API void __stdcall Destroy_HP_HttpServer(HP_HttpServer pServer);
Destroy_HP_HttpServer = HPSocketDLL.Destroy_HP_HttpServer if hasattr(HPSocketDLL, "Destroy_HP_HttpServer") else None
if Destroy_HP_HttpServer:
    Destroy_HP_HttpServer.restype = None
    Destroy_HP_HttpServer.argtypes = [HP_HttpServer]
#  销毁 HP_HttpAgent 对象
# HPSOCKET_API void __stdcall Destroy_HP_HttpAgent(HP_HttpAgent pAgent);
Destroy_HP_HttpAgent = HPSocketDLL.Destroy_HP_HttpAgent if hasattr(HPSocketDLL, "Destroy_HP_HttpAgent") else None
if Destroy_HP_HttpAgent:
    Destroy_HP_HttpAgent.restype = None
    Destroy_HP_HttpAgent.argtypes = [HP_HttpAgent]
#  销毁 HP_HttpClient 对象
# HPSOCKET_API void __stdcall Destroy_HP_HttpClient(HP_HttpClient pClient);
Destroy_HP_HttpClient = HPSocketDLL.Destroy_HP_HttpClient if hasattr(HPSocketDLL, "Destroy_HP_HttpClient") else None
if Destroy_HP_HttpClient:
    Destroy_HP_HttpClient.restype = None
    Destroy_HP_HttpClient.argtypes = [HP_HttpClient]
#  销毁 HP_HttpSyncClient 对象
# HPSOCKET_API void __stdcall Destroy_HP_HttpSyncClient(HP_HttpSyncClient pClient);
Destroy_HP_HttpSyncClient = HPSocketDLL.Destroy_HP_HttpSyncClient if hasattr(HPSocketDLL, "Destroy_HP_HttpSyncClient") else None
if Destroy_HP_HttpSyncClient:
    Destroy_HP_HttpSyncClient.restype = None
    Destroy_HP_HttpSyncClient.argtypes = [HP_HttpSyncClient]

#  创建 HP_HttpServerListener 对象
# HPSOCKET_API HP_HttpServerListener __stdcall Create_HP_HttpServerListener();
Create_HP_HttpServerListener = HPSocketDLL.Create_HP_HttpServerListener if hasattr(HPSocketDLL, "Create_HP_HttpServerListener") else None
if Create_HP_HttpServerListener:
    Create_HP_HttpServerListener.restype = HP_HttpServerListener
    Create_HP_HttpServerListener.argtypes = []
#  创建 HP_HttpAgentListener 对象
# HPSOCKET_API HP_HttpAgentListener __stdcall Create_HP_HttpAgentListener();
Create_HP_HttpAgentListener = HPSocketDLL.Create_HP_HttpAgentListener if hasattr(HPSocketDLL, "Create_HP_HttpAgentListener") else None
if Create_HP_HttpAgentListener:
    Create_HP_HttpAgentListener.restype = HP_HttpAgentListener
    Create_HP_HttpAgentListener.argtypes = []
#  创建 HP_HttpClientListener 对象
# HPSOCKET_API HP_HttpClientListener __stdcall Create_HP_HttpClientListener();
Create_HP_HttpClientListener = HPSocketDLL.Create_HP_HttpClientListener if hasattr(HPSocketDLL, "Create_HP_HttpClientListener") else None
if Create_HP_HttpClientListener:
    Create_HP_HttpClientListener.restype = HP_HttpClientListener
    Create_HP_HttpClientListener.argtypes = []

#  销毁 HP_HttpServerListener 对象
# HPSOCKET_API void __stdcall Destroy_HP_HttpServerListener(HP_HttpServerListener pListener);
Destroy_HP_HttpServerListener = HPSocketDLL.Destroy_HP_HttpServerListener if hasattr(HPSocketDLL, "Destroy_HP_HttpServerListener") else None
if Destroy_HP_HttpServerListener:
    Destroy_HP_HttpServerListener.restype = None
    Destroy_HP_HttpServerListener.argtypes = [HP_HttpServerListener]
#  销毁 HP_HttpAgentListener 对象
# HPSOCKET_API void __stdcall Destroy_HP_HttpAgentListener(HP_HttpAgentListener pListener);
Destroy_HP_HttpAgentListener = HPSocketDLL.Destroy_HP_HttpAgentListener if hasattr(HPSocketDLL, "Destroy_HP_HttpAgentListener") else None
if Destroy_HP_HttpAgentListener:
    Destroy_HP_HttpAgentListener.restype = None
    Destroy_HP_HttpAgentListener.argtypes = [HP_HttpAgentListener]
#  销毁 HP_HttpClientListener 对象
# HPSOCKET_API void __stdcall Destroy_HP_HttpClientListener(HP_HttpClientListener pListener);
Destroy_HP_HttpClientListener = HPSocketDLL.Destroy_HP_HttpClientListener if hasattr(HPSocketDLL, "Destroy_HP_HttpClientListener") else None
if Destroy_HP_HttpClientListener:
    Destroy_HP_HttpClientListener.restype = None
    Destroy_HP_HttpClientListener.argtypes = [HP_HttpClientListener]

# ********************************************************************************
# ************************** HTTP Server 回调函数设置方法 *************************

# HPSOCKET_API void __stdcall HP_Set_FN_HttpServer_OnMessageBegin(HP_HttpServerListener pListener		, HP_FN_HttpServer_OnMessageBegin fn);
HP_Set_FN_HttpServer_OnMessageBegin = HPSocketDLL.HP_Set_FN_HttpServer_OnMessageBegin if hasattr(HPSocketDLL, "HP_Set_FN_HttpServer_OnMessageBegin") else None
if HP_Set_FN_HttpServer_OnMessageBegin:
    HP_Set_FN_HttpServer_OnMessageBegin.restype = None
    HP_Set_FN_HttpServer_OnMessageBegin.argtypes = [HP_HttpServerListener, HP_FN_HttpServer_OnMessageBegin]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpServer_OnRequestLine(HP_HttpServerListener pListener		, HP_FN_HttpServer_OnRequestLine fn);
HP_Set_FN_HttpServer_OnRequestLine = HPSocketDLL.HP_Set_FN_HttpServer_OnRequestLine if hasattr(HPSocketDLL, "HP_Set_FN_HttpServer_OnRequestLine") else None
if HP_Set_FN_HttpServer_OnRequestLine:
    HP_Set_FN_HttpServer_OnRequestLine.restype = None
    HP_Set_FN_HttpServer_OnRequestLine.argtypes = [HP_HttpServerListener, HP_FN_HttpServer_OnRequestLine]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpServer_OnHeader(HP_HttpServerListener pListener			, HP_FN_HttpServer_OnHeader fn);
HP_Set_FN_HttpServer_OnHeader = HPSocketDLL.HP_Set_FN_HttpServer_OnHeader if hasattr(HPSocketDLL, "HP_Set_FN_HttpServer_OnHeader") else None
if HP_Set_FN_HttpServer_OnHeader:
    HP_Set_FN_HttpServer_OnHeader.restype = None
    HP_Set_FN_HttpServer_OnHeader.argtypes = [HP_HttpServerListener, HP_FN_HttpServer_OnHeader]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpServer_OnHeadersComplete(HP_HttpServerListener pListener	, HP_FN_HttpServer_OnHeadersComplete fn);
HP_Set_FN_HttpServer_OnHeadersComplete = HPSocketDLL.HP_Set_FN_HttpServer_OnHeadersComplete if hasattr(HPSocketDLL, "HP_Set_FN_HttpServer_OnHeadersComplete") else None
if HP_Set_FN_HttpServer_OnHeadersComplete:
    HP_Set_FN_HttpServer_OnHeadersComplete.restype = None
    HP_Set_FN_HttpServer_OnHeadersComplete.argtypes = [HP_HttpServerListener, HP_FN_HttpServer_OnHeadersComplete]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpServer_OnBody(HP_HttpServerListener pListener				, HP_FN_HttpServer_OnBody fn);
HP_Set_FN_HttpServer_OnBody = HPSocketDLL.HP_Set_FN_HttpServer_OnBody if hasattr(HPSocketDLL, "HP_Set_FN_HttpServer_OnBody") else None
if HP_Set_FN_HttpServer_OnBody:
    HP_Set_FN_HttpServer_OnBody.restype = None
    HP_Set_FN_HttpServer_OnBody.argtypes = [HP_HttpServerListener, HP_FN_HttpServer_OnBody]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpServer_OnChunkHeader(HP_HttpServerListener pListener		, HP_FN_HttpServer_OnChunkHeader fn);
HP_Set_FN_HttpServer_OnChunkHeader = HPSocketDLL.HP_Set_FN_HttpServer_OnChunkHeader if hasattr(HPSocketDLL, "HP_Set_FN_HttpServer_OnChunkHeader") else None
if HP_Set_FN_HttpServer_OnChunkHeader:
    HP_Set_FN_HttpServer_OnChunkHeader.restype = None
    HP_Set_FN_HttpServer_OnChunkHeader.argtypes = [HP_HttpServerListener, HP_FN_HttpServer_OnChunkHeader]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpServer_OnChunkComplete(HP_HttpServerListener pListener	, HP_FN_HttpServer_OnChunkComplete fn);
HP_Set_FN_HttpServer_OnChunkComplete = HPSocketDLL.HP_Set_FN_HttpServer_OnChunkComplete if hasattr(HPSocketDLL, "HP_Set_FN_HttpServer_OnChunkComplete") else None
if HP_Set_FN_HttpServer_OnChunkComplete:
    HP_Set_FN_HttpServer_OnChunkComplete.restype = None
    HP_Set_FN_HttpServer_OnChunkComplete.argtypes = [HP_HttpServerListener, HP_FN_HttpServer_OnChunkComplete]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpServer_OnMessageComplete(HP_HttpServerListener pListener	, HP_FN_HttpServer_OnMessageComplete fn);
HP_Set_FN_HttpServer_OnMessageComplete = HPSocketDLL.HP_Set_FN_HttpServer_OnMessageComplete if hasattr(HPSocketDLL, "HP_Set_FN_HttpServer_OnMessageComplete") else None
if HP_Set_FN_HttpServer_OnMessageComplete:
    HP_Set_FN_HttpServer_OnMessageComplete.restype = None
    HP_Set_FN_HttpServer_OnMessageComplete.argtypes = [HP_HttpServerListener, HP_FN_HttpServer_OnMessageComplete]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpServer_OnUpgrade(HP_HttpServerListener pListener			, HP_FN_HttpServer_OnUpgrade fn);
HP_Set_FN_HttpServer_OnUpgrade = HPSocketDLL.HP_Set_FN_HttpServer_OnUpgrade if hasattr(HPSocketDLL, "HP_Set_FN_HttpServer_OnUpgrade") else None
if HP_Set_FN_HttpServer_OnUpgrade:
    HP_Set_FN_HttpServer_OnUpgrade.restype = None
    HP_Set_FN_HttpServer_OnUpgrade.argtypes = [HP_HttpServerListener, HP_FN_HttpServer_OnUpgrade]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpServer_OnParseError(HP_HttpServerListener pListener		, HP_FN_HttpServer_OnParseError fn);
HP_Set_FN_HttpServer_OnParseError = HPSocketDLL.HP_Set_FN_HttpServer_OnParseError if hasattr(HPSocketDLL, "HP_Set_FN_HttpServer_OnParseError") else None
if HP_Set_FN_HttpServer_OnParseError:
    HP_Set_FN_HttpServer_OnParseError.restype = None
    HP_Set_FN_HttpServer_OnParseError.argtypes = [HP_HttpServerListener, HP_FN_HttpServer_OnParseError]

# HPSOCKET_API void __stdcall HP_Set_FN_HttpServer_OnWSMessageHeader(HP_HttpServerListener pListener	, HP_FN_HttpServer_OnWSMessageHeader fn);
HP_Set_FN_HttpServer_OnWSMessageHeader = HPSocketDLL.HP_Set_FN_HttpServer_OnWSMessageHeader if hasattr(HPSocketDLL, "HP_Set_FN_HttpServer_OnWSMessageHeader") else None
if HP_Set_FN_HttpServer_OnWSMessageHeader:
    HP_Set_FN_HttpServer_OnWSMessageHeader.restype = None
    HP_Set_FN_HttpServer_OnWSMessageHeader.argtypes = [HP_HttpServerListener, HP_FN_HttpServer_OnWSMessageHeader]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpServer_OnWSMessageBody(HP_HttpServerListener pListener	, HP_FN_HttpServer_OnWSMessageBody fn);
HP_Set_FN_HttpServer_OnWSMessageBody = HPSocketDLL.HP_Set_FN_HttpServer_OnWSMessageBody if hasattr(HPSocketDLL, "HP_Set_FN_HttpServer_OnWSMessageBody") else None
if HP_Set_FN_HttpServer_OnWSMessageBody:
    HP_Set_FN_HttpServer_OnWSMessageBody.restype = None
    HP_Set_FN_HttpServer_OnWSMessageBody.argtypes = [HP_HttpServerListener, HP_FN_HttpServer_OnWSMessageBody]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpServer_OnWSMessageComplete(HP_HttpServerListener pListener, HP_FN_HttpServer_OnWSMessageComplete fn);
HP_Set_FN_HttpServer_OnWSMessageComplete = HPSocketDLL.HP_Set_FN_HttpServer_OnWSMessageComplete if hasattr(HPSocketDLL, "HP_Set_FN_HttpServer_OnWSMessageComplete") else None
if HP_Set_FN_HttpServer_OnWSMessageComplete:
    HP_Set_FN_HttpServer_OnWSMessageComplete.restype = None
    HP_Set_FN_HttpServer_OnWSMessageComplete.argtypes = [HP_HttpServerListener, HP_FN_HttpServer_OnWSMessageComplete]

# HPSOCKET_API void __stdcall HP_Set_FN_HttpServer_OnPrepareListen(HP_HttpServerListener pListener	, HP_FN_HttpServer_OnPrepareListen fn);
HP_Set_FN_HttpServer_OnPrepareListen = HPSocketDLL.HP_Set_FN_HttpServer_OnPrepareListen if hasattr(HPSocketDLL, "HP_Set_FN_HttpServer_OnPrepareListen") else None
if HP_Set_FN_HttpServer_OnPrepareListen:
    HP_Set_FN_HttpServer_OnPrepareListen.restype = None
    HP_Set_FN_HttpServer_OnPrepareListen.argtypes = [HP_HttpServerListener, HP_FN_HttpServer_OnPrepareListen]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpServer_OnAccept(HP_HttpServerListener pListener			, HP_FN_HttpServer_OnAccept fn);
HP_Set_FN_HttpServer_OnAccept = HPSocketDLL.HP_Set_FN_HttpServer_OnAccept if hasattr(HPSocketDLL, "HP_Set_FN_HttpServer_OnAccept") else None
if HP_Set_FN_HttpServer_OnAccept:
    HP_Set_FN_HttpServer_OnAccept.restype = None
    HP_Set_FN_HttpServer_OnAccept.argtypes = [HP_HttpServerListener, HP_FN_HttpServer_OnAccept]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpServer_OnHandShake(HP_HttpServerListener pListener		, HP_FN_HttpServer_OnHandShake fn);
HP_Set_FN_HttpServer_OnHandShake = HPSocketDLL.HP_Set_FN_HttpServer_OnHandShake if hasattr(HPSocketDLL, "HP_Set_FN_HttpServer_OnHandShake") else None
if HP_Set_FN_HttpServer_OnHandShake:
    HP_Set_FN_HttpServer_OnHandShake.restype = None
    HP_Set_FN_HttpServer_OnHandShake.argtypes = [HP_HttpServerListener, HP_FN_HttpServer_OnHandShake]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpServer_OnReceive(HP_HttpServerListener pListener			, HP_FN_HttpServer_OnReceive fn);
HP_Set_FN_HttpServer_OnReceive = HPSocketDLL.HP_Set_FN_HttpServer_OnReceive if hasattr(HPSocketDLL, "HP_Set_FN_HttpServer_OnReceive") else None
if HP_Set_FN_HttpServer_OnReceive:
    HP_Set_FN_HttpServer_OnReceive.restype = None
    HP_Set_FN_HttpServer_OnReceive.argtypes = [HP_HttpServerListener, HP_FN_HttpServer_OnReceive]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpServer_OnSend(HP_HttpServerListener pListener				, HP_FN_HttpServer_OnSend fn);
HP_Set_FN_HttpServer_OnSend = HPSocketDLL.HP_Set_FN_HttpServer_OnSend if hasattr(HPSocketDLL, "HP_Set_FN_HttpServer_OnSend") else None
if HP_Set_FN_HttpServer_OnSend:
    HP_Set_FN_HttpServer_OnSend.restype = None
    HP_Set_FN_HttpServer_OnSend.argtypes = [HP_HttpServerListener, HP_FN_HttpServer_OnSend]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpServer_OnClose(HP_HttpServerListener pListener			, HP_FN_HttpServer_OnClose fn);
HP_Set_FN_HttpServer_OnClose = HPSocketDLL.HP_Set_FN_HttpServer_OnClose if hasattr(HPSocketDLL, "HP_Set_FN_HttpServer_OnClose") else None
if HP_Set_FN_HttpServer_OnClose:
    HP_Set_FN_HttpServer_OnClose.restype = None
    HP_Set_FN_HttpServer_OnClose.argtypes = [HP_HttpServerListener, HP_FN_HttpServer_OnClose]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpServer_OnShutdown(HP_HttpServerListener pListener			, HP_FN_HttpServer_OnShutdown fn);
HP_Set_FN_HttpServer_OnShutdown = HPSocketDLL.HP_Set_FN_HttpServer_OnShutdown if hasattr(HPSocketDLL, "HP_Set_FN_HttpServer_OnShutdown") else None
if HP_Set_FN_HttpServer_OnShutdown:
    HP_Set_FN_HttpServer_OnShutdown.restype = None
    HP_Set_FN_HttpServer_OnShutdown.argtypes = [HP_HttpServerListener, HP_FN_HttpServer_OnShutdown]

# ********************************************************************************
# *************************** HTTP Agent 回调函数设置方法 *************************

# HPSOCKET_API void __stdcall HP_Set_FN_HttpAgent_OnMessageBegin(HP_HttpAgentListener pListener		, HP_FN_HttpAgent_OnMessageBegin fn);
HP_Set_FN_HttpAgent_OnMessageBegin = HPSocketDLL.HP_Set_FN_HttpAgent_OnMessageBegin if hasattr(HPSocketDLL, "HP_Set_FN_HttpAgent_OnMessageBegin") else None
if HP_Set_FN_HttpAgent_OnMessageBegin:
    HP_Set_FN_HttpAgent_OnMessageBegin.restype = None
    HP_Set_FN_HttpAgent_OnMessageBegin.argtypes = [HP_HttpAgentListener, HP_FN_HttpAgent_OnMessageBegin]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpAgent_OnStatusLine(HP_HttpAgentListener pListener			, HP_FN_HttpAgent_OnStatusLine fn);
HP_Set_FN_HttpAgent_OnStatusLine = HPSocketDLL.HP_Set_FN_HttpAgent_OnStatusLine if hasattr(HPSocketDLL, "HP_Set_FN_HttpAgent_OnStatusLine") else None
if HP_Set_FN_HttpAgent_OnStatusLine:
    HP_Set_FN_HttpAgent_OnStatusLine.restype = None
    HP_Set_FN_HttpAgent_OnStatusLine.argtypes = [HP_HttpAgentListener, HP_FN_HttpAgent_OnStatusLine]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpAgent_OnHeader(HP_HttpAgentListener pListener				, HP_FN_HttpAgent_OnHeader fn);
HP_Set_FN_HttpAgent_OnHeader = HPSocketDLL.HP_Set_FN_HttpAgent_OnHeader if hasattr(HPSocketDLL, "HP_Set_FN_HttpAgent_OnHeader") else None
if HP_Set_FN_HttpAgent_OnHeader:
    HP_Set_FN_HttpAgent_OnHeader.restype = None
    HP_Set_FN_HttpAgent_OnHeader.argtypes = [HP_HttpAgentListener, HP_FN_HttpAgent_OnHeader]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpAgent_OnHeadersComplete(HP_HttpAgentListener pListener	, HP_FN_HttpAgent_OnHeadersComplete fn);
HP_Set_FN_HttpAgent_OnHeadersComplete = HPSocketDLL.HP_Set_FN_HttpAgent_OnHeadersComplete if hasattr(HPSocketDLL, "HP_Set_FN_HttpAgent_OnHeadersComplete") else None
if HP_Set_FN_HttpAgent_OnHeadersComplete:
    HP_Set_FN_HttpAgent_OnHeadersComplete.restype = None
    HP_Set_FN_HttpAgent_OnHeadersComplete.argtypes = [HP_HttpAgentListener, HP_FN_HttpAgent_OnHeadersComplete]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpAgent_OnBody(HP_HttpAgentListener pListener				, HP_FN_HttpAgent_OnBody fn);
HP_Set_FN_HttpAgent_OnBody = HPSocketDLL.HP_Set_FN_HttpAgent_OnBody if hasattr(HPSocketDLL, "HP_Set_FN_HttpAgent_OnBody") else None
if HP_Set_FN_HttpAgent_OnBody:
    HP_Set_FN_HttpAgent_OnBody.restype = None
    HP_Set_FN_HttpAgent_OnBody.argtypes = [HP_HttpAgentListener, HP_FN_HttpAgent_OnBody]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpAgent_OnChunkHeader(HP_HttpAgentListener pListener		, HP_FN_HttpAgent_OnChunkHeader fn);
HP_Set_FN_HttpAgent_OnChunkHeader = HPSocketDLL.HP_Set_FN_HttpAgent_OnChunkHeader if hasattr(HPSocketDLL, "HP_Set_FN_HttpAgent_OnChunkHeader") else None
if HP_Set_FN_HttpAgent_OnChunkHeader:
    HP_Set_FN_HttpAgent_OnChunkHeader.restype = None
    HP_Set_FN_HttpAgent_OnChunkHeader.argtypes = [HP_HttpAgentListener, HP_FN_HttpAgent_OnChunkHeader]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpAgent_OnChunkComplete(HP_HttpAgentListener pListener		, HP_FN_HttpAgent_OnChunkComplete fn);
HP_Set_FN_HttpAgent_OnChunkComplete = HPSocketDLL.HP_Set_FN_HttpAgent_OnChunkComplete if hasattr(HPSocketDLL, "HP_Set_FN_HttpAgent_OnChunkComplete") else None
if HP_Set_FN_HttpAgent_OnChunkComplete:
    HP_Set_FN_HttpAgent_OnChunkComplete.restype = None
    HP_Set_FN_HttpAgent_OnChunkComplete.argtypes = [HP_HttpAgentListener, HP_FN_HttpAgent_OnChunkComplete]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpAgent_OnMessageComplete(HP_HttpAgentListener pListener	, HP_FN_HttpAgent_OnMessageComplete fn);
HP_Set_FN_HttpAgent_OnMessageComplete = HPSocketDLL.HP_Set_FN_HttpAgent_OnMessageComplete if hasattr(HPSocketDLL, "HP_Set_FN_HttpAgent_OnMessageComplete") else None
if HP_Set_FN_HttpAgent_OnMessageComplete:
    HP_Set_FN_HttpAgent_OnMessageComplete.restype = None
    HP_Set_FN_HttpAgent_OnMessageComplete.argtypes = [HP_HttpAgentListener, HP_FN_HttpAgent_OnMessageComplete]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpAgent_OnUpgrade(HP_HttpAgentListener pListener			, HP_FN_HttpAgent_OnUpgrade fn);
HP_Set_FN_HttpAgent_OnUpgrade = HPSocketDLL.HP_Set_FN_HttpAgent_OnUpgrade if hasattr(HPSocketDLL, "HP_Set_FN_HttpAgent_OnUpgrade") else None
if HP_Set_FN_HttpAgent_OnUpgrade:
    HP_Set_FN_HttpAgent_OnUpgrade.restype = None
    HP_Set_FN_HttpAgent_OnUpgrade.argtypes = [HP_HttpAgentListener, HP_FN_HttpAgent_OnUpgrade]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpAgent_OnParseError(HP_HttpAgentListener pListener			, HP_FN_HttpAgent_OnParseError fn);
HP_Set_FN_HttpAgent_OnParseError = HPSocketDLL.HP_Set_FN_HttpAgent_OnParseError if hasattr(HPSocketDLL, "HP_Set_FN_HttpAgent_OnParseError") else None
if HP_Set_FN_HttpAgent_OnParseError:
    HP_Set_FN_HttpAgent_OnParseError.restype = None
    HP_Set_FN_HttpAgent_OnParseError.argtypes = [HP_HttpAgentListener, HP_FN_HttpAgent_OnParseError]

# HPSOCKET_API void __stdcall HP_Set_FN_HttpAgent_OnWSMessageHeader(HP_HttpAgentListener pListener	, HP_FN_HttpAgent_OnWSMessageHeader fn);
HP_Set_FN_HttpAgent_OnWSMessageHeader = HPSocketDLL.HP_Set_FN_HttpAgent_OnWSMessageHeader if hasattr(HPSocketDLL, "HP_Set_FN_HttpAgent_OnWSMessageHeader") else None
if HP_Set_FN_HttpAgent_OnWSMessageHeader:
    HP_Set_FN_HttpAgent_OnWSMessageHeader.restype = None
    HP_Set_FN_HttpAgent_OnWSMessageHeader.argtypes = [HP_HttpAgentListener, HP_FN_HttpAgent_OnWSMessageHeader]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpAgent_OnWSMessageBody(HP_HttpAgentListener pListener		, HP_FN_HttpAgent_OnWSMessageBody fn);
HP_Set_FN_HttpAgent_OnWSMessageBody = HPSocketDLL.HP_Set_FN_HttpAgent_OnWSMessageBody if hasattr(HPSocketDLL, "HP_Set_FN_HttpAgent_OnWSMessageBody") else None
if HP_Set_FN_HttpAgent_OnWSMessageBody:
    HP_Set_FN_HttpAgent_OnWSMessageBody.restype = None
    HP_Set_FN_HttpAgent_OnWSMessageBody.argtypes = [HP_HttpAgentListener, HP_FN_HttpAgent_OnWSMessageBody]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpAgent_OnWSMessageComplete(HP_HttpAgentListener pListener	, HP_FN_HttpAgent_OnWSMessageComplete fn);
HP_Set_FN_HttpAgent_OnWSMessageComplete = HPSocketDLL.HP_Set_FN_HttpAgent_OnWSMessageComplete if hasattr(HPSocketDLL, "HP_Set_FN_HttpAgent_OnWSMessageComplete") else None
if HP_Set_FN_HttpAgent_OnWSMessageComplete:
    HP_Set_FN_HttpAgent_OnWSMessageComplete.restype = None
    HP_Set_FN_HttpAgent_OnWSMessageComplete.argtypes = [HP_HttpAgentListener, HP_FN_HttpAgent_OnWSMessageComplete]

# HPSOCKET_API void __stdcall HP_Set_FN_HttpAgent_OnPrepareConnect(HP_HttpAgentListener pListener		, HP_FN_HttpAgent_OnPrepareConnect fn);
HP_Set_FN_HttpAgent_OnPrepareConnect = HPSocketDLL.HP_Set_FN_HttpAgent_OnPrepareConnect if hasattr(HPSocketDLL, "HP_Set_FN_HttpAgent_OnPrepareConnect") else None
if HP_Set_FN_HttpAgent_OnPrepareConnect:
    HP_Set_FN_HttpAgent_OnPrepareConnect.restype = None
    HP_Set_FN_HttpAgent_OnPrepareConnect.argtypes = [HP_HttpAgentListener, HP_FN_HttpAgent_OnPrepareConnect]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpAgent_OnConnect(HP_HttpAgentListener pListener			, HP_FN_HttpAgent_OnConnect fn);
HP_Set_FN_HttpAgent_OnConnect = HPSocketDLL.HP_Set_FN_HttpAgent_OnConnect if hasattr(HPSocketDLL, "HP_Set_FN_HttpAgent_OnConnect") else None
if HP_Set_FN_HttpAgent_OnConnect:
    HP_Set_FN_HttpAgent_OnConnect.restype = None
    HP_Set_FN_HttpAgent_OnConnect.argtypes = [HP_HttpAgentListener, HP_FN_HttpAgent_OnConnect]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpAgent_OnHandShake(HP_HttpAgentListener pListener			, HP_FN_HttpAgent_OnHandShake fn);
HP_Set_FN_HttpAgent_OnHandShake = HPSocketDLL.HP_Set_FN_HttpAgent_OnHandShake if hasattr(HPSocketDLL, "HP_Set_FN_HttpAgent_OnHandShake") else None
if HP_Set_FN_HttpAgent_OnHandShake:
    HP_Set_FN_HttpAgent_OnHandShake.restype = None
    HP_Set_FN_HttpAgent_OnHandShake.argtypes = [HP_HttpAgentListener, HP_FN_HttpAgent_OnHandShake]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpAgent_OnReceive(HP_HttpAgentListener pListener			, HP_FN_HttpAgent_OnReceive fn);
HP_Set_FN_HttpAgent_OnReceive = HPSocketDLL.HP_Set_FN_HttpAgent_OnReceive if hasattr(HPSocketDLL, "HP_Set_FN_HttpAgent_OnReceive") else None
if HP_Set_FN_HttpAgent_OnReceive:
    HP_Set_FN_HttpAgent_OnReceive.restype = None
    HP_Set_FN_HttpAgent_OnReceive.argtypes = [HP_HttpAgentListener, HP_FN_HttpAgent_OnReceive]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpAgent_OnSend(HP_HttpAgentListener pListener				, HP_FN_HttpAgent_OnSend fn);
HP_Set_FN_HttpAgent_OnSend = HPSocketDLL.HP_Set_FN_HttpAgent_OnSend if hasattr(HPSocketDLL, "HP_Set_FN_HttpAgent_OnSend") else None
if HP_Set_FN_HttpAgent_OnSend:
    HP_Set_FN_HttpAgent_OnSend.restype = None
    HP_Set_FN_HttpAgent_OnSend.argtypes = [HP_HttpAgentListener, HP_FN_HttpAgent_OnSend]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpAgent_OnClose(HP_HttpAgentListener pListener				, HP_FN_HttpAgent_OnClose fn);
HP_Set_FN_HttpAgent_OnClose = HPSocketDLL.HP_Set_FN_HttpAgent_OnClose if hasattr(HPSocketDLL, "HP_Set_FN_HttpAgent_OnClose") else None
if HP_Set_FN_HttpAgent_OnClose:
    HP_Set_FN_HttpAgent_OnClose.restype = None
    HP_Set_FN_HttpAgent_OnClose.argtypes = [HP_HttpAgentListener, HP_FN_HttpAgent_OnClose]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpAgent_OnShutdown(HP_HttpAgentListener pListener			, HP_FN_HttpAgent_OnShutdown fn);
HP_Set_FN_HttpAgent_OnShutdown = HPSocketDLL.HP_Set_FN_HttpAgent_OnShutdown if hasattr(HPSocketDLL, "HP_Set_FN_HttpAgent_OnShutdown") else None
if HP_Set_FN_HttpAgent_OnShutdown:
    HP_Set_FN_HttpAgent_OnShutdown.restype = None
    HP_Set_FN_HttpAgent_OnShutdown.argtypes = [HP_HttpAgentListener, HP_FN_HttpAgent_OnShutdown]

# ********************************************************************************
# ************************** HTTP Client 回调函数设置方法 *************************

# HPSOCKET_API void __stdcall HP_Set_FN_HttpClient_OnMessageBegin(HP_HttpClientListener pListener		, HP_FN_HttpClient_OnMessageBegin fn);
HP_Set_FN_HttpClient_OnMessageBegin = HPSocketDLL.HP_Set_FN_HttpClient_OnMessageBegin if hasattr(HPSocketDLL, "HP_Set_FN_HttpClient_OnMessageBegin") else None
if HP_Set_FN_HttpClient_OnMessageBegin:
    HP_Set_FN_HttpClient_OnMessageBegin.restype = None
    HP_Set_FN_HttpClient_OnMessageBegin.argtypes = [HP_HttpClientListener, HP_FN_HttpClient_OnMessageBegin]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpClient_OnStatusLine(HP_HttpClientListener pListener		, HP_FN_HttpClient_OnStatusLine fn);
HP_Set_FN_HttpClient_OnStatusLine = HPSocketDLL.HP_Set_FN_HttpClient_OnStatusLine if hasattr(HPSocketDLL, "HP_Set_FN_HttpClient_OnStatusLine") else None
if HP_Set_FN_HttpClient_OnStatusLine:
    HP_Set_FN_HttpClient_OnStatusLine.restype = None
    HP_Set_FN_HttpClient_OnStatusLine.argtypes = [HP_HttpClientListener, HP_FN_HttpClient_OnStatusLine]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpClient_OnHeader(HP_HttpClientListener pListener			, HP_FN_HttpClient_OnHeader fn);
HP_Set_FN_HttpClient_OnHeader = HPSocketDLL.HP_Set_FN_HttpClient_OnHeader if hasattr(HPSocketDLL, "HP_Set_FN_HttpClient_OnHeader") else None
if HP_Set_FN_HttpClient_OnHeader:
    HP_Set_FN_HttpClient_OnHeader.restype = None
    HP_Set_FN_HttpClient_OnHeader.argtypes = [HP_HttpClientListener, HP_FN_HttpClient_OnHeader]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpClient_OnHeadersComplete(HP_HttpClientListener pListener	, HP_FN_HttpClient_OnHeadersComplete fn);
HP_Set_FN_HttpClient_OnHeadersComplete = HPSocketDLL.HP_Set_FN_HttpClient_OnHeadersComplete if hasattr(HPSocketDLL, "HP_Set_FN_HttpClient_OnHeadersComplete") else None
if HP_Set_FN_HttpClient_OnHeadersComplete:
    HP_Set_FN_HttpClient_OnHeadersComplete.restype = None
    HP_Set_FN_HttpClient_OnHeadersComplete.argtypes = [HP_HttpClientListener, HP_FN_HttpClient_OnHeadersComplete]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpClient_OnBody(HP_HttpClientListener pListener				, HP_FN_HttpClient_OnBody fn);
HP_Set_FN_HttpClient_OnBody = HPSocketDLL.HP_Set_FN_HttpClient_OnBody if hasattr(HPSocketDLL, "HP_Set_FN_HttpClient_OnBody") else None
if HP_Set_FN_HttpClient_OnBody:
    HP_Set_FN_HttpClient_OnBody.restype = None
    HP_Set_FN_HttpClient_OnBody.argtypes = [HP_HttpClientListener, HP_FN_HttpClient_OnBody]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpClient_OnChunkHeader(HP_HttpClientListener pListener		, HP_FN_HttpClient_OnChunkHeader fn);
HP_Set_FN_HttpClient_OnChunkHeader = HPSocketDLL.HP_Set_FN_HttpClient_OnChunkHeader if hasattr(HPSocketDLL, "HP_Set_FN_HttpClient_OnChunkHeader") else None
if HP_Set_FN_HttpClient_OnChunkHeader:
    HP_Set_FN_HttpClient_OnChunkHeader.restype = None
    HP_Set_FN_HttpClient_OnChunkHeader.argtypes = [HP_HttpClientListener, HP_FN_HttpClient_OnChunkHeader]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpClient_OnChunkComplete(HP_HttpClientListener pListener	, HP_FN_HttpClient_OnChunkComplete fn);
HP_Set_FN_HttpClient_OnChunkComplete = HPSocketDLL.HP_Set_FN_HttpClient_OnChunkComplete if hasattr(HPSocketDLL, "HP_Set_FN_HttpClient_OnChunkComplete") else None
if HP_Set_FN_HttpClient_OnChunkComplete:
    HP_Set_FN_HttpClient_OnChunkComplete.restype = None
    HP_Set_FN_HttpClient_OnChunkComplete.argtypes = [HP_HttpClientListener, HP_FN_HttpClient_OnChunkComplete]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpClient_OnMessageComplete(HP_HttpClientListener pListener	, HP_FN_HttpClient_OnMessageComplete fn);
HP_Set_FN_HttpClient_OnMessageComplete = HPSocketDLL.HP_Set_FN_HttpClient_OnMessageComplete if hasattr(HPSocketDLL, "HP_Set_FN_HttpClient_OnMessageComplete") else None
if HP_Set_FN_HttpClient_OnMessageComplete:
    HP_Set_FN_HttpClient_OnMessageComplete.restype = None
    HP_Set_FN_HttpClient_OnMessageComplete.argtypes = [HP_HttpClientListener, HP_FN_HttpClient_OnMessageComplete]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpClient_OnUpgrade(HP_HttpClientListener pListener			, HP_FN_HttpClient_OnUpgrade fn);
HP_Set_FN_HttpClient_OnUpgrade = HPSocketDLL.HP_Set_FN_HttpClient_OnUpgrade if hasattr(HPSocketDLL, "HP_Set_FN_HttpClient_OnUpgrade") else None
if HP_Set_FN_HttpClient_OnUpgrade:
    HP_Set_FN_HttpClient_OnUpgrade.restype = None
    HP_Set_FN_HttpClient_OnUpgrade.argtypes = [HP_HttpClientListener, HP_FN_HttpClient_OnUpgrade]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpClient_OnParseError(HP_HttpClientListener pListener		, HP_FN_HttpClient_OnParseError fn);
HP_Set_FN_HttpClient_OnParseError = HPSocketDLL.HP_Set_FN_HttpClient_OnParseError if hasattr(HPSocketDLL, "HP_Set_FN_HttpClient_OnParseError") else None
if HP_Set_FN_HttpClient_OnParseError:
    HP_Set_FN_HttpClient_OnParseError.restype = None
    HP_Set_FN_HttpClient_OnParseError.argtypes = [HP_HttpClientListener, HP_FN_HttpClient_OnParseError]

# HPSOCKET_API void __stdcall HP_Set_FN_HttpClient_OnWSMessageHeader(HP_HttpClientListener pListener	, HP_FN_HttpClient_OnWSMessageHeader fn);
HP_Set_FN_HttpClient_OnWSMessageHeader = HPSocketDLL.HP_Set_FN_HttpClient_OnWSMessageHeader if hasattr(HPSocketDLL, "HP_Set_FN_HttpClient_OnWSMessageHeader") else None
if HP_Set_FN_HttpClient_OnWSMessageHeader:
    HP_Set_FN_HttpClient_OnWSMessageHeader.restype = None
    HP_Set_FN_HttpClient_OnWSMessageHeader.argtypes = [HP_HttpClientListener, HP_FN_HttpClient_OnWSMessageHeader]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpClient_OnWSMessageBody(HP_HttpClientListener pListener	, HP_FN_HttpClient_OnWSMessageBody fn);
HP_Set_FN_HttpClient_OnWSMessageBody = HPSocketDLL.HP_Set_FN_HttpClient_OnWSMessageBody if hasattr(HPSocketDLL, "HP_Set_FN_HttpClient_OnWSMessageBody") else None
if HP_Set_FN_HttpClient_OnWSMessageBody:
    HP_Set_FN_HttpClient_OnWSMessageBody.restype = None
    HP_Set_FN_HttpClient_OnWSMessageBody.argtypes = [HP_HttpClientListener, HP_FN_HttpClient_OnWSMessageBody]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpClient_OnWSMessageComplete(HP_HttpClientListener pListener, HP_FN_HttpClient_OnWSMessageComplete fn);
HP_Set_FN_HttpClient_OnWSMessageComplete = HPSocketDLL.HP_Set_FN_HttpClient_OnWSMessageComplete if hasattr(HPSocketDLL, "HP_Set_FN_HttpClient_OnWSMessageComplete") else None
if HP_Set_FN_HttpClient_OnWSMessageComplete:
    HP_Set_FN_HttpClient_OnWSMessageComplete.restype = None
    HP_Set_FN_HttpClient_OnWSMessageComplete.argtypes = [HP_HttpClientListener, HP_FN_HttpClient_OnWSMessageComplete]

# HPSOCKET_API void __stdcall HP_Set_FN_HttpClient_OnPrepareConnect(HP_HttpClientListener pListener	, HP_FN_HttpClient_OnPrepareConnect fn);
HP_Set_FN_HttpClient_OnPrepareConnect = HPSocketDLL.HP_Set_FN_HttpClient_OnPrepareConnect if hasattr(HPSocketDLL, "HP_Set_FN_HttpClient_OnPrepareConnect") else None
if HP_Set_FN_HttpClient_OnPrepareConnect:
    HP_Set_FN_HttpClient_OnPrepareConnect.restype = None
    HP_Set_FN_HttpClient_OnPrepareConnect.argtypes = [HP_HttpClientListener, HP_FN_HttpClient_OnPrepareConnect]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpClient_OnConnect(HP_HttpClientListener pListener			, HP_FN_HttpClient_OnConnect fn);
HP_Set_FN_HttpClient_OnConnect = HPSocketDLL.HP_Set_FN_HttpClient_OnConnect if hasattr(HPSocketDLL, "HP_Set_FN_HttpClient_OnConnect") else None
if HP_Set_FN_HttpClient_OnConnect:
    HP_Set_FN_HttpClient_OnConnect.restype = None
    HP_Set_FN_HttpClient_OnConnect.argtypes = [HP_HttpClientListener, HP_FN_HttpClient_OnConnect]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpClient_OnHandShake(HP_HttpClientListener pListener		, HP_FN_HttpClient_OnHandShake fn);
HP_Set_FN_HttpClient_OnHandShake = HPSocketDLL.HP_Set_FN_HttpClient_OnHandShake if hasattr(HPSocketDLL, "HP_Set_FN_HttpClient_OnHandShake") else None
if HP_Set_FN_HttpClient_OnHandShake:
    HP_Set_FN_HttpClient_OnHandShake.restype = None
    HP_Set_FN_HttpClient_OnHandShake.argtypes = [HP_HttpClientListener, HP_FN_HttpClient_OnHandShake]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpClient_OnReceive(HP_HttpClientListener pListener			, HP_FN_HttpClient_OnReceive fn);
HP_Set_FN_HttpClient_OnReceive = HPSocketDLL.HP_Set_FN_HttpClient_OnReceive if hasattr(HPSocketDLL, "HP_Set_FN_HttpClient_OnReceive") else None
if HP_Set_FN_HttpClient_OnReceive:
    HP_Set_FN_HttpClient_OnReceive.restype = None
    HP_Set_FN_HttpClient_OnReceive.argtypes = [HP_HttpClientListener, HP_FN_HttpClient_OnReceive]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpClient_OnSend(HP_HttpClientListener pListener				, HP_FN_HttpClient_OnSend fn);
HP_Set_FN_HttpClient_OnSend = HPSocketDLL.HP_Set_FN_HttpClient_OnSend if hasattr(HPSocketDLL, "HP_Set_FN_HttpClient_OnSend") else None
if HP_Set_FN_HttpClient_OnSend:
    HP_Set_FN_HttpClient_OnSend.restype = None
    HP_Set_FN_HttpClient_OnSend.argtypes = [HP_HttpClientListener, HP_FN_HttpClient_OnSend]
# HPSOCKET_API void __stdcall HP_Set_FN_HttpClient_OnClose(HP_HttpClientListener pListener			, HP_FN_HttpClient_OnClose fn);
HP_Set_FN_HttpClient_OnClose = HPSocketDLL.HP_Set_FN_HttpClient_OnClose if hasattr(HPSocketDLL, "HP_Set_FN_HttpClient_OnClose") else None
if HP_Set_FN_HttpClient_OnClose:
    HP_Set_FN_HttpClient_OnClose.restype = None
    HP_Set_FN_HttpClient_OnClose.argtypes = [HP_HttpClientListener, HP_FN_HttpClient_OnClose]

# ************************************************************************
# ************************** HTTP Server 操作方法 *************************

#
# * 名称：回复请求
# * 描述：向客户端回复 HTTP 请求
# *
# * 参数：		dwConnID		-- 连接 ID
# *			usStatusCode	-- HTTP 状态码
# *			lpszDesc		-- HTTP 状态描述
# *			lpHeaders		-- 回复请求头
# *			iHeaderCount	-- 回复请求头数量
# *			pData			-- 回复请求体
# *			iLength			-- 回复请求体长度
# * 返回值：	TRUE			-- 成功
# *			FALSE			-- 失败
#
# HPSOCKET_API BOOL __stdcall HP_HttpServer_SendResponse(HP_HttpServer pServer, HP_CONNID dwConnID, USHORT usStatusCode, LPCSTR lpszDesc, const HP_THeader lpHeaders[], int iHeaderCount, const BYTE* pData, int iLength);
HP_HttpServer_SendResponse = HPSocketDLL.HP_HttpServer_SendResponse if hasattr(HPSocketDLL, "HP_HttpServer_SendResponse") else None
if HP_HttpServer_SendResponse:
    HP_HttpServer_SendResponse.restype = ctypes.c_bool
    HP_HttpServer_SendResponse.argtypes = [HP_HttpServer, HP_CONNID, ctypes.c_ushort, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int, ctypes.POINTER(ctypes.c_byte), ctypes.c_int]

#
# * 名称：发送本地文件
# * 描述：向指定连接发送 4096 KB 以下的小文件
# *
# * 参数：		dwConnID		-- 连接 ID
# *			lpszFileName	-- 文件路径
# *			usStatusCode	-- HTTP 状态码
# *			lpszDesc		-- HTTP 状态描述
# *			lpHeaders		-- 回复请求头
# *			iHeaderCount	-- 回复请求头数量
# * 返回值：	TRUE			-- 成功
# *			FALSE			-- 失败
#
# HPSOCKET_API BOOL __stdcall HP_HttpServer_SendLocalFile(HP_HttpServer pServer, HP_CONNID dwConnID, LPCSTR lpszFileName, USHORT usStatusCode, LPCSTR lpszDesc, const HP_THeader lpHeaders[], int iHeaderCount);
HP_HttpServer_SendLocalFile = HPSocketDLL.HP_HttpServer_SendLocalFile if hasattr(HPSocketDLL, "HP_HttpServer_SendLocalFile") else None
if HP_HttpServer_SendLocalFile:
    HP_HttpServer_SendLocalFile.restype = ctypes.c_bool
    HP_HttpServer_SendLocalFile.argtypes = [HP_HttpServer, HP_CONNID, ctypes.c_char_p, ctypes.c_ushort, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int]

#
# * 名称：发送 WebSocket 消息
# * 描述：向对端端发送 WebSocket 消息
# *
# * 参数：		dwConnID		-- 连接 ID
# *			bFinal			-- 是否结束帧
# *			iReserved		-- RSV1/RSV2/RSV3 各 1 位
# *			iOperationCode	-- 操作码：0x0 - 0xF
# *			lpszMask		-- 掩码（nullptr 或 4 字节掩码，如果为 nullptr 则没有掩码）
# *			pData			-- 消息体数据缓冲区
# *			iLength			-- 消息体数据长度
# *			ullBodyLen		-- 消息总长度
# * 								ullBodyLen = 0		 -> 消息总长度为 iLength
# * 								ullBodyLen = iLength -> 消息总长度为 ullBodyLen
# * 								ullBodyLen > iLength -> 消息总长度为 ullBodyLen，后续消息体长度为 ullBOdyLen - iLength，后续消息体通过底层方法 Send() / SendPackets() 发送
# * 								ullBodyLen < iLength -> 错误参数，发送失败
# * 返回值：	TRUE			-- 成功
# *			FALSE			-- 失败
#
# HPSOCKET_API BOOL __stdcall HP_HttpServer_SendWSMessage(HP_HttpServer pServer, HP_CONNID dwConnID, BOOL bFinal, BYTE iReserved, BYTE iOperationCode, const int lpszMask, BYTE* pData, int iLength, ULONGLONG ullBodyLen);
HP_HttpServer_SendWSMessage = HPSocketDLL.HP_HttpServer_SendWSMessage if hasattr(HPSocketDLL, "HP_HttpServer_SendWSMessage") else None
if HP_HttpServer_SendWSMessage:
    HP_HttpServer_SendWSMessage.restype = ctypes.c_bool
    HP_HttpServer_SendWSMessage.argtypes = [HP_HttpServer, HP_CONNID, ctypes.c_bool, ctypes.c_byte, ctypes.c_byte, ctypes.c_int, ctypes.POINTER(ctypes.c_byte), ctypes.c_int, ctypes.c_ulonglong]

#
# * 名称：释放连接
# * 描述：把连接放入释放队列，等待某个时间（通过 SetReleaseDelay() 设置）关闭连接
# *
# * 参数：		dwConnID		-- 连接 ID
# * 返回值：	TRUE			-- 成功
# *			FALSE			-- 失败
#
# HPSOCKET_API BOOL __stdcall HP_HttpServer_Release(HP_HttpServer pServer, HP_CONNID dwConnID);
HP_HttpServer_Release = HPSocketDLL.HP_HttpServer_Release if hasattr(HPSocketDLL, "HP_HttpServer_Release") else None
if HP_HttpServer_Release:
    HP_HttpServer_Release.restype = ctypes.c_bool
    HP_HttpServer_Release.argtypes = [HP_HttpServer, HP_CONNID]

# ****************************************************************************
# ************************** HTTP Server 属性访问方法 *************************

#  设置连接释放延时（默认：3000 毫秒）
# HPSOCKET_API void __stdcall HP_HttpServer_SetReleaseDelay(HP_HttpServer pServer, DWORD dwReleaseDelay);
HP_HttpServer_SetReleaseDelay = HPSocketDLL.HP_HttpServer_SetReleaseDelay if hasattr(HPSocketDLL, "HP_HttpServer_SetReleaseDelay") else None
if HP_HttpServer_SetReleaseDelay:
    HP_HttpServer_SetReleaseDelay.restype = None
    HP_HttpServer_SetReleaseDelay.argtypes = [HP_HttpServer, ctypes.c_uint]
#  获取连接释放延时
# HPSOCKET_API DWORD __stdcall HP_HttpServer_GetReleaseDelay(HP_HttpServer pServer);
HP_HttpServer_GetReleaseDelay = HPSocketDLL.HP_HttpServer_GetReleaseDelay if hasattr(HPSocketDLL, "HP_HttpServer_GetReleaseDelay") else None
if HP_HttpServer_GetReleaseDelay:
    HP_HttpServer_GetReleaseDelay.restype = ctypes.c_uint
    HP_HttpServer_GetReleaseDelay.argtypes = [HP_HttpServer]
#  获取请求行 URL 域掩码（URL 域参考：EnHttpUrlField）
# HPSOCKET_API USHORT __stdcall HP_HttpServer_GetUrlFieldSet(HP_HttpServer pServer, HP_CONNID dwConnID);
HP_HttpServer_GetUrlFieldSet = HPSocketDLL.HP_HttpServer_GetUrlFieldSet if hasattr(HPSocketDLL, "HP_HttpServer_GetUrlFieldSet") else None
if HP_HttpServer_GetUrlFieldSet:
    HP_HttpServer_GetUrlFieldSet.restype = ctypes.c_ushort
    HP_HttpServer_GetUrlFieldSet.argtypes = [HP_HttpServer, HP_CONNID]
#  获取某个 URL 域值
# HPSOCKET_API LPCSTR __stdcall HP_HttpServer_GetUrlField(HP_HttpServer pServer, HP_CONNID dwConnID, En_HP_HttpUrlField enField);
HP_HttpServer_GetUrlField = HPSocketDLL.HP_HttpServer_GetUrlField if hasattr(HPSocketDLL, "HP_HttpServer_GetUrlField") else None
if HP_HttpServer_GetUrlField:
    HP_HttpServer_GetUrlField.restype = ctypes.c_char_p
    HP_HttpServer_GetUrlField.argtypes = [HP_HttpServer, HP_CONNID, En_HP_HttpUrlField]
#  获取请求方法
# HPSOCKET_API LPCSTR __stdcall HP_HttpServer_GetMethod(HP_HttpServer pServer, HP_CONNID dwConnID);
HP_HttpServer_GetMethod = HPSocketDLL.HP_HttpServer_GetMethod if hasattr(HPSocketDLL, "HP_HttpServer_GetMethod") else None
if HP_HttpServer_GetMethod:
    HP_HttpServer_GetMethod.restype = ctypes.c_char_p
    HP_HttpServer_GetMethod.argtypes = [HP_HttpServer, HP_CONNID]

#  设置本地协议版本
# HPSOCKET_API void __stdcall HP_HttpServer_SetLocalVersion(HP_HttpServer pServer, En_HP_HttpVersion usVersion);
HP_HttpServer_SetLocalVersion = HPSocketDLL.HP_HttpServer_SetLocalVersion if hasattr(HPSocketDLL, "HP_HttpServer_SetLocalVersion") else None
if HP_HttpServer_SetLocalVersion:
    HP_HttpServer_SetLocalVersion.restype = None
    HP_HttpServer_SetLocalVersion.argtypes = [HP_HttpServer, En_HP_HttpVersion]
#  获取本地协议版本
# HPSOCKET_API En_HP_HttpVersion __stdcall HP_HttpServer_GetLocalVersion(HP_HttpServer pServer);
HP_HttpServer_GetLocalVersion = HPSocketDLL.HP_HttpServer_GetLocalVersion if hasattr(HPSocketDLL, "HP_HttpServer_GetLocalVersion") else None
if HP_HttpServer_GetLocalVersion:
    HP_HttpServer_GetLocalVersion.restype = En_HP_HttpVersion
    HP_HttpServer_GetLocalVersion.argtypes = [HP_HttpServer]

#  检查是否升级协议
# HPSOCKET_API BOOL __stdcall HP_HttpServer_IsUpgrade(HP_HttpServer pServer, HP_CONNID dwConnID);
HP_HttpServer_IsUpgrade = HPSocketDLL.HP_HttpServer_IsUpgrade if hasattr(HPSocketDLL, "HP_HttpServer_IsUpgrade") else None
if HP_HttpServer_IsUpgrade:
    HP_HttpServer_IsUpgrade.restype = ctypes.c_bool
    HP_HttpServer_IsUpgrade.argtypes = [HP_HttpServer, HP_CONNID]
#  检查是否有 Keep-Alive 标识
# HPSOCKET_API BOOL __stdcall HP_HttpServer_IsKeepAlive(HP_HttpServer pServer, HP_CONNID dwConnID);
HP_HttpServer_IsKeepAlive = HPSocketDLL.HP_HttpServer_IsKeepAlive if hasattr(HPSocketDLL, "HP_HttpServer_IsKeepAlive") else None
if HP_HttpServer_IsKeepAlive:
    HP_HttpServer_IsKeepAlive.restype = ctypes.c_bool
    HP_HttpServer_IsKeepAlive.argtypes = [HP_HttpServer, HP_CONNID]
#  获取协议版本
# HPSOCKET_API USHORT __stdcall HP_HttpServer_GetVersion(HP_HttpServer pServer, HP_CONNID dwConnID);
HP_HttpServer_GetVersion = HPSocketDLL.HP_HttpServer_GetVersion if hasattr(HPSocketDLL, "HP_HttpServer_GetVersion") else None
if HP_HttpServer_GetVersion:
    HP_HttpServer_GetVersion.restype = ctypes.c_ushort
    HP_HttpServer_GetVersion.argtypes = [HP_HttpServer, HP_CONNID]
#  获取主机
# HPSOCKET_API LPCSTR __stdcall HP_HttpServer_GetHost(HP_HttpServer pServer, HP_CONNID dwConnID);
HP_HttpServer_GetHost = HPSocketDLL.HP_HttpServer_GetHost if hasattr(HPSocketDLL, "HP_HttpServer_GetHost") else None
if HP_HttpServer_GetHost:
    HP_HttpServer_GetHost.restype = ctypes.c_char_p
    HP_HttpServer_GetHost.argtypes = [HP_HttpServer, HP_CONNID]
#  获取内容长度
# HPSOCKET_API ULONGLONG __stdcall HP_HttpServer_GetContentLength(HP_HttpServer pServer, HP_CONNID dwConnID);
HP_HttpServer_GetContentLength = HPSocketDLL.HP_HttpServer_GetContentLength if hasattr(HPSocketDLL, "HP_HttpServer_GetContentLength") else None
if HP_HttpServer_GetContentLength:
    HP_HttpServer_GetContentLength.restype = ctypes.c_ulonglong
    HP_HttpServer_GetContentLength.argtypes = [HP_HttpServer, HP_CONNID]
#  获取内容类型
# HPSOCKET_API LPCSTR __stdcall HP_HttpServer_GetContentType(HP_HttpServer pServer, HP_CONNID dwConnID);
HP_HttpServer_GetContentType = HPSocketDLL.HP_HttpServer_GetContentType if hasattr(HPSocketDLL, "HP_HttpServer_GetContentType") else None
if HP_HttpServer_GetContentType:
    HP_HttpServer_GetContentType.restype = ctypes.c_char_p
    HP_HttpServer_GetContentType.argtypes = [HP_HttpServer, HP_CONNID]
#  获取内容编码
# HPSOCKET_API LPCSTR __stdcall HP_HttpServer_GetContentEncoding(HP_HttpServer pServer, HP_CONNID dwConnID);
HP_HttpServer_GetContentEncoding = HPSocketDLL.HP_HttpServer_GetContentEncoding if hasattr(HPSocketDLL, "HP_HttpServer_GetContentEncoding") else None
if HP_HttpServer_GetContentEncoding:
    HP_HttpServer_GetContentEncoding.restype = ctypes.c_char_p
    HP_HttpServer_GetContentEncoding.argtypes = [HP_HttpServer, HP_CONNID]
#  获取传输编码
# HPSOCKET_API LPCSTR __stdcall HP_HttpServer_GetTransferEncoding(HP_HttpServer pServer, HP_CONNID dwConnID);
HP_HttpServer_GetTransferEncoding = HPSocketDLL.HP_HttpServer_GetTransferEncoding if hasattr(HPSocketDLL, "HP_HttpServer_GetTransferEncoding") else None
if HP_HttpServer_GetTransferEncoding:
    HP_HttpServer_GetTransferEncoding.restype = ctypes.c_char_p
    HP_HttpServer_GetTransferEncoding.argtypes = [HP_HttpServer, HP_CONNID]
#  获取协议升级类型
# HPSOCKET_API En_HP_HttpUpgradeType __stdcall HP_HttpServer_GetUpgradeType(HP_HttpServer pServer, HP_CONNID dwConnID);
HP_HttpServer_GetUpgradeType = HPSocketDLL.HP_HttpServer_GetUpgradeType if hasattr(HPSocketDLL, "HP_HttpServer_GetUpgradeType") else None
if HP_HttpServer_GetUpgradeType:
    HP_HttpServer_GetUpgradeType.restype = En_HP_HttpUpgradeType
    HP_HttpServer_GetUpgradeType.argtypes = [HP_HttpServer, HP_CONNID]
#  获取解析错误代码
# HPSOCKET_API USHORT __stdcall HP_HttpServer_GetParseErrorCode(HP_HttpServer pServer, HP_CONNID dwConnID, LPCSTR* lpszErrorDesc);
HP_HttpServer_GetParseErrorCode = HPSocketDLL.HP_HttpServer_GetParseErrorCode if hasattr(HPSocketDLL, "HP_HttpServer_GetParseErrorCode") else None
if HP_HttpServer_GetParseErrorCode:
    HP_HttpServer_GetParseErrorCode.restype = ctypes.c_ushort
    HP_HttpServer_GetParseErrorCode.argtypes = [HP_HttpServer, HP_CONNID, ctypes.POINTER(ctypes.c_char_p)]

#  获取某个请求头（单值）
# HPSOCKET_API BOOL __stdcall HP_HttpServer_GetHeader(HP_HttpServer pServer, HP_CONNID dwConnID, LPCSTR lpszName, LPCSTR* lpszValue);
HP_HttpServer_GetHeader = HPSocketDLL.HP_HttpServer_GetHeader if hasattr(HPSocketDLL, "HP_HttpServer_GetHeader") else None
if HP_HttpServer_GetHeader:
    HP_HttpServer_GetHeader.restype = ctypes.c_bool
    HP_HttpServer_GetHeader.argtypes = [HP_HttpServer, HP_CONNID, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p)]
#  获取某个请求头（多值）
# HPSOCKET_API BOOL __stdcall HP_HttpServer_GetHeaders(HP_HttpServer pServer, HP_CONNID dwConnID, LPCSTR lpszName, LPCSTR lpszValue[], DWORD* pdwCount);
HP_HttpServer_GetHeaders = HPSocketDLL.HP_HttpServer_GetHeaders if hasattr(HPSocketDLL, "HP_HttpServer_GetHeaders") else None
if HP_HttpServer_GetHeaders:
    HP_HttpServer_GetHeaders.restype = ctypes.c_bool
    HP_HttpServer_GetHeaders.argtypes = [HP_HttpServer, HP_CONNID, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_uint)]
#  获取所有请求头
# HPSOCKET_API BOOL __stdcall HP_HttpServer_GetAllHeaders(HP_HttpServer pServer, HP_CONNID dwConnID, HP_THeader lpHeaders[], DWORD* pdwCount);
HP_HttpServer_GetAllHeaders = HPSocketDLL.HP_HttpServer_GetAllHeaders if hasattr(HPSocketDLL, "HP_HttpServer_GetAllHeaders") else None
if HP_HttpServer_GetAllHeaders:
    HP_HttpServer_GetAllHeaders.restype = ctypes.c_bool
    HP_HttpServer_GetAllHeaders.argtypes = [HP_HttpServer, HP_CONNID, ctypes.POINTER(HP_THeader), ctypes.POINTER(ctypes.c_uint)]
#  获取所有请求头名称
# HPSOCKET_API BOOL __stdcall HP_HttpServer_GetAllHeaderNames(HP_HttpServer pServer, HP_CONNID dwConnID, LPCSTR lpszName[], DWORD* pdwCount);
HP_HttpServer_GetAllHeaderNames = HPSocketDLL.HP_HttpServer_GetAllHeaderNames if hasattr(HPSocketDLL, "HP_HttpServer_GetAllHeaderNames") else None
if HP_HttpServer_GetAllHeaderNames:
    HP_HttpServer_GetAllHeaderNames.restype = ctypes.c_bool
    HP_HttpServer_GetAllHeaderNames.argtypes = [HP_HttpServer, HP_CONNID, ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_uint)]

#  获取 Cookie
# HPSOCKET_API BOOL __stdcall HP_HttpServer_GetCookie(HP_HttpServer pServer, HP_CONNID dwConnID, LPCSTR lpszName, LPCSTR* lpszValue);
HP_HttpServer_GetCookie = HPSocketDLL.HP_HttpServer_GetCookie if hasattr(HPSocketDLL, "HP_HttpServer_GetCookie") else None
if HP_HttpServer_GetCookie:
    HP_HttpServer_GetCookie.restype = ctypes.c_bool
    HP_HttpServer_GetCookie.argtypes = [HP_HttpServer, HP_CONNID, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p)]
#  获取所有 Cookie
# HPSOCKET_API BOOL __stdcall HP_HttpServer_GetAllCookies(HP_HttpServer pServer, HP_CONNID dwConnID, HP_TCookie lpCookies[], DWORD* pdwCount);
HP_HttpServer_GetAllCookies = HPSocketDLL.HP_HttpServer_GetAllCookies if hasattr(HPSocketDLL, "HP_HttpServer_GetAllCookies") else None
if HP_HttpServer_GetAllCookies:
    HP_HttpServer_GetAllCookies.restype = ctypes.c_bool
    HP_HttpServer_GetAllCookies.argtypes = [HP_HttpServer, HP_CONNID, ctypes.POINTER(HP_TCookie), ctypes.POINTER(ctypes.c_uint)]

#  获取当前 WebSocket 消息状态，传入 nullptr 则不获取相应字段
# HPSOCKET_API BOOL __stdcall HP_HttpServer_GetWSMessageState(HP_HttpServer pServer, HP_CONNID dwConnID, BOOL* lpbFinal, BYTE* lpiReserved, BYTE* lpiOperationCode, LPCBYTE* lpszMask, ULONGLONG* lpullBodyLen, ULONGLONG* lpullBodyRemain);
HP_HttpServer_GetWSMessageState = HPSocketDLL.HP_HttpServer_GetWSMessageState if hasattr(HPSocketDLL, "HP_HttpServer_GetWSMessageState") else None
if HP_HttpServer_GetWSMessageState:
    HP_HttpServer_GetWSMessageState.restype = ctypes.c_bool
    HP_HttpServer_GetWSMessageState.argtypes = [HP_HttpServer, HP_CONNID, ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(LPCBYTE), ctypes.POINTER(ctypes.c_ulonglong), ctypes.POINTER(ctypes.c_ulonglong)]

# ************************************************************************
# ************************** HTTP Agent 操作方法 **************************

#
# * 名称：发送请求
# * 描述：向服务端发送 HTTP 请求
# *
# * 参数：		dwConnID		-- 连接 ID
# *			lpszMethod		-- 请求方法
# *			lpszPath		-- 请求路径
# *			lpHeaders		-- 请求头
# *			iHeaderCount	-- 请求头数量
# *			pBody			-- 请求体
# *			iLength			-- 请求体长度
# * 返回值：	TRUE			-- 成功
# *			FALSE			-- 失败
#
# HPSOCKET_API BOOL __stdcall HP_HttpAgent_SendRequest(HP_HttpAgent pAgent, HP_CONNID dwConnID, LPCSTR lpszMethod, LPCSTR lpszPath, const HP_THeader lpHeaders[], int iHeaderCount, const BYTE* pData, int iLength);
HP_HttpAgent_SendRequest = HPSocketDLL.HP_HttpAgent_SendRequest if hasattr(HPSocketDLL, "HP_HttpAgent_SendRequest") else None
if HP_HttpAgent_SendRequest:
    HP_HttpAgent_SendRequest.restype = ctypes.c_bool
    HP_HttpAgent_SendRequest.argtypes = [HP_HttpAgent, HP_CONNID, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int, ctypes.POINTER(ctypes.c_byte), ctypes.c_int]

#
# * 名称：发送本地文件
# * 描述：向指定连接发送 4096 KB 以下的小文件
# *
# * 参数：		dwConnID		-- 连接 ID
# *			lpszFileName	-- 文件路径
# *			lpszMethod		-- 请求方法
# *			lpszPath		-- 请求路径
# *			lpHeaders		-- 请求头
# *			iHeaderCount	-- 请求头数量
# * 返回值：	TRUE			-- 成功
# *			FALSE			-- 失败
#
# HPSOCKET_API BOOL __stdcall HP_HttpAgent_SendLocalFile(HP_HttpAgent pAgent, HP_CONNID dwConnID, LPCSTR lpszFileName, LPCSTR lpszMethod, LPCSTR lpszPath, const HP_THeader lpHeaders[], int iHeaderCount);
HP_HttpAgent_SendLocalFile = HPSocketDLL.HP_HttpAgent_SendLocalFile if hasattr(HPSocketDLL, "HP_HttpAgent_SendLocalFile") else None
if HP_HttpAgent_SendLocalFile:
    HP_HttpAgent_SendLocalFile.restype = ctypes.c_bool
    HP_HttpAgent_SendLocalFile.argtypes = [HP_HttpAgent, HP_CONNID, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int]

#  发送 POST 请求
# HPSOCKET_API BOOL __stdcall HP_HttpAgent_SendPost(HP_HttpAgent pAgent, HP_CONNID dwConnID, LPCSTR lpszPath, const HP_THeader lpHeaders[], int iHeaderCount, const BYTE* pBody, int iLength);
HP_HttpAgent_SendPost = HPSocketDLL.HP_HttpAgent_SendPost if hasattr(HPSocketDLL, "HP_HttpAgent_SendPost") else None
if HP_HttpAgent_SendPost:
    HP_HttpAgent_SendPost.restype = ctypes.c_bool
    HP_HttpAgent_SendPost.argtypes = [HP_HttpAgent, HP_CONNID, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int, ctypes.POINTER(ctypes.c_byte), ctypes.c_int]
#  发送 PUT 请求
# HPSOCKET_API BOOL __stdcall HP_HttpAgent_SendPut(HP_HttpAgent pAgent, HP_CONNID dwConnID, LPCSTR lpszPath, const HP_THeader lpHeaders[], int iHeaderCount, const BYTE* pBody, int iLength);
HP_HttpAgent_SendPut = HPSocketDLL.HP_HttpAgent_SendPut if hasattr(HPSocketDLL, "HP_HttpAgent_SendPut") else None
if HP_HttpAgent_SendPut:
    HP_HttpAgent_SendPut.restype = ctypes.c_bool
    HP_HttpAgent_SendPut.argtypes = [HP_HttpAgent, HP_CONNID, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int, ctypes.POINTER(ctypes.c_byte), ctypes.c_int]
#  发送 PATCH 请求
# HPSOCKET_API BOOL __stdcall HP_HttpAgent_SendPatch(HP_HttpAgent pAgent, HP_CONNID dwConnID, LPCSTR lpszPath, const HP_THeader lpHeaders[], int iHeaderCount, const BYTE* pBody, int iLength);
HP_HttpAgent_SendPatch = HPSocketDLL.HP_HttpAgent_SendPatch if hasattr(HPSocketDLL, "HP_HttpAgent_SendPatch") else None
if HP_HttpAgent_SendPatch:
    HP_HttpAgent_SendPatch.restype = ctypes.c_bool
    HP_HttpAgent_SendPatch.argtypes = [HP_HttpAgent, HP_CONNID, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int, ctypes.POINTER(ctypes.c_byte), ctypes.c_int]
#  发送 GET 请求
# HPSOCKET_API BOOL __stdcall HP_HttpAgent_SendGet(HP_HttpAgent pAgent, HP_CONNID dwConnID, LPCSTR lpszPath, const HP_THeader lpHeaders[], int iHeaderCount);
HP_HttpAgent_SendGet = HPSocketDLL.HP_HttpAgent_SendGet if hasattr(HPSocketDLL, "HP_HttpAgent_SendGet") else None
if HP_HttpAgent_SendGet:
    HP_HttpAgent_SendGet.restype = ctypes.c_bool
    HP_HttpAgent_SendGet.argtypes = [HP_HttpAgent, HP_CONNID, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int]
#  发送 DELETE 请求
# HPSOCKET_API BOOL __stdcall HP_HttpAgent_SendDelete(HP_HttpAgent pAgent, HP_CONNID dwConnID, LPCSTR lpszPath, const HP_THeader lpHeaders[], int iHeaderCount);
HP_HttpAgent_SendDelete = HPSocketDLL.HP_HttpAgent_SendDelete if hasattr(HPSocketDLL, "HP_HttpAgent_SendDelete") else None
if HP_HttpAgent_SendDelete:
    HP_HttpAgent_SendDelete.restype = ctypes.c_bool
    HP_HttpAgent_SendDelete.argtypes = [HP_HttpAgent, HP_CONNID, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int]
#  发送 HEAD 请求
# HPSOCKET_API BOOL __stdcall HP_HttpAgent_SendHead(HP_HttpAgent pAgent, HP_CONNID dwConnID, LPCSTR lpszPath, const HP_THeader lpHeaders[], int iHeaderCount);
HP_HttpAgent_SendHead = HPSocketDLL.HP_HttpAgent_SendHead if hasattr(HPSocketDLL, "HP_HttpAgent_SendHead") else None
if HP_HttpAgent_SendHead:
    HP_HttpAgent_SendHead.restype = ctypes.c_bool
    HP_HttpAgent_SendHead.argtypes = [HP_HttpAgent, HP_CONNID, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int]
#  发送 TRACE 请求
# HPSOCKET_API BOOL __stdcall HP_HttpAgent_SendTrace(HP_HttpAgent pAgent, HP_CONNID dwConnID, LPCSTR lpszPath, const HP_THeader lpHeaders[], int iHeaderCount);
HP_HttpAgent_SendTrace = HPSocketDLL.HP_HttpAgent_SendTrace if hasattr(HPSocketDLL, "HP_HttpAgent_SendTrace") else None
if HP_HttpAgent_SendTrace:
    HP_HttpAgent_SendTrace.restype = ctypes.c_bool
    HP_HttpAgent_SendTrace.argtypes = [HP_HttpAgent, HP_CONNID, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int]
#  发送 OPTIONS 请求
# HPSOCKET_API BOOL __stdcall HP_HttpAgent_SendOptions(HP_HttpAgent pAgent, HP_CONNID dwConnID, LPCSTR lpszPath, const HP_THeader lpHeaders[], int iHeaderCount);
HP_HttpAgent_SendOptions = HPSocketDLL.HP_HttpAgent_SendOptions if hasattr(HPSocketDLL, "HP_HttpAgent_SendOptions") else None
if HP_HttpAgent_SendOptions:
    HP_HttpAgent_SendOptions.restype = ctypes.c_bool
    HP_HttpAgent_SendOptions.argtypes = [HP_HttpAgent, HP_CONNID, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int]
#  发送 CONNECT 请求
# HPSOCKET_API BOOL __stdcall HP_HttpAgent_SendConnect(HP_HttpAgent pAgent, HP_CONNID dwConnID, LPCSTR lpszHost, const HP_THeader lpHeaders[], int iHeaderCount);
HP_HttpAgent_SendConnect = HPSocketDLL.HP_HttpAgent_SendConnect if hasattr(HPSocketDLL, "HP_HttpAgent_SendConnect") else None
if HP_HttpAgent_SendConnect:
    HP_HttpAgent_SendConnect.restype = ctypes.c_bool
    HP_HttpAgent_SendConnect.argtypes = [HP_HttpAgent, HP_CONNID, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int]

#
# * 名称：发送 WebSocket 消息
# * 描述：向对端端发送 WebSocket 消息
# *
# * 参数：		dwConnID		-- 连接 ID
# *			bFinal			-- 是否结束帧
# *			iReserved		-- RSV1/RSV2/RSV3 各 1 位
# *			iOperationCode	-- 操作码：0x0 - 0xF
# *			lpszMask		-- 掩码（nullptr 或 4 字节掩码，如果为 nullptr 则没有掩码）
# *			pData			-- 消息体数据缓冲区
# *			iLength			-- 消息体数据长度
# *			ullBodyLen		-- 消息总长度
# * 								ullBodyLen = 0		 -> 消息总长度为 iLength
# * 								ullBodyLen = iLength -> 消息总长度为 ullBodyLen
# * 								ullBodyLen > iLength -> 消息总长度为 ullBodyLen，后续消息体长度为 ullBOdyLen - iLength，后续消息体通过底层方法 Send() / SendPackets() 发送
# * 								ullBodyLen < iLength -> 错误参数，发送失败
# * 返回值：	TRUE			-- 成功
# *			FALSE			-- 失败
#
# HPSOCKET_API BOOL __stdcall HP_HttpAgent_SendWSMessage(HP_HttpAgent pAgent, HP_CONNID dwConnID, BOOL bFinal, BYTE iReserved, BYTE iOperationCode, const int lpszMask, BYTE* pData, int iLength, ULONGLONG ullBodyLen);
HP_HttpAgent_SendWSMessage = HPSocketDLL.HP_HttpAgent_SendWSMessage if hasattr(HPSocketDLL, "HP_HttpAgent_SendWSMessage") else None
if HP_HttpAgent_SendWSMessage:
    HP_HttpAgent_SendWSMessage.restype = ctypes.c_bool
    HP_HttpAgent_SendWSMessage.argtypes = [HP_HttpAgent, HP_CONNID, ctypes.c_bool, ctypes.c_byte, ctypes.c_byte, ctypes.c_int, ctypes.POINTER(ctypes.c_byte), ctypes.c_int, ctypes.c_ulonglong]

# ****************************************************************************
# ************************** HTTP Agent 属性访问方法 **************************

#  获取 HTTP 状态码
# HPSOCKET_API USHORT __stdcall HP_HttpAgent_GetStatusCode(HP_HttpAgent pAgent, HP_CONNID dwConnID);
HP_HttpAgent_GetStatusCode = HPSocketDLL.HP_HttpAgent_GetStatusCode if hasattr(HPSocketDLL, "HP_HttpAgent_GetStatusCode") else None
if HP_HttpAgent_GetStatusCode:
    HP_HttpAgent_GetStatusCode.restype = ctypes.c_ushort
    HP_HttpAgent_GetStatusCode.argtypes = [HP_HttpAgent, HP_CONNID]

#  设置本地协议版本
# HPSOCKET_API void __stdcall HP_HttpAgent_SetLocalVersion(HP_HttpAgent pAgent, En_HP_HttpVersion usVersion);
HP_HttpAgent_SetLocalVersion = HPSocketDLL.HP_HttpAgent_SetLocalVersion if hasattr(HPSocketDLL, "HP_HttpAgent_SetLocalVersion") else None
if HP_HttpAgent_SetLocalVersion:
    HP_HttpAgent_SetLocalVersion.restype = None
    HP_HttpAgent_SetLocalVersion.argtypes = [HP_HttpAgent, En_HP_HttpVersion]
#  获取本地协议版本
# HPSOCKET_API En_HP_HttpVersion __stdcall HP_HttpAgent_GetLocalVersion(HP_HttpAgent pAgent);
HP_HttpAgent_GetLocalVersion = HPSocketDLL.HP_HttpAgent_GetLocalVersion if hasattr(HPSocketDLL, "HP_HttpAgent_GetLocalVersion") else None
if HP_HttpAgent_GetLocalVersion:
    HP_HttpAgent_GetLocalVersion.restype = En_HP_HttpVersion
    HP_HttpAgent_GetLocalVersion.argtypes = [HP_HttpAgent]

#  检查是否升级协议
# HPSOCKET_API BOOL __stdcall HP_HttpAgent_IsUpgrade(HP_HttpAgent pAgent, HP_CONNID dwConnID);
HP_HttpAgent_IsUpgrade = HPSocketDLL.HP_HttpAgent_IsUpgrade if hasattr(HPSocketDLL, "HP_HttpAgent_IsUpgrade") else None
if HP_HttpAgent_IsUpgrade:
    HP_HttpAgent_IsUpgrade.restype = ctypes.c_bool
    HP_HttpAgent_IsUpgrade.argtypes = [HP_HttpAgent, HP_CONNID]
#  检查是否有 Keep-Alive 标识
# HPSOCKET_API BOOL __stdcall HP_HttpAgent_IsKeepAlive(HP_HttpAgent pAgent, HP_CONNID dwConnID);
HP_HttpAgent_IsKeepAlive = HPSocketDLL.HP_HttpAgent_IsKeepAlive if hasattr(HPSocketDLL, "HP_HttpAgent_IsKeepAlive") else None
if HP_HttpAgent_IsKeepAlive:
    HP_HttpAgent_IsKeepAlive.restype = ctypes.c_bool
    HP_HttpAgent_IsKeepAlive.argtypes = [HP_HttpAgent, HP_CONNID]
#  获取协议版本
# HPSOCKET_API USHORT __stdcall HP_HttpAgent_GetVersion(HP_HttpAgent pAgent, HP_CONNID dwConnID);
HP_HttpAgent_GetVersion = HPSocketDLL.HP_HttpAgent_GetVersion if hasattr(HPSocketDLL, "HP_HttpAgent_GetVersion") else None
if HP_HttpAgent_GetVersion:
    HP_HttpAgent_GetVersion.restype = ctypes.c_ushort
    HP_HttpAgent_GetVersion.argtypes = [HP_HttpAgent, HP_CONNID]
#  获取内容长度
# HPSOCKET_API ULONGLONG __stdcall HP_HttpAgent_GetContentLength(HP_HttpAgent pAgent, HP_CONNID dwConnID);
HP_HttpAgent_GetContentLength = HPSocketDLL.HP_HttpAgent_GetContentLength if hasattr(HPSocketDLL, "HP_HttpAgent_GetContentLength") else None
if HP_HttpAgent_GetContentLength:
    HP_HttpAgent_GetContentLength.restype = ctypes.c_ulonglong
    HP_HttpAgent_GetContentLength.argtypes = [HP_HttpAgent, HP_CONNID]
#  获取内容类型
# HPSOCKET_API LPCSTR __stdcall HP_HttpAgent_GetContentType(HP_HttpAgent pAgent, HP_CONNID dwConnID);
HP_HttpAgent_GetContentType = HPSocketDLL.HP_HttpAgent_GetContentType if hasattr(HPSocketDLL, "HP_HttpAgent_GetContentType") else None
if HP_HttpAgent_GetContentType:
    HP_HttpAgent_GetContentType.restype = ctypes.c_char_p
    HP_HttpAgent_GetContentType.argtypes = [HP_HttpAgent, HP_CONNID]
#  获取内容编码
# HPSOCKET_API LPCSTR __stdcall HP_HttpAgent_GetContentEncoding(HP_HttpAgent pAgent, HP_CONNID dwConnID);
HP_HttpAgent_GetContentEncoding = HPSocketDLL.HP_HttpAgent_GetContentEncoding if hasattr(HPSocketDLL, "HP_HttpAgent_GetContentEncoding") else None
if HP_HttpAgent_GetContentEncoding:
    HP_HttpAgent_GetContentEncoding.restype = ctypes.c_char_p
    HP_HttpAgent_GetContentEncoding.argtypes = [HP_HttpAgent, HP_CONNID]
#  获取传输编码
# HPSOCKET_API LPCSTR __stdcall HP_HttpAgent_GetTransferEncoding(HP_HttpAgent pAgent, HP_CONNID dwConnID);
HP_HttpAgent_GetTransferEncoding = HPSocketDLL.HP_HttpAgent_GetTransferEncoding if hasattr(HPSocketDLL, "HP_HttpAgent_GetTransferEncoding") else None
if HP_HttpAgent_GetTransferEncoding:
    HP_HttpAgent_GetTransferEncoding.restype = ctypes.c_char_p
    HP_HttpAgent_GetTransferEncoding.argtypes = [HP_HttpAgent, HP_CONNID]
#  获取协议升级类型
# HPSOCKET_API En_HP_HttpUpgradeType __stdcall HP_HttpAgent_GetUpgradeType(HP_HttpAgent pAgent, HP_CONNID dwConnID);
HP_HttpAgent_GetUpgradeType = HPSocketDLL.HP_HttpAgent_GetUpgradeType if hasattr(HPSocketDLL, "HP_HttpAgent_GetUpgradeType") else None
if HP_HttpAgent_GetUpgradeType:
    HP_HttpAgent_GetUpgradeType.restype = En_HP_HttpUpgradeType
    HP_HttpAgent_GetUpgradeType.argtypes = [HP_HttpAgent, HP_CONNID]
#  获取解析错误代码
# HPSOCKET_API USHORT __stdcall HP_HttpAgent_GetParseErrorCode(HP_HttpAgent pAgent, HP_CONNID dwConnID, LPCSTR* lpszErrorDesc);
HP_HttpAgent_GetParseErrorCode = HPSocketDLL.HP_HttpAgent_GetParseErrorCode if hasattr(HPSocketDLL, "HP_HttpAgent_GetParseErrorCode") else None
if HP_HttpAgent_GetParseErrorCode:
    HP_HttpAgent_GetParseErrorCode.restype = ctypes.c_ushort
    HP_HttpAgent_GetParseErrorCode.argtypes = [HP_HttpAgent, HP_CONNID, ctypes.POINTER(ctypes.c_char_p)]

#  获取某个请求头（单值）
# HPSOCKET_API BOOL __stdcall HP_HttpAgent_GetHeader(HP_HttpAgent pAgent, HP_CONNID dwConnID, LPCSTR lpszName, LPCSTR* lpszValue);
HP_HttpAgent_GetHeader = HPSocketDLL.HP_HttpAgent_GetHeader if hasattr(HPSocketDLL, "HP_HttpAgent_GetHeader") else None
if HP_HttpAgent_GetHeader:
    HP_HttpAgent_GetHeader.restype = ctypes.c_bool
    HP_HttpAgent_GetHeader.argtypes = [HP_HttpAgent, HP_CONNID, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p)]
#  获取某个请求头（多值）
# HPSOCKET_API BOOL __stdcall HP_HttpAgent_GetHeaders(HP_HttpAgent pAgent, HP_CONNID dwConnID, LPCSTR lpszName, LPCSTR lpszValue[], DWORD* pdwCount);
HP_HttpAgent_GetHeaders = HPSocketDLL.HP_HttpAgent_GetHeaders if hasattr(HPSocketDLL, "HP_HttpAgent_GetHeaders") else None
if HP_HttpAgent_GetHeaders:
    HP_HttpAgent_GetHeaders.restype = ctypes.c_bool
    HP_HttpAgent_GetHeaders.argtypes = [HP_HttpAgent, HP_CONNID, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_uint)]
#  获取所有请求头
# HPSOCKET_API BOOL __stdcall HP_HttpAgent_GetAllHeaders(HP_HttpAgent pAgent, HP_CONNID dwConnID, HP_THeader lpHeaders[], DWORD* pdwCount);
HP_HttpAgent_GetAllHeaders = HPSocketDLL.HP_HttpAgent_GetAllHeaders if hasattr(HPSocketDLL, "HP_HttpAgent_GetAllHeaders") else None
if HP_HttpAgent_GetAllHeaders:
    HP_HttpAgent_GetAllHeaders.restype = ctypes.c_bool
    HP_HttpAgent_GetAllHeaders.argtypes = [HP_HttpAgent, HP_CONNID, ctypes.POINTER(HP_THeader), ctypes.POINTER(ctypes.c_uint)]
#  获取所有请求头名称
# HPSOCKET_API BOOL __stdcall HP_HttpAgent_GetAllHeaderNames(HP_HttpAgent pAgent, HP_CONNID dwConnID, LPCSTR lpszName[], DWORD* pdwCount);
HP_HttpAgent_GetAllHeaderNames = HPSocketDLL.HP_HttpAgent_GetAllHeaderNames if hasattr(HPSocketDLL, "HP_HttpAgent_GetAllHeaderNames") else None
if HP_HttpAgent_GetAllHeaderNames:
    HP_HttpAgent_GetAllHeaderNames.restype = ctypes.c_bool
    HP_HttpAgent_GetAllHeaderNames.argtypes = [HP_HttpAgent, HP_CONNID, ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_uint)]

#  设置是否使用 Cookie
# HPSOCKET_API void __stdcall HP_HttpAgent_SetUseCookie(HP_HttpAgent pAgent, BOOL bUseCookie);
HP_HttpAgent_SetUseCookie = HPSocketDLL.HP_HttpAgent_SetUseCookie if hasattr(HPSocketDLL, "HP_HttpAgent_SetUseCookie") else None
if HP_HttpAgent_SetUseCookie:
    HP_HttpAgent_SetUseCookie.restype = None
    HP_HttpAgent_SetUseCookie.argtypes = [HP_HttpAgent, ctypes.c_bool]
#  检查是否使用 Cookie
# HPSOCKET_API BOOL __stdcall HP_HttpAgent_IsUseCookie(HP_HttpAgent pAgent);
HP_HttpAgent_IsUseCookie = HPSocketDLL.HP_HttpAgent_IsUseCookie if hasattr(HPSocketDLL, "HP_HttpAgent_IsUseCookie") else None
if HP_HttpAgent_IsUseCookie:
    HP_HttpAgent_IsUseCookie.restype = ctypes.c_bool
    HP_HttpAgent_IsUseCookie.argtypes = [HP_HttpAgent]
#  获取 Cookie
# HPSOCKET_API BOOL __stdcall HP_HttpAgent_GetCookie(HP_HttpAgent pAgent, HP_CONNID dwConnID, LPCSTR lpszName, LPCSTR* lpszValue);
HP_HttpAgent_GetCookie = HPSocketDLL.HP_HttpAgent_GetCookie if hasattr(HPSocketDLL, "HP_HttpAgent_GetCookie") else None
if HP_HttpAgent_GetCookie:
    HP_HttpAgent_GetCookie.restype = ctypes.c_bool
    HP_HttpAgent_GetCookie.argtypes = [HP_HttpAgent, HP_CONNID, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p)]
#  获取所有 Cookie
# HPSOCKET_API BOOL __stdcall HP_HttpAgent_GetAllCookies(HP_HttpAgent pAgent, HP_CONNID dwConnID, HP_TCookie lpCookies[], DWORD* pdwCount);
HP_HttpAgent_GetAllCookies = HPSocketDLL.HP_HttpAgent_GetAllCookies if hasattr(HPSocketDLL, "HP_HttpAgent_GetAllCookies") else None
if HP_HttpAgent_GetAllCookies:
    HP_HttpAgent_GetAllCookies.restype = ctypes.c_bool
    HP_HttpAgent_GetAllCookies.argtypes = [HP_HttpAgent, HP_CONNID, ctypes.POINTER(HP_TCookie), ctypes.POINTER(ctypes.c_uint)]

#  获取当前 WebSocket 消息状态，传入 nullptr 则不获取相应字段
# HPSOCKET_API BOOL __stdcall HP_HttpAgent_GetWSMessageState(HP_HttpAgent pAgent, HP_CONNID dwConnID, BOOL* lpbFinal, BYTE* lpiReserved, BYTE* lpiOperationCode, LPCBYTE* lpszMask, ULONGLONG* lpullBodyLen, ULONGLONG* lpullBodyRemain);
HP_HttpAgent_GetWSMessageState = HPSocketDLL.HP_HttpAgent_GetWSMessageState if hasattr(HPSocketDLL, "HP_HttpAgent_GetWSMessageState") else None
if HP_HttpAgent_GetWSMessageState:
    HP_HttpAgent_GetWSMessageState.restype = ctypes.c_bool
    HP_HttpAgent_GetWSMessageState.argtypes = [HP_HttpAgent, HP_CONNID, ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(LPCBYTE), ctypes.POINTER(ctypes.c_ulonglong), ctypes.POINTER(ctypes.c_ulonglong)]

# ************************************************************************
# ************************** HTTP Client 操作方法 *************************

#
# * 名称：发送请求
# * 描述：向服务端发送 HTTP 请求
# *
# * 参数：		lpszMethod		-- 请求方法
# *			lpszPath		-- 请求路径
# *			lpHeaders		-- 请求头
# *			iHeaderCount	-- 请求头数量
# *			pBody			-- 请求体
# *			iLength			-- 请求体长度
# * 返回值：	TRUE			-- 成功
# *			FALSE			-- 失败
#
# HPSOCKET_API BOOL __stdcall HP_HttpClient_SendRequest(HP_HttpClient pClient, LPCSTR lpszMethod, LPCSTR lpszPath, const HP_THeader lpHeaders[], int iHeaderCount, const BYTE* pBody, int iLength);
HP_HttpClient_SendRequest = HPSocketDLL.HP_HttpClient_SendRequest if hasattr(HPSocketDLL, "HP_HttpClient_SendRequest") else None
if HP_HttpClient_SendRequest:
    HP_HttpClient_SendRequest.restype = ctypes.c_bool
    HP_HttpClient_SendRequest.argtypes = [HP_HttpClient, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int, ctypes.POINTER(ctypes.c_byte), ctypes.c_int]

#
# * 名称：发送本地文件
# * 描述：向指定连接发送 4096 KB 以下的小文件
# *
# * 参数：		dwConnID		-- 连接 ID
# *			lpszFileName	-- 文件路径
# *			lpszMethod		-- 请求方法
# *			lpszPath		-- 请求路径
# *			lpHeaders		-- 请求头
# *			iHeaderCount	-- 请求头数量
# * 返回值：	TRUE			-- 成功
# *			FALSE			-- 失败
#
# HPSOCKET_API BOOL __stdcall HP_HttpClient_SendLocalFile(HP_HttpClient pClient, LPCSTR lpszFileName, LPCSTR lpszMethod, LPCSTR lpszPath, const HP_THeader lpHeaders[], int iHeaderCount);
HP_HttpClient_SendLocalFile = HPSocketDLL.HP_HttpClient_SendLocalFile if hasattr(HPSocketDLL, "HP_HttpClient_SendLocalFile") else None
if HP_HttpClient_SendLocalFile:
    HP_HttpClient_SendLocalFile.restype = ctypes.c_bool
    HP_HttpClient_SendLocalFile.argtypes = [HP_HttpClient, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int]

#  发送 POST 请求
# HPSOCKET_API BOOL __stdcall HP_HttpClient_SendPost(HP_HttpClient pClient, LPCSTR lpszPath, const HP_THeader lpHeaders[], int iHeaderCount, const BYTE* pBody, int iLength);
HP_HttpClient_SendPost = HPSocketDLL.HP_HttpClient_SendPost if hasattr(HPSocketDLL, "HP_HttpClient_SendPost") else None
if HP_HttpClient_SendPost:
    HP_HttpClient_SendPost.restype = ctypes.c_bool
    HP_HttpClient_SendPost.argtypes = [HP_HttpClient, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int, ctypes.POINTER(ctypes.c_byte), ctypes.c_int]
#  发送 PUT 请求
# HPSOCKET_API BOOL __stdcall HP_HttpClient_SendPut(HP_HttpClient pClient, LPCSTR lpszPath, const HP_THeader lpHeaders[], int iHeaderCount, const BYTE* pBody, int iLength);
HP_HttpClient_SendPut = HPSocketDLL.HP_HttpClient_SendPut if hasattr(HPSocketDLL, "HP_HttpClient_SendPut") else None
if HP_HttpClient_SendPut:
    HP_HttpClient_SendPut.restype = ctypes.c_bool
    HP_HttpClient_SendPut.argtypes = [HP_HttpClient, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int, ctypes.POINTER(ctypes.c_byte), ctypes.c_int]
#  发送 PATCH 请求
# HPSOCKET_API BOOL __stdcall HP_HttpClient_SendPatch(HP_HttpClient pClient, LPCSTR lpszPath, const HP_THeader lpHeaders[], int iHeaderCount, const BYTE* pBody, int iLength);
HP_HttpClient_SendPatch = HPSocketDLL.HP_HttpClient_SendPatch if hasattr(HPSocketDLL, "HP_HttpClient_SendPatch") else None
if HP_HttpClient_SendPatch:
    HP_HttpClient_SendPatch.restype = ctypes.c_bool
    HP_HttpClient_SendPatch.argtypes = [HP_HttpClient, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int, ctypes.POINTER(ctypes.c_byte), ctypes.c_int]
#  发送 GET 请求
# HPSOCKET_API BOOL __stdcall HP_HttpClient_SendGet(HP_HttpClient pClient, LPCSTR lpszPath, const HP_THeader lpHeaders[], int iHeaderCount);
HP_HttpClient_SendGet = HPSocketDLL.HP_HttpClient_SendGet if hasattr(HPSocketDLL, "HP_HttpClient_SendGet") else None
if HP_HttpClient_SendGet:
    HP_HttpClient_SendGet.restype = ctypes.c_bool
    HP_HttpClient_SendGet.argtypes = [HP_HttpClient, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int]
#  发送 DELETE 请求
# HPSOCKET_API BOOL __stdcall HP_HttpClient_SendDelete(HP_HttpClient pClient, LPCSTR lpszPath, const HP_THeader lpHeaders[], int iHeaderCount);
HP_HttpClient_SendDelete = HPSocketDLL.HP_HttpClient_SendDelete if hasattr(HPSocketDLL, "HP_HttpClient_SendDelete") else None
if HP_HttpClient_SendDelete:
    HP_HttpClient_SendDelete.restype = ctypes.c_bool
    HP_HttpClient_SendDelete.argtypes = [HP_HttpClient, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int]
#  发送 HEAD 请求
# HPSOCKET_API BOOL __stdcall HP_HttpClient_SendHead(HP_HttpClient pClient, LPCSTR lpszPath, const HP_THeader lpHeaders[], int iHeaderCount);
HP_HttpClient_SendHead = HPSocketDLL.HP_HttpClient_SendHead if hasattr(HPSocketDLL, "HP_HttpClient_SendHead") else None
if HP_HttpClient_SendHead:
    HP_HttpClient_SendHead.restype = ctypes.c_bool
    HP_HttpClient_SendHead.argtypes = [HP_HttpClient, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int]
#  发送 TRACE 请求
# HPSOCKET_API BOOL __stdcall HP_HttpClient_SendTrace(HP_HttpClient pClient, LPCSTR lpszPath, const HP_THeader lpHeaders[], int iHeaderCount);
HP_HttpClient_SendTrace = HPSocketDLL.HP_HttpClient_SendTrace if hasattr(HPSocketDLL, "HP_HttpClient_SendTrace") else None
if HP_HttpClient_SendTrace:
    HP_HttpClient_SendTrace.restype = ctypes.c_bool
    HP_HttpClient_SendTrace.argtypes = [HP_HttpClient, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int]
#  发送 OPTIONS 请求
# HPSOCKET_API BOOL __stdcall HP_HttpClient_SendOptions(HP_HttpClient pClient, LPCSTR lpszPath, const HP_THeader lpHeaders[], int iHeaderCount);
HP_HttpClient_SendOptions = HPSocketDLL.HP_HttpClient_SendOptions if hasattr(HPSocketDLL, "HP_HttpClient_SendOptions") else None
if HP_HttpClient_SendOptions:
    HP_HttpClient_SendOptions.restype = ctypes.c_bool
    HP_HttpClient_SendOptions.argtypes = [HP_HttpClient, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int]
#  发送 CONNECT 请求
# HPSOCKET_API BOOL __stdcall HP_HttpClient_SendConnect(HP_HttpClient pClient, LPCSTR lpszHost, const HP_THeader lpHeaders[], int iHeaderCount);
HP_HttpClient_SendConnect = HPSocketDLL.HP_HttpClient_SendConnect if hasattr(HPSocketDLL, "HP_HttpClient_SendConnect") else None
if HP_HttpClient_SendConnect:
    HP_HttpClient_SendConnect.restype = ctypes.c_bool
    HP_HttpClient_SendConnect.argtypes = [HP_HttpClient, ctypes.c_char_p, ctypes.POINTER(HP_THeader), ctypes.c_int]

#
# * 名称：发送 WebSocket 消息
# * 描述：向对端端发送 WebSocket 消息
# *
# * 参数：		bFinal			-- 是否结束帧
# *			iReserved		-- RSV1/RSV2/RSV3 各 1 位
# *			iOperationCode	-- 操作码：0x0 - 0xF
# *			lpszMask		-- 掩码（nullptr 或 4 字节掩码，如果为 nullptr 则没有掩码）
# *			pData			-- 消息体数据缓冲区
# *			iLength			-- 消息体数据长度
# *			ullBodyLen		-- 消息总长度
# * 								ullBodyLen = 0		 -> 消息总长度为 iLength
# * 								ullBodyLen = iLength -> 消息总长度为 ullBodyLen
# * 								ullBodyLen > iLength -> 消息总长度为 ullBodyLen，后续消息体长度为 ullBOdyLen - iLength，后续消息体通过底层方法 Send() / SendPackets() 发送
# * 								ullBodyLen < iLength -> 错误参数，发送失败
# * 返回值：	TRUE			-- 成功
# *			FALSE			-- 失败
#
# HPSOCKET_API BOOL __stdcall HP_HttpClient_SendWSMessage(HP_HttpClient pClient, BOOL bFinal, BYTE iReserved, BYTE iOperationCode, const int lpszMask, BYTE* pData, int iLength, ULONGLONG ullBodyLen);
HP_HttpClient_SendWSMessage = HPSocketDLL.HP_HttpClient_SendWSMessage if hasattr(HPSocketDLL, "HP_HttpClient_SendWSMessage") else None
if HP_HttpClient_SendWSMessage:
    HP_HttpClient_SendWSMessage.restype = ctypes.c_bool
    HP_HttpClient_SendWSMessage.argtypes = [HP_HttpClient, ctypes.c_bool, ctypes.c_byte, ctypes.c_byte, ctypes.c_int, ctypes.POINTER(ctypes.c_byte), ctypes.c_int, ctypes.c_ulonglong]

# ****************************************************************************
# ************************** HTTP Client 属性访问方法 *************************

#  获取 HTTP 状态码
# HPSOCKET_API USHORT __stdcall HP_HttpClient_GetStatusCode(HP_HttpClient pClient);
HP_HttpClient_GetStatusCode = HPSocketDLL.HP_HttpClient_GetStatusCode if hasattr(HPSocketDLL, "HP_HttpClient_GetStatusCode") else None
if HP_HttpClient_GetStatusCode:
    HP_HttpClient_GetStatusCode.restype = ctypes.c_ushort
    HP_HttpClient_GetStatusCode.argtypes = [HP_HttpClient]

#  设置本地协议版本
# HPSOCKET_API void __stdcall HP_HttpClient_SetLocalVersion(HP_HttpClient pClient, En_HP_HttpVersion usVersion);
HP_HttpClient_SetLocalVersion = HPSocketDLL.HP_HttpClient_SetLocalVersion if hasattr(HPSocketDLL, "HP_HttpClient_SetLocalVersion") else None
if HP_HttpClient_SetLocalVersion:
    HP_HttpClient_SetLocalVersion.restype = None
    HP_HttpClient_SetLocalVersion.argtypes = [HP_HttpClient, En_HP_HttpVersion]
#  获取本地协议版本
# HPSOCKET_API En_HP_HttpVersion __stdcall HP_HttpClient_GetLocalVersion(HP_HttpClient pClient);
HP_HttpClient_GetLocalVersion = HPSocketDLL.HP_HttpClient_GetLocalVersion if hasattr(HPSocketDLL, "HP_HttpClient_GetLocalVersion") else None
if HP_HttpClient_GetLocalVersion:
    HP_HttpClient_GetLocalVersion.restype = En_HP_HttpVersion
    HP_HttpClient_GetLocalVersion.argtypes = [HP_HttpClient]

#  检查是否升级协议
# HPSOCKET_API BOOL __stdcall HP_HttpClient_IsUpgrade(HP_HttpClient pClient);
HP_HttpClient_IsUpgrade = HPSocketDLL.HP_HttpClient_IsUpgrade if hasattr(HPSocketDLL, "HP_HttpClient_IsUpgrade") else None
if HP_HttpClient_IsUpgrade:
    HP_HttpClient_IsUpgrade.restype = ctypes.c_bool
    HP_HttpClient_IsUpgrade.argtypes = [HP_HttpClient]
#  检查是否有 Keep-Alive 标识
# HPSOCKET_API BOOL __stdcall HP_HttpClient_IsKeepAlive(HP_HttpClient pClient);
HP_HttpClient_IsKeepAlive = HPSocketDLL.HP_HttpClient_IsKeepAlive if hasattr(HPSocketDLL, "HP_HttpClient_IsKeepAlive") else None
if HP_HttpClient_IsKeepAlive:
    HP_HttpClient_IsKeepAlive.restype = ctypes.c_bool
    HP_HttpClient_IsKeepAlive.argtypes = [HP_HttpClient]
#  获取协议版本
# HPSOCKET_API USHORT __stdcall HP_HttpClient_GetVersion(HP_HttpClient pClient);
HP_HttpClient_GetVersion = HPSocketDLL.HP_HttpClient_GetVersion if hasattr(HPSocketDLL, "HP_HttpClient_GetVersion") else None
if HP_HttpClient_GetVersion:
    HP_HttpClient_GetVersion.restype = ctypes.c_ushort
    HP_HttpClient_GetVersion.argtypes = [HP_HttpClient]
#  获取内容长度
# HPSOCKET_API ULONGLONG __stdcall HP_HttpClient_GetContentLength(HP_HttpClient pClient);
HP_HttpClient_GetContentLength = HPSocketDLL.HP_HttpClient_GetContentLength if hasattr(HPSocketDLL, "HP_HttpClient_GetContentLength") else None
if HP_HttpClient_GetContentLength:
    HP_HttpClient_GetContentLength.restype = ctypes.c_ulonglong
    HP_HttpClient_GetContentLength.argtypes = [HP_HttpClient]
#  获取内容类型
# HPSOCKET_API LPCSTR __stdcall HP_HttpClient_GetContentType(HP_HttpClient pClient);
HP_HttpClient_GetContentType = HPSocketDLL.HP_HttpClient_GetContentType if hasattr(HPSocketDLL, "HP_HttpClient_GetContentType") else None
if HP_HttpClient_GetContentType:
    HP_HttpClient_GetContentType.restype = ctypes.c_char_p
    HP_HttpClient_GetContentType.argtypes = [HP_HttpClient]
#  获取内容编码
# HPSOCKET_API LPCSTR __stdcall HP_HttpClient_GetContentEncoding(HP_HttpClient pClient);
HP_HttpClient_GetContentEncoding = HPSocketDLL.HP_HttpClient_GetContentEncoding if hasattr(HPSocketDLL, "HP_HttpClient_GetContentEncoding") else None
if HP_HttpClient_GetContentEncoding:
    HP_HttpClient_GetContentEncoding.restype = ctypes.c_char_p
    HP_HttpClient_GetContentEncoding.argtypes = [HP_HttpClient]
#  获取传输编码
# HPSOCKET_API LPCSTR __stdcall HP_HttpClient_GetTransferEncoding(HP_HttpClient pClient);
HP_HttpClient_GetTransferEncoding = HPSocketDLL.HP_HttpClient_GetTransferEncoding if hasattr(HPSocketDLL, "HP_HttpClient_GetTransferEncoding") else None
if HP_HttpClient_GetTransferEncoding:
    HP_HttpClient_GetTransferEncoding.restype = ctypes.c_char_p
    HP_HttpClient_GetTransferEncoding.argtypes = [HP_HttpClient]
#  获取协议升级类型
# HPSOCKET_API En_HP_HttpUpgradeType __stdcall HP_HttpClient_GetUpgradeType(HP_HttpClient pClient);
HP_HttpClient_GetUpgradeType = HPSocketDLL.HP_HttpClient_GetUpgradeType if hasattr(HPSocketDLL, "HP_HttpClient_GetUpgradeType") else None
if HP_HttpClient_GetUpgradeType:
    HP_HttpClient_GetUpgradeType.restype = En_HP_HttpUpgradeType
    HP_HttpClient_GetUpgradeType.argtypes = [HP_HttpClient]
#  获取解析错误代码
# HPSOCKET_API USHORT __stdcall HP_HttpClient_GetParseErrorCode(HP_HttpClient pClient, LPCSTR* lpszErrorDesc);
HP_HttpClient_GetParseErrorCode = HPSocketDLL.HP_HttpClient_GetParseErrorCode if hasattr(HPSocketDLL, "HP_HttpClient_GetParseErrorCode") else None
if HP_HttpClient_GetParseErrorCode:
    HP_HttpClient_GetParseErrorCode.restype = ctypes.c_ushort
    HP_HttpClient_GetParseErrorCode.argtypes = [HP_HttpClient, ctypes.POINTER(ctypes.c_char_p)]

#  获取某个请求头（单值）
# HPSOCKET_API BOOL __stdcall HP_HttpClient_GetHeader(HP_HttpClient pClient, LPCSTR lpszName, LPCSTR* lpszValue);
HP_HttpClient_GetHeader = HPSocketDLL.HP_HttpClient_GetHeader if hasattr(HPSocketDLL, "HP_HttpClient_GetHeader") else None
if HP_HttpClient_GetHeader:
    HP_HttpClient_GetHeader.restype = ctypes.c_bool
    HP_HttpClient_GetHeader.argtypes = [HP_HttpClient, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p)]
#  获取某个请求头（多值）
# HPSOCKET_API BOOL __stdcall HP_HttpClient_GetHeaders(HP_HttpClient pClient, LPCSTR lpszName, LPCSTR lpszValue[], DWORD* pdwCount);
HP_HttpClient_GetHeaders = HPSocketDLL.HP_HttpClient_GetHeaders if hasattr(HPSocketDLL, "HP_HttpClient_GetHeaders") else None
if HP_HttpClient_GetHeaders:
    HP_HttpClient_GetHeaders.restype = ctypes.c_bool
    HP_HttpClient_GetHeaders.argtypes = [HP_HttpClient, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_uint)]
#  获取所有请求头
# HPSOCKET_API BOOL __stdcall HP_HttpClient_GetAllHeaders(HP_HttpClient pClient, HP_THeader lpHeaders[], DWORD* pdwCount);
HP_HttpClient_GetAllHeaders = HPSocketDLL.HP_HttpClient_GetAllHeaders if hasattr(HPSocketDLL, "HP_HttpClient_GetAllHeaders") else None
if HP_HttpClient_GetAllHeaders:
    HP_HttpClient_GetAllHeaders.restype = ctypes.c_bool
    HP_HttpClient_GetAllHeaders.argtypes = [HP_HttpClient, ctypes.POINTER(HP_THeader), ctypes.POINTER(ctypes.c_uint)]
#  获取所有请求头名称
# HPSOCKET_API BOOL __stdcall HP_HttpClient_GetAllHeaderNames(HP_HttpClient pClient, LPCSTR lpszName[], DWORD* pdwCount);
HP_HttpClient_GetAllHeaderNames = HPSocketDLL.HP_HttpClient_GetAllHeaderNames if hasattr(HPSocketDLL, "HP_HttpClient_GetAllHeaderNames") else None
if HP_HttpClient_GetAllHeaderNames:
    HP_HttpClient_GetAllHeaderNames.restype = ctypes.c_bool
    HP_HttpClient_GetAllHeaderNames.argtypes = [HP_HttpClient, ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_uint)]

#  设置是否使用 Cookie
# HPSOCKET_API void __stdcall HP_HttpClient_SetUseCookie(HP_HttpClient pClient, BOOL bUseCookie);
HP_HttpClient_SetUseCookie = HPSocketDLL.HP_HttpClient_SetUseCookie if hasattr(HPSocketDLL, "HP_HttpClient_SetUseCookie") else None
if HP_HttpClient_SetUseCookie:
    HP_HttpClient_SetUseCookie.restype = None
    HP_HttpClient_SetUseCookie.argtypes = [HP_HttpClient, ctypes.c_bool]
#  检查是否使用 Cookie
# HPSOCKET_API BOOL __stdcall HP_HttpClient_IsUseCookie(HP_HttpClient pClient);
HP_HttpClient_IsUseCookie = HPSocketDLL.HP_HttpClient_IsUseCookie if hasattr(HPSocketDLL, "HP_HttpClient_IsUseCookie") else None
if HP_HttpClient_IsUseCookie:
    HP_HttpClient_IsUseCookie.restype = ctypes.c_bool
    HP_HttpClient_IsUseCookie.argtypes = [HP_HttpClient]
#  获取 Cookie
# HPSOCKET_API BOOL __stdcall HP_HttpClient_GetCookie(HP_HttpClient pClient, LPCSTR lpszName, LPCSTR* lpszValue);
HP_HttpClient_GetCookie = HPSocketDLL.HP_HttpClient_GetCookie if hasattr(HPSocketDLL, "HP_HttpClient_GetCookie") else None
if HP_HttpClient_GetCookie:
    HP_HttpClient_GetCookie.restype = ctypes.c_bool
    HP_HttpClient_GetCookie.argtypes = [HP_HttpClient, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p)]
#  获取所有 Cookie
# HPSOCKET_API BOOL __stdcall HP_HttpClient_GetAllCookies(HP_HttpClient pClient, HP_TCookie lpCookies[], DWORD* pdwCount);
HP_HttpClient_GetAllCookies = HPSocketDLL.HP_HttpClient_GetAllCookies if hasattr(HPSocketDLL, "HP_HttpClient_GetAllCookies") else None
if HP_HttpClient_GetAllCookies:
    HP_HttpClient_GetAllCookies.restype = ctypes.c_bool
    HP_HttpClient_GetAllCookies.argtypes = [HP_HttpClient, ctypes.POINTER(HP_TCookie), ctypes.POINTER(ctypes.c_uint)]

#  获取当前 WebSocket 消息状态，传入 nullptr 则不获取相应字段
# HPSOCKET_API BOOL __stdcall HP_HttpClient_GetWSMessageState(HP_HttpClient pClient, BOOL* lpbFinal, BYTE* lpiReserved, BYTE* lpiOperationCode, LPCBYTE* lpszMask, ULONGLONG* lpullBodyLen, ULONGLONG* lpullBodyRemain);
HP_HttpClient_GetWSMessageState = HPSocketDLL.HP_HttpClient_GetWSMessageState if hasattr(HPSocketDLL, "HP_HttpClient_GetWSMessageState") else None
if HP_HttpClient_GetWSMessageState:
    HP_HttpClient_GetWSMessageState.restype = ctypes.c_bool
    HP_HttpClient_GetWSMessageState.argtypes = [HP_HttpClient, ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(LPCBYTE), ctypes.POINTER(ctypes.c_ulonglong), ctypes.POINTER(ctypes.c_ulonglong)]

# ************************************************************************
# *********************** HTTP Sync Client 操作方法 ***********************

#
# * 名称：发送 URL 请求
# * 描述：向服务端发送 HTTP URL 请求
# *
# * 参数：		lpszMethod		-- 请求方法
# *			lpszUrl			-- 请求 URL
# *			lpHeaders		-- 请求头
# *			iHeaderCount	-- 请求头数量
# *			pBody			-- 请求体
# *			iLength			-- 请求体长度
# *			bForceReconnect	-- 强制重新连接（默认：FALSE，当请求 URL 的主机和端口与现有连接一致时，重用现有连接）
# * 返回值：	TRUE			-- 成功
# *			FALSE			-- 失败
#
# HPSOCKET_API BOOL __stdcall HP_HttpSyncClient_OpenUrl(HP_HttpSyncClient pClient, LPCSTR lpszMethod, LPCSTR lpszUrl, const THeader lpHeaders[], int iHeaderCount, const BYTE* pBody, int iLength, BOOL bForceReconnect);
HP_HttpSyncClient_OpenUrl = HPSocketDLL.HP_HttpSyncClient_OpenUrl if hasattr(HPSocketDLL, "HP_HttpSyncClient_OpenUrl") else None
if HP_HttpSyncClient_OpenUrl:
    HP_HttpSyncClient_OpenUrl.restype = ctypes.c_bool
    HP_HttpSyncClient_OpenUrl.argtypes = [HP_HttpSyncClient, ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(THeader), ctypes.c_int, ctypes.POINTER(ctypes.c_byte), ctypes.c_int, ctypes.c_bool]

#
# * 名称：清除请求结果
# * 描述：清除上一次请求的响应头和响应体等结果信息（该方法会在每次发送请求前自动调用）
# *
# * 参数：
# * 返回值：	TRUE			-- 成功
# *			FALSE			-- 失败
#
# HPSOCKET_API BOOL __stdcall HP_HttpSyncClient_CleanupRequestResult(HP_HttpSyncClient pClient);
HP_HttpSyncClient_CleanupRequestResult = HPSocketDLL.HP_HttpSyncClient_CleanupRequestResult if hasattr(HPSocketDLL, "HP_HttpSyncClient_CleanupRequestResult") else None
if HP_HttpSyncClient_CleanupRequestResult:
    HP_HttpSyncClient_CleanupRequestResult.restype = ctypes.c_bool
    HP_HttpSyncClient_CleanupRequestResult.argtypes = [HP_HttpSyncClient]

# ****************************************************************************
# *********************** HTTP Sync Client 属性访问方法 ***********************

#  设置连接超时（毫秒，0：系统默认超时，默认：5000）
# HPSOCKET_API void __stdcall HP_HttpSyncClient_SetConnectTimeout(HP_HttpSyncClient pClient, DWORD dwConnectTimeout);
HP_HttpSyncClient_SetConnectTimeout = HPSocketDLL.HP_HttpSyncClient_SetConnectTimeout if hasattr(HPSocketDLL, "HP_HttpSyncClient_SetConnectTimeout") else None
if HP_HttpSyncClient_SetConnectTimeout:
    HP_HttpSyncClient_SetConnectTimeout.restype = None
    HP_HttpSyncClient_SetConnectTimeout.argtypes = [HP_HttpSyncClient, ctypes.c_uint]
#  设置请求超时（毫秒，0：无限等待，默认：10000）
# HPSOCKET_API void __stdcall HP_HttpSyncClient_SetRequestTimeout(HP_HttpSyncClient pClient, DWORD dwRequestTimeout);
HP_HttpSyncClient_SetRequestTimeout = HPSocketDLL.HP_HttpSyncClient_SetRequestTimeout if hasattr(HPSocketDLL, "HP_HttpSyncClient_SetRequestTimeout") else None
if HP_HttpSyncClient_SetRequestTimeout:
    HP_HttpSyncClient_SetRequestTimeout.restype = None
    HP_HttpSyncClient_SetRequestTimeout.argtypes = [HP_HttpSyncClient, ctypes.c_uint]

#  获取连接超时
# HPSOCKET_API DWORD __stdcall HP_HttpSyncClient_GetConnectTimeout(HP_HttpSyncClient pClient);
HP_HttpSyncClient_GetConnectTimeout = HPSocketDLL.HP_HttpSyncClient_GetConnectTimeout if hasattr(HPSocketDLL, "HP_HttpSyncClient_GetConnectTimeout") else None
if HP_HttpSyncClient_GetConnectTimeout:
    HP_HttpSyncClient_GetConnectTimeout.restype = ctypes.c_uint
    HP_HttpSyncClient_GetConnectTimeout.argtypes = [HP_HttpSyncClient]
#  获取请求超时
# HPSOCKET_API DWORD __stdcall HP_HttpSyncClient_GetRequestTimeout(HP_HttpSyncClient pClient);
HP_HttpSyncClient_GetRequestTimeout = HPSocketDLL.HP_HttpSyncClient_GetRequestTimeout if hasattr(HPSocketDLL, "HP_HttpSyncClient_GetRequestTimeout") else None
if HP_HttpSyncClient_GetRequestTimeout:
    HP_HttpSyncClient_GetRequestTimeout.restype = ctypes.c_uint
    HP_HttpSyncClient_GetRequestTimeout.argtypes = [HP_HttpSyncClient]

#  获取响应体
# HPSOCKET_API BOOL __stdcall HP_HttpSyncClient_GetResponseBody(HP_HttpSyncClient pClient, LPCBYTE* lpszBody, int* piLength);
HP_HttpSyncClient_GetResponseBody = HPSocketDLL.HP_HttpSyncClient_GetResponseBody if hasattr(HPSocketDLL, "HP_HttpSyncClient_GetResponseBody") else None
if HP_HttpSyncClient_GetResponseBody:
    HP_HttpSyncClient_GetResponseBody.restype = ctypes.c_bool
    HP_HttpSyncClient_GetResponseBody.argtypes = [HP_HttpSyncClient, ctypes.POINTER(LPCBYTE), ctypes.POINTER(ctypes.c_int)]

# ************************************************************************
# ************************** HTTP Cookie 管理方法 *************************

#  从文件加载 Cookie
# HPSOCKET_API BOOL __stdcall HP_HttpCookie_MGR_LoadFromFile(LPCSTR lpszFile, BOOL bKeepExists  );
HP_HttpCookie_MGR_LoadFromFile = HPSocketDLL.HP_HttpCookie_MGR_LoadFromFile if hasattr(HPSocketDLL, "HP_HttpCookie_MGR_LoadFromFile") else None
if HP_HttpCookie_MGR_LoadFromFile:
    HP_HttpCookie_MGR_LoadFromFile.restype = ctypes.c_bool
    HP_HttpCookie_MGR_LoadFromFile.argtypes = [ctypes.c_char_p, ctypes.c_bool]
#  保存 Cookie 到文件
# HPSOCKET_API BOOL __stdcall HP_HttpCookie_MGR_SaveToFile(LPCSTR lpszFile, BOOL bKeepExists  );
HP_HttpCookie_MGR_SaveToFile = HPSocketDLL.HP_HttpCookie_MGR_SaveToFile if hasattr(HPSocketDLL, "HP_HttpCookie_MGR_SaveToFile") else None
if HP_HttpCookie_MGR_SaveToFile:
    HP_HttpCookie_MGR_SaveToFile.restype = ctypes.c_bool
    HP_HttpCookie_MGR_SaveToFile.argtypes = [ctypes.c_char_p, ctypes.c_bool]
#  清理 Cookie
# HPSOCKET_API BOOL __stdcall HP_HttpCookie_MGR_ClearCookies(LPCSTR lpszDomain  , LPCSTR lpszPath  );
HP_HttpCookie_MGR_ClearCookies = HPSocketDLL.HP_HttpCookie_MGR_ClearCookies if hasattr(HPSocketDLL, "HP_HttpCookie_MGR_ClearCookies") else None
if HP_HttpCookie_MGR_ClearCookies:
    HP_HttpCookie_MGR_ClearCookies.restype = ctypes.c_bool
    HP_HttpCookie_MGR_ClearCookies.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
#  清理过期 Cookie
# HPSOCKET_API BOOL __stdcall HP_HttpCookie_MGR_RemoveExpiredCookies(LPCSTR lpszDomain  , LPCSTR lpszPath  );
HP_HttpCookie_MGR_RemoveExpiredCookies = HPSocketDLL.HP_HttpCookie_MGR_RemoveExpiredCookies if hasattr(HPSocketDLL, "HP_HttpCookie_MGR_RemoveExpiredCookies") else None
if HP_HttpCookie_MGR_RemoveExpiredCookies:
    HP_HttpCookie_MGR_RemoveExpiredCookies.restype = ctypes.c_bool
    HP_HttpCookie_MGR_RemoveExpiredCookies.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
#  设置 Cookie
# HPSOCKET_API BOOL __stdcall HP_HttpCookie_MGR_SetCookie(LPCSTR lpszName, LPCSTR lpszValue, LPCSTR lpszDomain, LPCSTR lpszPath, int iMaxAge  , BOOL bHttpOnly  , BOOL bSecure  , int enSameSite  , BOOL bOnlyUpdateValueIfExists  );
HP_HttpCookie_MGR_SetCookie = HPSocketDLL.HP_HttpCookie_MGR_SetCookie if hasattr(HPSocketDLL, "HP_HttpCookie_MGR_SetCookie") else None
if HP_HttpCookie_MGR_SetCookie:
    HP_HttpCookie_MGR_SetCookie.restype = ctypes.c_bool
    HP_HttpCookie_MGR_SetCookie.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_bool, ctypes.c_bool, ctypes.c_int, ctypes.c_bool]
#  删除 Cookie
# HPSOCKET_API BOOL __stdcall HP_HttpCookie_MGR_DeleteCookie(LPCSTR lpszDomain, LPCSTR lpszPath, LPCSTR lpszName);
HP_HttpCookie_MGR_DeleteCookie = HPSocketDLL.HP_HttpCookie_MGR_DeleteCookie if hasattr(HPSocketDLL, "HP_HttpCookie_MGR_DeleteCookie") else None
if HP_HttpCookie_MGR_DeleteCookie:
    HP_HttpCookie_MGR_DeleteCookie.restype = ctypes.c_bool
    HP_HttpCookie_MGR_DeleteCookie.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
#  设置是否允许第三方 Cookie
# HPSOCKET_API void __stdcall HP_HttpCookie_MGR_SetEnableThirdPartyCookie(BOOL bEnableThirdPartyCookie  );
HP_HttpCookie_MGR_SetEnableThirdPartyCookie = HPSocketDLL.HP_HttpCookie_MGR_SetEnableThirdPartyCookie if hasattr(HPSocketDLL, "HP_HttpCookie_MGR_SetEnableThirdPartyCookie") else None
if HP_HttpCookie_MGR_SetEnableThirdPartyCookie:
    HP_HttpCookie_MGR_SetEnableThirdPartyCookie.restype = None
    HP_HttpCookie_MGR_SetEnableThirdPartyCookie.argtypes = [ctypes.c_bool]
#  检查是否允许第三方 Cookie
# HPSOCKET_API BOOL __stdcall HP_HttpCookie_MGR_IsEnableThirdPartyCookie();
HP_HttpCookie_MGR_IsEnableThirdPartyCookie = HPSocketDLL.HP_HttpCookie_MGR_IsEnableThirdPartyCookie if hasattr(HPSocketDLL, "HP_HttpCookie_MGR_IsEnableThirdPartyCookie") else None
if HP_HttpCookie_MGR_IsEnableThirdPartyCookie:
    HP_HttpCookie_MGR_IsEnableThirdPartyCookie.restype = ctypes.c_bool
    HP_HttpCookie_MGR_IsEnableThirdPartyCookie.argtypes = []

#  Cookie expires 字符串转换为整数
# HPSOCKET_API BOOL __stdcall HP_HttpCookie_HLP_ParseExpires(LPCSTR lpszExpires, __time64_t* ptmExpires);
HP_HttpCookie_HLP_ParseExpires = HPSocketDLL.HP_HttpCookie_HLP_ParseExpires if hasattr(HPSocketDLL, "HP_HttpCookie_HLP_ParseExpires") else None
if HP_HttpCookie_HLP_ParseExpires:
    HP_HttpCookie_HLP_ParseExpires.restype = ctypes.c_bool
    HP_HttpCookie_HLP_ParseExpires.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_ulonglong)]
#  整数转换为 Cookie expires 字符串
# HPSOCKET_API BOOL __stdcall HP_HttpCookie_HLP_MakeExpiresStr(char lpszBuff[], int* piBuffLen, __time64_t tmExpires);
HP_HttpCookie_HLP_MakeExpiresStr = HPSocketDLL.HP_HttpCookie_HLP_MakeExpiresStr if hasattr(HPSocketDLL, "HP_HttpCookie_HLP_MakeExpiresStr") else None
if HP_HttpCookie_HLP_MakeExpiresStr:
    HP_HttpCookie_HLP_MakeExpiresStr.restype = ctypes.c_bool
    HP_HttpCookie_HLP_MakeExpiresStr.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int), ctypes.c_ulonglong]
#  生成 Cookie 字符串
# HPSOCKET_API BOOL __stdcall HP_HttpCookie_HLP_ToString(char lpszBuff[], int* piBuffLen, LPCSTR lpszName, LPCSTR lpszValue, LPCSTR lpszDomain, LPCSTR lpszPath, int iMaxAge  , BOOL bHttpOnly  , BOOL bSecure  , int enSameSite  );
HP_HttpCookie_HLP_ToString = HPSocketDLL.HP_HttpCookie_HLP_ToString if hasattr(HPSocketDLL, "HP_HttpCookie_HLP_ToString") else None
if HP_HttpCookie_HLP_ToString:
    HP_HttpCookie_HLP_ToString.restype = ctypes.c_bool
    HP_HttpCookie_HLP_ToString.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int), ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_bool, ctypes.c_bool, ctypes.c_int]
#  获取当前 UTC 时间
# HPSOCKET_API __time64_t __stdcall HP_HttpCookie_HLP_CurrentUTCTime();
HP_HttpCookie_HLP_CurrentUTCTime = HPSocketDLL.HP_HttpCookie_HLP_CurrentUTCTime if hasattr(HPSocketDLL, "HP_HttpCookie_HLP_CurrentUTCTime") else None
if HP_HttpCookie_HLP_CurrentUTCTime:
    HP_HttpCookie_HLP_CurrentUTCTime.restype = ctypes.c_ulonglong
    HP_HttpCookie_HLP_CurrentUTCTime.argtypes = []
#  Max-Age -> expires
# HPSOCKET_API __time64_t __stdcall HP_HttpCookie_HLP_MaxAgeToExpires(int iMaxAge);
HP_HttpCookie_HLP_MaxAgeToExpires = HPSocketDLL.HP_HttpCookie_HLP_MaxAgeToExpires if hasattr(HPSocketDLL, "HP_HttpCookie_HLP_MaxAgeToExpires") else None
if HP_HttpCookie_HLP_MaxAgeToExpires:
    HP_HttpCookie_HLP_MaxAgeToExpires.restype = ctypes.c_ulonglong
    HP_HttpCookie_HLP_MaxAgeToExpires.argtypes = [ctypes.c_int]
#  expires -> Max-Age
# HPSOCKET_API int __stdcall HP_HttpCookie_HLP_ExpiresToMaxAge(__time64_t tmExpires);
HP_HttpCookie_HLP_ExpiresToMaxAge = HPSocketDLL.HP_HttpCookie_HLP_ExpiresToMaxAge if hasattr(HPSocketDLL, "HP_HttpCookie_HLP_ExpiresToMaxAge") else None
if HP_HttpCookie_HLP_ExpiresToMaxAge:
    HP_HttpCookie_HLP_ExpiresToMaxAge.restype = ctypes.c_int
    HP_HttpCookie_HLP_ExpiresToMaxAge.argtypes = [ctypes.c_ulonglong]

# ***************************************************************************************************************************************************
# ************************************************************** Global Function Exports ************************************************************
# ***************************************************************************************************************************************************

#  获取 HPSocket 版本号（4 个字节分别为：主版本号，子版本号，修正版本号，构建编号）
# HPSOCKET_API DWORD __stdcall HP_GetHPSocketVersion();
HP_GetHPSocketVersion = HPSocketDLL.HP_GetHPSocketVersion if hasattr(HPSocketDLL, "HP_GetHPSocketVersion") else None
if HP_GetHPSocketVersion:
    HP_GetHPSocketVersion.restype = ctypes.c_uint
    HP_GetHPSocketVersion.argtypes = []

#  获取错误描述文本
# HPSOCKET_API LPCTSTR __stdcall HP_GetSocketErrorDesc(En_HP_SocketError enCode);
HP_GetSocketErrorDesc = HPSocketDLL.HP_GetSocketErrorDesc if hasattr(HPSocketDLL, "HP_GetSocketErrorDesc") else None
if HP_GetSocketErrorDesc:
    HP_GetSocketErrorDesc.restype = ctypes.c_char_p
    HP_GetSocketErrorDesc.argtypes = [En_HP_SocketError]
#  调用系统的 GetLastError() 方法获取系统错误代码
# HPSOCKET_API DWORD __stdcall SYS_GetLastError();
SYS_GetLastError = HPSocketDLL.SYS_GetLastError if hasattr(HPSocketDLL, "SYS_GetLastError") else None
if SYS_GetLastError:
    SYS_GetLastError.restype = ctypes.c_uint
    SYS_GetLastError.argtypes = []
#  调用系统的 WSAGetLastError() 方法获取系统错误代码
# HPSOCKET_API int __stdcall SYS_WSAGetLastError();
SYS_WSAGetLastError = HPSocketDLL.SYS_WSAGetLastError if hasattr(HPSocketDLL, "SYS_WSAGetLastError") else None
if SYS_WSAGetLastError:
    SYS_WSAGetLastError.restype = ctypes.c_int
    SYS_WSAGetLastError.argtypes = []
#  调用系统的 setsockopt()
# HPSOCKET_API int __stdcall SYS_SetSocketOption(SOCKET sock, int level, int name, LPVOID val, int len);
SYS_SetSocketOption = HPSocketDLL.SYS_SetSocketOption if hasattr(HPSocketDLL, "SYS_SetSocketOption") else None
if SYS_SetSocketOption:
    SYS_SetSocketOption.restype = ctypes.c_int
    SYS_SetSocketOption.argtypes = [SOCKET, ctypes.c_int, ctypes.c_int, LPVOID, ctypes.c_int]
#  调用系统的 getsockopt()
# HPSOCKET_API int __stdcall SYS_GetSocketOption(SOCKET sock, int level, int name, LPVOID val, int* len);
SYS_GetSocketOption = HPSocketDLL.SYS_GetSocketOption if hasattr(HPSocketDLL, "SYS_GetSocketOption") else None
if SYS_GetSocketOption:
    SYS_GetSocketOption.restype = ctypes.c_int
    SYS_GetSocketOption.argtypes = [SOCKET, ctypes.c_int, ctypes.c_int, LPVOID, ctypes.POINTER(ctypes.c_int)]
#  调用系统的 ioctlsocket()
# HPSOCKET_API int __stdcall SYS_IoctlSocket(SOCKET sock, long cmd, u_long* arg);
SYS_IoctlSocket = HPSocketDLL.SYS_IoctlSocket if hasattr(HPSocketDLL, "SYS_IoctlSocket") else None
if SYS_IoctlSocket:
    SYS_IoctlSocket.restype = ctypes.c_int
    SYS_IoctlSocket.argtypes = [SOCKET, ctypes.c_long, ctypes.POINTER(ctypes.c_ulong)]
#  调用系统的 WSAIoctl()
# HPSOCKET_API int __stdcall SYS_WSAIoctl(SOCKET sock, DWORD dwIoControlCode, LPVOID lpvInBuffer, DWORD cbInBuffer, LPVOID lpvOutBuffer, DWORD cbOutBuffer, LPDWORD lpcbBytesReturned);
SYS_WSAIoctl = HPSocketDLL.SYS_WSAIoctl if hasattr(HPSocketDLL, "SYS_WSAIoctl") else None
if SYS_WSAIoctl:
    SYS_WSAIoctl.restype = ctypes.c_int
    SYS_WSAIoctl.argtypes = [SOCKET, ctypes.c_uint, LPVOID, ctypes.c_uint, LPVOID, ctypes.c_uint, ctypes.POINTER(ctypes.c_ulong)]

#  设置 socket 选项：IPPROTO_TCP -> TCP_NODELAY
# HPSOCKET_API int __stdcall SYS_SSO_NoDelay(SOCKET sock, BOOL bNoDelay);
SYS_SSO_NoDelay = HPSocketDLL.SYS_SSO_NoDelay if hasattr(HPSocketDLL, "SYS_SSO_NoDelay") else None
if SYS_SSO_NoDelay:
    SYS_SSO_NoDelay.restype = ctypes.c_int
    SYS_SSO_NoDelay.argtypes = [SOCKET, ctypes.c_bool]
#  设置 socket 选项：SOL_SOCKET -> SO_DONTLINGER
# HPSOCKET_API int __stdcall SYS_SSO_DontLinger(SOCKET sock, BOOL bDont);
SYS_SSO_DontLinger = HPSocketDLL.SYS_SSO_DontLinger if hasattr(HPSocketDLL, "SYS_SSO_DontLinger") else None
if SYS_SSO_DontLinger:
    SYS_SSO_DontLinger.restype = ctypes.c_int
    SYS_SSO_DontLinger.argtypes = [SOCKET, ctypes.c_bool]
#  设置 socket 选项：SOL_SOCKET -> SO_LINGER
# HPSOCKET_API int __stdcall SYS_SSO_Linger(SOCKET sock, USHORT l_onoff, USHORT l_linger);
SYS_SSO_Linger = HPSocketDLL.SYS_SSO_Linger if hasattr(HPSocketDLL, "SYS_SSO_Linger") else None
if SYS_SSO_Linger:
    SYS_SSO_Linger.restype = ctypes.c_int
    SYS_SSO_Linger.argtypes = [SOCKET, ctypes.c_ushort, ctypes.c_ushort]
#  设置 socket 选项：SOL_SOCKET -> SO_RCVBUF
# HPSOCKET_API int __stdcall SYS_SSO_RecvBuffSize(SOCKET sock, int size);
SYS_SSO_RecvBuffSize = HPSocketDLL.SYS_SSO_RecvBuffSize if hasattr(HPSocketDLL, "SYS_SSO_RecvBuffSize") else None
if SYS_SSO_RecvBuffSize:
    SYS_SSO_RecvBuffSize.restype = ctypes.c_int
    SYS_SSO_RecvBuffSize.argtypes = [SOCKET, ctypes.c_int]
#  设置 socket 选项：SOL_SOCKET -> SO_SNDBUF
# HPSOCKET_API int __stdcall SYS_SSO_SendBuffSize(SOCKET sock, int size);
SYS_SSO_SendBuffSize = HPSocketDLL.SYS_SSO_SendBuffSize if hasattr(HPSocketDLL, "SYS_SSO_SendBuffSize") else None
if SYS_SSO_SendBuffSize:
    SYS_SSO_SendBuffSize.restype = ctypes.c_int
    SYS_SSO_SendBuffSize.argtypes = [SOCKET, ctypes.c_int]
#  设置 socket 选项：SOL_SOCKET -> SO_REUSEADDR
# HPSOCKET_API int __stdcall SYS_SSO_ReuseAddress(SOCKET sock, BOOL bReuse);
SYS_SSO_ReuseAddress = HPSocketDLL.SYS_SSO_ReuseAddress if hasattr(HPSocketDLL, "SYS_SSO_ReuseAddress") else None
if SYS_SSO_ReuseAddress:
    SYS_SSO_ReuseAddress.restype = ctypes.c_int
    SYS_SSO_ReuseAddress.argtypes = [SOCKET, ctypes.c_bool]

#  获取 SOCKET 本地地址信息
# HPSOCKET_API BOOL __stdcall SYS_GetSocketLocalAddress(SOCKET socket, TCHAR lpszAddress[], int* piAddressLen, USHORT* pusPort);
SYS_GetSocketLocalAddress = HPSocketDLL.SYS_GetSocketLocalAddress if hasattr(HPSocketDLL, "SYS_GetSocketLocalAddress") else None
if SYS_GetSocketLocalAddress:
    SYS_GetSocketLocalAddress.restype = ctypes.c_bool
    SYS_GetSocketLocalAddress.argtypes = [SOCKET, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_ushort)]
#  获取 SOCKET 远程地址信息
# HPSOCKET_API BOOL __stdcall SYS_GetSocketRemoteAddress(SOCKET socket, TCHAR lpszAddress[], int* piAddressLen, USHORT* pusPort);
SYS_GetSocketRemoteAddress = HPSocketDLL.SYS_GetSocketRemoteAddress if hasattr(HPSocketDLL, "SYS_GetSocketRemoteAddress") else None
if SYS_GetSocketRemoteAddress:
    SYS_GetSocketRemoteAddress.restype = ctypes.c_bool
    SYS_GetSocketRemoteAddress.argtypes = [SOCKET, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_ushort)]

#  枚举主机 IP 地址
# HPSOCKET_API BOOL __stdcall SYS_EnumHostIPAddresses(LPCTSTR lpszHost, En_HP_IPAddrType enType, HP_LPTIPAddr** lpppIPAddr, int* piIPAddrCount);
SYS_EnumHostIPAddresses = HPSocketDLL.SYS_EnumHostIPAddresses if hasattr(HPSocketDLL, "SYS_EnumHostIPAddresses") else None
if SYS_EnumHostIPAddresses:
    SYS_EnumHostIPAddresses.restype = ctypes.c_bool
    SYS_EnumHostIPAddresses.argtypes = [ctypes.c_char_p, En_HP_IPAddrType, ctypes.POINTER(ctypes.POINTER(HP_LPTIPAddr)), ctypes.POINTER(ctypes.c_int)]
#  释放 HP_LPTIPAddr*
# HPSOCKET_API BOOL __stdcall SYS_FreeHostIPAddresses(HP_LPTIPAddr* lppIPAddr);
SYS_FreeHostIPAddresses = HPSocketDLL.SYS_FreeHostIPAddresses if hasattr(HPSocketDLL, "SYS_FreeHostIPAddresses") else None
if SYS_FreeHostIPAddresses:
    SYS_FreeHostIPAddresses.restype = ctypes.c_bool
    SYS_FreeHostIPAddresses.argtypes = [ctypes.POINTER(HP_LPTIPAddr)]
#  检查字符串是否符合 IP 地址格式
# HPSOCKET_API BOOL __stdcall SYS_IsIPAddress(LPCTSTR lpszAddress, En_HP_IPAddrType* penType);
SYS_IsIPAddress = HPSocketDLL.SYS_IsIPAddress if hasattr(HPSocketDLL, "SYS_IsIPAddress") else None
if SYS_IsIPAddress:
    SYS_IsIPAddress.restype = ctypes.c_bool
    SYS_IsIPAddress.argtypes = [ctypes.c_char_p, ctypes.POINTER(En_HP_IPAddrType)]
#  通过主机名获取 IP 地址
# HPSOCKET_API BOOL __stdcall SYS_GetIPAddress(LPCTSTR lpszHost, TCHAR lpszIP[], int* piIPLenth, En_HP_IPAddrType* penType);
SYS_GetIPAddress = HPSocketDLL.SYS_GetIPAddress if hasattr(HPSocketDLL, "SYS_GetIPAddress") else None
if SYS_GetIPAddress:
    SYS_GetIPAddress.restype = ctypes.c_bool
    SYS_GetIPAddress.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(En_HP_IPAddrType)]

#  64 位网络字节序转主机字节序
# HPSOCKET_API ULONGLONG __stdcall SYS_NToH64(ULONGLONG value);
SYS_NToH64 = HPSocketDLL.SYS_NToH64 if hasattr(HPSocketDLL, "SYS_NToH64") else None
if SYS_NToH64:
    SYS_NToH64.restype = ctypes.c_ulonglong
    SYS_NToH64.argtypes = [ctypes.c_ulonglong]
#  64 位主机字节序转网络字节序
# HPSOCKET_API ULONGLONG __stdcall SYS_HToN64(ULONGLONG value);
SYS_HToN64 = HPSocketDLL.SYS_HToN64 if hasattr(HPSocketDLL, "SYS_HToN64") else None
if SYS_HToN64:
    SYS_HToN64.restype = ctypes.c_ulonglong
    SYS_HToN64.argtypes = [ctypes.c_ulonglong]

#  CP_XXX -> UNICODE
# HPSOCKET_API BOOL __stdcall SYS_CodePageToUnicode(int iCodePage, const char szSrc[], WCHAR szDest[], int* piDestLength);
SYS_CodePageToUnicode = HPSocketDLL.SYS_CodePageToUnicode if hasattr(HPSocketDLL, "SYS_CodePageToUnicode") else None
if SYS_CodePageToUnicode:
    SYS_CodePageToUnicode.restype = ctypes.c_bool
    SYS_CodePageToUnicode.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_wchar), ctypes.POINTER(ctypes.c_int)]
#  UNICODE -> CP_XXX
# HPSOCKET_API BOOL __stdcall SYS_UnicodeToCodePage(int iCodePage, const WCHAR szSrc[], char szDest[], int* piDestLength);
SYS_UnicodeToCodePage = HPSocketDLL.SYS_UnicodeToCodePage if hasattr(HPSocketDLL, "SYS_UnicodeToCodePage") else None
if SYS_UnicodeToCodePage:
    SYS_UnicodeToCodePage.restype = ctypes.c_bool
    SYS_UnicodeToCodePage.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_wchar), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int)]
#  GBK -> UNICODE
# HPSOCKET_API BOOL __stdcall SYS_GbkToUnicode(const char szSrc[], WCHAR szDest[], int* piDestLength);
SYS_GbkToUnicode = HPSocketDLL.SYS_GbkToUnicode if hasattr(HPSocketDLL, "SYS_GbkToUnicode") else None
if SYS_GbkToUnicode:
    SYS_GbkToUnicode.restype = ctypes.c_bool
    SYS_GbkToUnicode.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_wchar), ctypes.POINTER(ctypes.c_int)]
#  UNICODE -> GBK
# HPSOCKET_API BOOL __stdcall SYS_UnicodeToGbk(const WCHAR szSrc[], char szDest[], int* piDestLength);
SYS_UnicodeToGbk = HPSocketDLL.SYS_UnicodeToGbk if hasattr(HPSocketDLL, "SYS_UnicodeToGbk") else None
if SYS_UnicodeToGbk:
    SYS_UnicodeToGbk.restype = ctypes.c_bool
    SYS_UnicodeToGbk.argtypes = [ctypes.POINTER(ctypes.c_wchar), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int)]
#  UTF8 -> UNICODE
# HPSOCKET_API BOOL __stdcall SYS_Utf8ToUnicode(const char szSrc[], WCHAR szDest[], int* piDestLength);
SYS_Utf8ToUnicode = HPSocketDLL.SYS_Utf8ToUnicode if hasattr(HPSocketDLL, "SYS_Utf8ToUnicode") else None
if SYS_Utf8ToUnicode:
    SYS_Utf8ToUnicode.restype = ctypes.c_bool
    SYS_Utf8ToUnicode.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_wchar), ctypes.POINTER(ctypes.c_int)]
#  UNICODE -> UTF8
# HPSOCKET_API BOOL __stdcall SYS_UnicodeToUtf8(const WCHAR szSrc[], char szDest[], int* piDestLength);
SYS_UnicodeToUtf8 = HPSocketDLL.SYS_UnicodeToUtf8 if hasattr(HPSocketDLL, "SYS_UnicodeToUtf8") else None
if SYS_UnicodeToUtf8:
    SYS_UnicodeToUtf8.restype = ctypes.c_bool
    SYS_UnicodeToUtf8.argtypes = [ctypes.POINTER(ctypes.c_wchar), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int)]
#  GBK -> UTF8
# HPSOCKET_API BOOL __stdcall SYS_GbkToUtf8(const char szSrc[], char szDest[], int* piDestLength);
SYS_GbkToUtf8 = HPSocketDLL.SYS_GbkToUtf8 if hasattr(HPSocketDLL, "SYS_GbkToUtf8") else None
if SYS_GbkToUtf8:
    SYS_GbkToUtf8.restype = ctypes.c_bool
    SYS_GbkToUtf8.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int)]
#  UTF8 -> GBK
# HPSOCKET_API BOOL __stdcall SYS_Utf8ToGbk(const char szSrc[], char szDest[], int* piDestLength);
SYS_Utf8ToGbk = HPSocketDLL.SYS_Utf8ToGbk if hasattr(HPSocketDLL, "SYS_Utf8ToGbk") else None
if SYS_Utf8ToGbk:
    SYS_Utf8ToGbk.restype = ctypes.c_bool
    SYS_Utf8ToGbk.argtypes = [ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_int)]

#  普通压缩
# HPSOCKET_API int __stdcall SYS_Compress(const BYTE* lpszSrc, DWORD dwSrcLen, BYTE* lpszDest, DWORD* pdwDestLen);
SYS_Compress = HPSocketDLL.SYS_Compress if hasattr(HPSocketDLL, "SYS_Compress") else None
if SYS_Compress:
    SYS_Compress.restype = ctypes.c_int
    SYS_Compress.argtypes = [ctypes.POINTER(ctypes.c_byte), ctypes.c_uint, ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_uint)]
#  高级压缩（默认值：iLevel -> -1，iMethod -> 8，iWindowBits -> 15，iMemLevel -> 8，iStrategy -> 0）
# HPSOCKET_API int __stdcall SYS_CompressEx(const BYTE* lpszSrc, DWORD dwSrcLen, BYTE* lpszDest, DWORD* pdwDestLen, int iLevel, int iMethod, int iWindowBits, int iMemLevel, int iStrategy);
SYS_CompressEx = HPSocketDLL.SYS_CompressEx if hasattr(HPSocketDLL, "SYS_CompressEx") else None
if SYS_CompressEx:
    SYS_CompressEx.restype = ctypes.c_int
    SYS_CompressEx.argtypes = [ctypes.POINTER(ctypes.c_byte), ctypes.c_uint, ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_uint), ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int]
#  普通解压
# HPSOCKET_API int __stdcall SYS_Uncompress(const BYTE* lpszSrc, DWORD dwSrcLen, BYTE* lpszDest, DWORD* pdwDestLen);
SYS_Uncompress = HPSocketDLL.SYS_Uncompress if hasattr(HPSocketDLL, "SYS_Uncompress") else None
if SYS_Uncompress:
    SYS_Uncompress.restype = ctypes.c_int
    SYS_Uncompress.argtypes = [ctypes.POINTER(ctypes.c_byte), ctypes.c_uint, ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_uint)]
#  高级解压（默认值：iWindowBits -> 15）
# HPSOCKET_API int __stdcall SYS_UncompressEx(const BYTE* lpszSrc, DWORD dwSrcLen, BYTE* lpszDest, DWORD* pdwDestLen, int iWindowBits);
SYS_UncompressEx = HPSocketDLL.SYS_UncompressEx if hasattr(HPSocketDLL, "SYS_UncompressEx") else None
if SYS_UncompressEx:
    SYS_UncompressEx.restype = ctypes.c_int
    SYS_UncompressEx.argtypes = [ctypes.POINTER(ctypes.c_byte), ctypes.c_uint, ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_uint), ctypes.c_int]
#  推测压缩结果长度
# HPSOCKET_API DWORD __stdcall SYS_GuessCompressBound(DWORD dwSrcLen, BOOL bGZip);
SYS_GuessCompressBound = HPSocketDLL.SYS_GuessCompressBound if hasattr(HPSocketDLL, "SYS_GuessCompressBound") else None
if SYS_GuessCompressBound:
    SYS_GuessCompressBound.restype = ctypes.c_uint
    SYS_GuessCompressBound.argtypes = [ctypes.c_uint, ctypes.c_bool]

#  Gzip 压缩
# HPSOCKET_API int __stdcall SYS_GZipCompress(const BYTE* lpszSrc, DWORD dwSrcLen, BYTE* lpszDest, DWORD* pdwDestLen);
SYS_GZipCompress = HPSocketDLL.SYS_GZipCompress if hasattr(HPSocketDLL, "SYS_GZipCompress") else None
if SYS_GZipCompress:
    SYS_GZipCompress.restype = ctypes.c_int
    SYS_GZipCompress.argtypes = [ctypes.POINTER(ctypes.c_byte), ctypes.c_uint, ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_uint)]
#  Gzip 解压
# HPSOCKET_API int __stdcall SYS_GZipUncompress(const BYTE* lpszSrc, DWORD dwSrcLen, BYTE* lpszDest, DWORD* pdwDestLen);
SYS_GZipUncompress = HPSocketDLL.SYS_GZipUncompress if hasattr(HPSocketDLL, "SYS_GZipUncompress") else None
if SYS_GZipUncompress:
    SYS_GZipUncompress.restype = ctypes.c_int
    SYS_GZipUncompress.argtypes = [ctypes.POINTER(ctypes.c_byte), ctypes.c_uint, ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_uint)]
#  推测 Gzip 解压结果长度（如果返回 0 或不合理值则说明输入内容并非有效的 Gzip 格式）
# HPSOCKET_API DWORD __stdcall SYS_GZipGuessUncompressBound(const BYTE* lpszSrc, DWORD dwSrcLen);
SYS_GZipGuessUncompressBound = HPSocketDLL.SYS_GZipGuessUncompressBound if hasattr(HPSocketDLL, "SYS_GZipGuessUncompressBound") else None
if SYS_GZipGuessUncompressBound:
    SYS_GZipGuessUncompressBound.restype = ctypes.c_uint
    SYS_GZipGuessUncompressBound.argtypes = [ctypes.POINTER(ctypes.c_byte), ctypes.c_uint]

#  计算 Base64 编码后长度
# HPSOCKET_API DWORD __stdcall SYS_GuessBase64EncodeBound(DWORD dwSrcLen);
SYS_GuessBase64EncodeBound = HPSocketDLL.SYS_GuessBase64EncodeBound if hasattr(HPSocketDLL, "SYS_GuessBase64EncodeBound") else None
if SYS_GuessBase64EncodeBound:
    SYS_GuessBase64EncodeBound.restype = ctypes.c_uint
    SYS_GuessBase64EncodeBound.argtypes = [ctypes.c_uint]
#  计算 Base64 解码后长度
# HPSOCKET_API DWORD __stdcall SYS_GuessBase64DecodeBound(const BYTE* lpszSrc, DWORD dwSrcLen);
SYS_GuessBase64DecodeBound = HPSocketDLL.SYS_GuessBase64DecodeBound if hasattr(HPSocketDLL, "SYS_GuessBase64DecodeBound") else None
if SYS_GuessBase64DecodeBound:
    SYS_GuessBase64DecodeBound.restype = ctypes.c_uint
    SYS_GuessBase64DecodeBound.argtypes = [ctypes.POINTER(ctypes.c_byte), ctypes.c_uint]
#  Base64 编码（返回值：0 -> 成功，-3 -> 输入数据不正确，-5 -> 输出缓冲区不足）
# HPSOCKET_API int __stdcall SYS_Base64Encode(const BYTE* lpszSrc, DWORD dwSrcLen, BYTE* lpszDest, DWORD* pdwDestLen);
SYS_Base64Encode = HPSocketDLL.SYS_Base64Encode if hasattr(HPSocketDLL, "SYS_Base64Encode") else None
if SYS_Base64Encode:
    SYS_Base64Encode.restype = ctypes.c_int
    SYS_Base64Encode.argtypes = [ctypes.POINTER(ctypes.c_byte), ctypes.c_uint, ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_uint)]
#  Base64 解码（返回值：0 -> 成功，-3 -> 输入数据不正确，-5 -> 输出缓冲区不足）
# HPSOCKET_API int __stdcall SYS_Base64Decode(const BYTE* lpszSrc, DWORD dwSrcLen, BYTE* lpszDest, DWORD* pdwDestLen);
SYS_Base64Decode = HPSocketDLL.SYS_Base64Decode if hasattr(HPSocketDLL, "SYS_Base64Decode") else None
if SYS_Base64Decode:
    SYS_Base64Decode.restype = ctypes.c_int
    SYS_Base64Decode.argtypes = [ctypes.POINTER(ctypes.c_byte), ctypes.c_uint, ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_uint)]

#  计算 URL 编码后长度
# HPSOCKET_API DWORD __stdcall SYS_GuessUrlEncodeBound(const BYTE* lpszSrc, DWORD dwSrcLen);
SYS_GuessUrlEncodeBound = HPSocketDLL.SYS_GuessUrlEncodeBound if hasattr(HPSocketDLL, "SYS_GuessUrlEncodeBound") else None
if SYS_GuessUrlEncodeBound:
    SYS_GuessUrlEncodeBound.restype = ctypes.c_uint
    SYS_GuessUrlEncodeBound.argtypes = [ctypes.POINTER(ctypes.c_byte), ctypes.c_uint]
#  计算 URL 解码后长度
# HPSOCKET_API DWORD __stdcall SYS_GuessUrlDecodeBound(const BYTE* lpszSrc, DWORD dwSrcLen);
SYS_GuessUrlDecodeBound = HPSocketDLL.SYS_GuessUrlDecodeBound if hasattr(HPSocketDLL, "SYS_GuessUrlDecodeBound") else None
if SYS_GuessUrlDecodeBound:
    SYS_GuessUrlDecodeBound.restype = ctypes.c_uint
    SYS_GuessUrlDecodeBound.argtypes = [ctypes.POINTER(ctypes.c_byte), ctypes.c_uint]
#  URL 编码（返回值：0 -> 成功，-3 -> 输入数据不正确，-5 -> 输出缓冲区不足）
# HPSOCKET_API int __stdcall SYS_UrlEncode(BYTE* lpszSrc, DWORD dwSrcLen, BYTE* lpszDest, DWORD* pdwDestLen);
SYS_UrlEncode = HPSocketDLL.SYS_UrlEncode if hasattr(HPSocketDLL, "SYS_UrlEncode") else None
if SYS_UrlEncode:
    SYS_UrlEncode.restype = ctypes.c_int
    SYS_UrlEncode.argtypes = [ctypes.POINTER(ctypes.c_byte), ctypes.c_uint, ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_uint)]
#  URL 解码（返回值：0 -> 成功，-3 -> 输入数据不正确，-5 -> 输出缓冲区不足）
# HPSOCKET_API int __stdcall SYS_UrlDecode(BYTE* lpszSrc, DWORD dwSrcLen, BYTE* lpszDest, DWORD* pdwDestLen);
SYS_UrlDecode = HPSocketDLL.SYS_UrlDecode if hasattr(HPSocketDLL, "SYS_UrlDecode") else None
if SYS_UrlDecode:
    SYS_UrlDecode.restype = ctypes.c_int
    SYS_UrlDecode.argtypes = [ctypes.POINTER(ctypes.c_byte), ctypes.c_uint, ctypes.POINTER(ctypes.c_byte), ctypes.POINTER(ctypes.c_uint)]


