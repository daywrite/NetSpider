#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016-7-25
@author: huaihuai
'''

import unittest
from module.tools.export import *


class Test(unittest.TestCase):
    def testexport_format(self):
        input = {'行政区': '行政', '小区': '小区啊'}
        result = export_format().relationship(input)

        self.assertEqual(2, len(result))
        self.assertEqual(0,result[2])
        self.assertEqual(1,result[3])

        error_input = {'政区': '行政', '小区': '小区啊'}
        error_result = export_format().relationship(error_input)

        self.assertTrue('error' in error_result)

        own_input = {'行政区': '行政', '小区': '小区啊'}
        own_result = export_format(['行政区','小区'],['行政','小区啊']).relationship(own_input)

        self.assertEqual(2, len(own_result))

        self.assertEqual(0,own_result[0])
        self.assertEqual(1,own_result[1])


if __name__ == "__main__":
    unittest.main()
