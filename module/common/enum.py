#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016-7-23
@author: huaihuai
'''

from enum import Enum

rtypeEnum = Enum('rtypeEnum', 'aspect,fitment,floor,property,account,own')

aspectEnum = Enum('aspectEnum', '东,西,南,北,东西,东南,东北,西南,西北,南北,不确定')
fitmentEnum = Enum('fitmentEnum', '不确定,精装修,中装修,简装修,毛坯')
floorEnum = Enum('floorEnum', '低,中,高')
propertyEnum = Enum('propertyEnum', '不确定,住宅,公寓,别墅,平房')
accountEnum = Enum('accountEnum', '不确定,月付,季付,半年付,年付')
