# This works for ida v7 import using File->open script command. Alternative you can copy and paste it into the output window
# -*- coding: utf-8 -*-
import json
import idaapi
import idc

imageBase = idaapi.get_imagebase()

def get_addr(addr):
    return imageBase + addr

def set_name(addr, name):
    ret = idc.set_name(addr, name, idc.SN_NOWARN | idc.SN_NOCHECK)
    if ret == 0:
        new_name = name + '_' + str(addr)
        ret = idc.set_name(addr, new_name, idc.SN_NOWARN | idc.SN_NOCHECK)

def make_function(start, end):
    next_func = idc.get_next_func(start)
    if next_func < end:
        end = next_func
    if idc.get_func_attr(start, idc.FUNCATTR_START) == start:
        ida_funcs.del_func(start)
    ida_funcs.add_func(start, end)

path = idaapi.ask_file(False, '*.json', 'script.json')
data = json.loads(open(path, 'rb').read().decode('utf-8'))

for function in data["Functions"]:
    addr = get_addr(function["Address"])
    name = function["Name"]  # Don't encode to bytes
    set_name(addr, name)

print('Script finished!')
