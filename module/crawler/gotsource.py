#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016-7-21
@author: huaihuai
'''


class HelloWorld(object):
    def __init__(self,content):
        self.content=content

    def HW(self):
        print(self.content)
        return self.content


if __name__ == '__main__':
    HelloWorld('123').HW()
