#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016-7-23
@author: huaihuai
'''

from enum import Enum

rtypeEnum = Enum('rtypeEnum', 'aspect,fitment,floor,own')

aspectEnum = Enum('aspectEnum', '东,西,南,北,东西,东南,东北,西南,西北,南北,不确定')
fitmentEnum = Enum('fitmentEnum', '不确定,精装修,中装修,简装修,毛坯')
floorEnum = Enum('floorEnum', '低,中,高')
