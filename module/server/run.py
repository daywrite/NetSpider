#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016-7-27
@author: huaihuai
'''

import threading
import time
from xmlrpc.server import SimpleXMLRPCServer, socketserver


# RPC-多线程
class RPCThreading(socketserver.ThreadingMixIn, SimpleXMLRPCServer):
    pass


# 全局锁
global mutex
mutex = threading._allocate_lock()


class RPCMultithreading(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def create(self):
        server_object = Server()
        server = RPCThreading((self.ip, self.port), logRequests=False)
        server.allow_none = True
        server.register_instance(server_object)
        print('多线程RPC服务器已开启......')
        server.serve_forever()


class Server(object):
    def __init__(self):
        pass

    def got_result(self, num):
        time.sleep(1)
        return num + 1


if __name__ == '__main__':
    RPCMultithreading('127.0.0.1', 8000).create()
