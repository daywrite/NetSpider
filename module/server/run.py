#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016-7-27
@author: huaihuai
'''
from xmlrpc.server import SimpleXMLRPCServer


class Server(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def Create(self):
        return SimpleXMLRPCServer((self.ip, self.port))


def got_result(num):
    return num + 1


if __name__ == '__main__':
    rpcserver = Server('127.0.0.1', 8000).Create()
    print('服务已启动')
    rpcserver.register_function(got_result, 'got_result')
    rpcserver.serve_forever()
