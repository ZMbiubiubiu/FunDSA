#! /home/bingo/anaconda3/bin/python
# *- coding=utf-8 -*


__date__ = "2019/05/03"
__author__ = "ZzLee"
__mail__ = "zhangmeng.lee@foxmail.com"
__version__ = "1.0"

"""
    探讨如何编写集合类广泛使用的几个特殊方法
    包括切片/
"""

from array import array
import math
import reprlib
import numbers
import functools
import operator
import itertools

class Vector:
    # 类属性
    typecode = "d"
    shortcut_names = 'xyz'

    # 构造函数, 接受一个可迭代对象
    def __init__(self, components):
        self._components = array(self.typecode, components)
        
    # 支持迭代
    def __iter__(self):
        return iter(self._components)
    
    # 支持len
    def __len__(self):
        return len(self._components)
    
    # 支持切片和索引
    def __getitem__(self, index):
        cls = type(self) # 获取实例所属的类
        if isinstance(index, slice):
            return cls(self._components[index]) # 若是切片, 返回一个新的Vector
        elif isinstance(index, numbers.Integral):
            return self._components[index]      # 若是整数, 返回一个值
        else:
            msg = f'{cls.__name__} indices must be integrals' # 否则报错
            raise TypeError(msg)

    # 支持前几个元素别名, 比如V.x, V.y, V.z .其中V.x == V[0]
    # 使用此方法的时机. 示例/类属性没有要查询(此处的name)的属性, 继承树上也没有
    # 才会调用此方法
    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            index = cls.shortcut_names.find(name)
            if index >= 0:
                return self._components[index]
        msg = f'{cls.__name__!r} has no attribute {name!r}'
        raise AttributeError(msg)
    # 以上还不够, 我们还需要实现 setattr.(以防你瞎赋值给示例属性)
    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = f"readonly attribute {name!r}"
            elif name.islower():
                error = f"can't set attributes 'a' to 'z' in {cls.__name__!r}"
            else:
                error = ""
            if error:
                raise AttributeError(error)
        super().__setattr__(name, value)
        

    # 使用reprlib库打印有限元素
    def __repr__(self):
        components = reprlib.repr(self._components) # 经包装, 变成有限长度的字符串
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    # 需要实现__iter__
    def __str__(self):
        return str(tuple(self))

    # 转换成字节序列
    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._components) #注意表达式第一部分, 参数是列表
    
    # 相等性判断
    def __eq__(self, other):
        # return tuple(self) == tuple(other) #效率低下
        # 首先判断长度, 再次判断各个值, 用zip生成的生成器
        return len(self) == len(other) and all(a==b for a,b in zip(self, other))

    # 可散列
    def __hash__(self):
        hashs = (hash(i) for i in self._components)
        # 第三个参数的设置应为恒等值, 对于异或运算来说, 应为0
        return functools.reduce(operator.xor, hash, 0)
    
    # 向量的模
    def __abs__(self):
        return math.sqrt(sum(i*i for i in self))

    # 格式化字符串
    def angle(self, n): 
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n-1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a
    def angles(self): 
        return (self.angle(n) for n in range(1, len(self)))
    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'): # 超球面坐标
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles()) 
            outer_fmt = '<{}>' 
        else:
            coords = self
            outer_fmt = '({})' 
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))

    # bool
    def __bool__(self):
        return bool(abs(self))

    # 由字节序列转换成Vector对象
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == "__main__":
    v = Vector(i for i in range(10))
    dump = bytes(v)
    print(v.frombytes(dump))
