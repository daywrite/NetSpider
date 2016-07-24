#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016-7-23
@author: huaihuai
'''

from module.common.enum import *
from module.tools.parameters import *

# 可以用*keyword改变更灵活
class utils_gotcode_rule(object):
    _aspect = [aspectEnum.不确定.name, aspectEnum.南北.name, aspectEnum.东西.name, aspectEnum.东南.name,
               aspectEnum.东北.name, aspectEnum.西南.name, aspectEnum.西北.name, aspectEnum.南.name,
               aspectEnum.北.name, aspectEnum.东.name, aspectEnum.西.name]
    _fitment = [fitmentEnum.不确定.name, fitmentEnum.不确定.name, fitmentEnum.精装修.name, fitmentEnum.中装修.name,
                fitmentEnum.简装修.name, fitmentEnum.毛坯.name]
    _floor = [floorEnum.低.name, floorEnum.中.name, floorEnum.高.name]
    _property=[propertyEnum.不确定.name,propertyEnum.住宅.name,propertyEnum.公寓.name,propertyEnum.别墅.name,propertyEnum.平房.name]
    _account=[accountEnum.不确定.name,accountEnum.月付.name,accountEnum.季付.name,accountEnum.半年付.name,accountEnum.年付.name]

    @validParam(default=int)
    def __init__(self, rtype=rtypeEnum.aspect.name, content=_aspect, **kwargs):
        self.content = content
        self.rtype = rtype

        if 'default' in kwargs:
            self.default = kwargs['default']
        else:
            self.default = 0

        if 'begin' in kwargs:
            self.begin = kwargs['begin']
        else:
            self.begin = -1

    def gotcontent(self):
        if self.rtype == rtypeEnum.aspect.name:
            self.content = self._aspect
        elif self.rtype == rtypeEnum.fitment.name:
            self.content = self._fitment
        elif self.rtype == rtypeEnum.floor.name:
            self.content = self._floor
        elif self.rtype == rtypeEnum.property.name:
            self.content = self._property
        elif self.rtype == rtypeEnum.account.name:
            self.content = self._account
        else:
            self.content = self.content

    def gotcode(self, input):
        self.gotcontent()
        i = self.begin
        for index in self.content:
            i += 1
            if index in input:
                return i

        return self.default


class utils(object):
    @staticmethod
    def gotaspect(content):
        if '南北' in content:
            return 1
        else:
            return 99
