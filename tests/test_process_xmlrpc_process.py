#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016-7-27
@author: huaihuai
'''
import unittest
from module.process.xmlrpc_process import *


class Test(unittest.TestCase):
    def testget_address(self):
        self.assertEqual('http://127.0.0.1:8000', Communication.get_address('127.0.0.1', '8000'))


if __name__ == "__main__":
    unittest.main()
