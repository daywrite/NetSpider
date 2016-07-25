#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2016-7-25
@author: huaihuai
'''


class export_format(object):
    _source = ['省', '市', '行政区', '小区']
    _des = ['行政', '小区啊']

    def __init__(self, source=_source, des=_des):
        if source is None:
            self.source = self._source
        else:
            self.source = source

        if des is None:
            self.des =self ._des
        else:
            self.des = des

    def relationship(self, input):
        # 判断input是否为字典

        result = {}

        source_ship = export_format.get_position(self.source)
        des_ship = export_format.get_position(self.des)

        for index in input.keys():
            if index in source_ship and input[index] in des_ship:
                result[source_ship[index]] = des_ship[input[index]]
            else:
                pass

        # 验证
        if len(result) != len(input):
            return {'error': 'input输入有误'}
        else:
            return result

    @staticmethod
    def get_position(content):
        # 判断是否是数组
        result = {}
        i = -1
        for index in content:
            i += 1
            result[index] = i

        return result




