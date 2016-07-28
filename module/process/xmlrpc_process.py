#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016-7-27
@author: huaihuai
'''
import threading
import xmlrpc.client


class Communication(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def connect(self, is_allow_none=True):
        return xmlrpc.client.ServerProxy(self.get_address(self.ip, self.port), allow_none=is_allow_none)

    @staticmethod
    def get_address(ip, port):
        return 'http://{ip}:{port}'.format(ip=ip, port=port)


def run(i):
    client = Communication('127.0.0.1', 8000).connect()
    print(client.got_result(i))

if __name__ == '__main__':
    client = Communication('127.0.0.1', 8000).connect()
    print(client.got_result(1))

    # thpool = []
    #
    # for i in range(10):
    #     thpool.append(threading.Thread(target=run,args=(i,)))
    # for th in thpool:
    #     th.start()
    # for th in thpool:
    #     th.join()
    print('所有线程执行完毕')
