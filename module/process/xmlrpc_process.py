#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016-7-27
@author: huaihuai
'''

import xmlrpc.client


class Communication(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def connect(self):
        return xmlrpc.client.ServerProxy(self.get_address(self.ip, self.port))

    @staticmethod
    def get_address(ip, port):
        return 'http://{ip}:{port}'.format(ip=ip, port=port)


if __name__ == '__main__':
    client = Communication('127.0.0.1', 8000).connect()
    print(client.got_result(1))
