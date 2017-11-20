#!/usr/bin/env python
# encoding: utf-8


"""
@version: 0.01
@author: zxs
@contact: xiaoshan.zhou@bayesba.com
@site: http://www.bayesba.com
@software: PyCharm
@file: types_utils.py
@time: 17-7-18 下午6:18
"""

import types

def is_none(value):
	return type(value) == types.NoneType

def is_string(value):
	return type(value) == types.StringType

def is_boolean(value):
	return type(value) == types.BooleanType

def is_int(value):
	return type(value) == types.IntType

def is_float(value):
	return type(value) == types.FloatType

def is_number(value):
	return is_int(value) or is_float(value)

def is_list(value):
	return type(value) == types.ListType

def is_dict(value):
	return type(value) == types.DictType