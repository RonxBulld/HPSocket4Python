# coding: utf-8

import ctypes

def SizeOf(ctypes_obj):
    return ctypes.sizeof(ctypes_obj)


def MakePointer(ctypes_obj):
    return ctypes.pointer(ctypes_obj)

