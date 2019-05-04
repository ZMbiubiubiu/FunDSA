#! /home/bingo/anaconda3/bin/python
# *- coding=utf-8 -*


__date__ = "2019/05/03"
__author__ = "ZzLee"
__mail__ = "zhangmeng.lee@foxmail.com"
__version__ = "1.0"

"""
    学习python风格的类编程, 为了实现一致性.
    在Vector2D这个向量类中, 尽可能多实现各种函数与行为
    具体情况如代码所示
"""
# 定义一个向量类
from math import hypot
from math import atan2
from array import array

class Vector2D:
    typecode = "d"
    def __init__(self, x, y):
        self._x = float(x)
        self._y = float(y)
    # 设置为只读属性
    # 为了实现可散列, 因为散列值一旦计算出来, 不能改变
    # 这个向量类使用x,y来计算散列值. 所以才设置为只读属性

    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y

    # 可哈希
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)
    
    # 可迭代
    def __iter__(self):
        return (i for i in (self.x, self.y))

    # 打印结果对于开发者有提示作用(比如是如何构造的)
    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    # 打印结果对于用户有提示作用(比如显示实例的内容)
    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))
    @classmethod #类方法要用此装饰器
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    # 相等性判断
    def __eq__(self, other):
        """
            之所以能用tuple构造, 是因为上面定义了__iter__函数
        """
        return tuple(self) == tuple(other)

    # 向量的模
    def __abs__(self):
        return hypot(*self)

    # 向量的角度(弧度)
    def angle(self):
        return atan2(self.y, self.x)

    # 自定义格式化输出
    def __format__(self, fmt_spec = ""):
        """
            p结尾,会以极坐标的形式打印
        """
        if fmt_spec.endswith("p"):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            out_fmt = '<{}, {}>'
        else:
            coords = self
            out_fmt = '({}, {})'
        components = [format(c, fmt_spec) for c in coords]
        return out_fmt.format(*components)
        
    # 布尔值
    def __bool__(self):
        return bool(abs(self))