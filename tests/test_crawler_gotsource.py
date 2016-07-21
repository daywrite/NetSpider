#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016-7-21
@author: huaihuai
'''

import unittest
from module.crawler.gotsource import *


class Test(unittest.TestCase):
    def testHelloWorld(self):
        hw=HelloWorld('hello world')
        self.assertEqual('hello world',hw.HW())


if __name__ == "__main__":
    unittest.main()
