#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016-7-25
@author: huaihuai
'''

import tornado.ioloop


class Fetcher(object):
    def __init__(self):
        self.ioloop = tornado.ioloop.IOLoop()

    def run(self):
        def queue_loop():
            print('执行queue_loop')

        tornado.ioloop.PeriodicCallback(queue_loop, 1000, io_loop=self.ioloop).start()

        try:
            self.ioloop.start()
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    Fetcher().run()
