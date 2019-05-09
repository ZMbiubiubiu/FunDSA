#! /home/bingo/anaconda3/bin/python
# *- coding=utf-8 -*


__date__ = "2019/05/03"
__author__ = "ZzLee"
__mail__ = "zhangmeng.lee@foxmail.com"
__version__ = "1.0"

"""
    定义一个字典类,实现功能如下
    如果字典的内容为d = { '1': 'one' }
    则满足 d['1'] = 'one'
          d[1] = 'one'
          d['2'] --> KeyError
"""

class Dict(dict):
    def __missing__(self, key):
        if isinstance(key, str): #如果键本来是字符串还找不到,那就真的无能为力了
            raise KeyError
        return self[str(key)]
    # __missing__的提供并不会影响get, get为了实现键自动转换到字符的功能,需要自己定义逻辑
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
    # 同样的理由
    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()