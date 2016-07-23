#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016-7-21
@author: huaihuai
'''

import unittest
from module.tools.rules import *


class Test(unittest.TestCase):
    def testgotaspect(self):
        self.assertEqual(1, utils.gotaspect('南北'))
        self.assertEqual(99, utils.gotaspect('南'))

    def testgotaspect1(self):
        self.assertEqual(1, utils_gotcode_rule().gotcode('南北'))
        self.assertEqual(0, utils_gotcode_rule().gotcode('不确定'))

        self.assertEqual(0, utils_gotcode_rule(rtypeEnum.aspect.name).gotcode('不确定'))

        self.assertEqual(2, utils_gotcode_rule(rtypeEnum.fitment.name).gotcode('精装修'))
        self.assertEqual(5, utils_gotcode_rule(rtypeEnum.fitment.name).gotcode('毛坯'))
        self.assertEqual(0, utils_gotcode_rule(rtypeEnum.fitment.name).gotcode('哈哈'))
        self.assertEqual(1, utils_gotcode_rule(rtypeEnum.fitment.name, '', 1).gotcode('哈哈'))

        self.assertEqual(0, utils_gotcode_rule(rtypeEnum.own.name, ['哈哈', '嘿嘿', '呵呵']).gotcode('哈哈'))
        self.assertEqual(0, utils_gotcode_rule(rtypeEnum.own.name, ['哈哈', '嘿嘿', '呵呵']).gotcode('拉拉'))
        self.assertEqual(2, utils_gotcode_rule(rtypeEnum.own.name, ['哈哈', '嘿嘿', '呵呵'], 2).gotcode('拉拉'))


if __name__ == "__main__":
    unittest.main()
