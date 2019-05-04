#! /home/bingo/anaconda3/bin/python
# *- coding=utf-8 -*

__author__ = "ZzLee"
__date__ = "2019/04/27"
__mail__ = "zhangmeng.lee@foxmail.com"

"""
    标准库中的迭代器
"""
"""用于过滤"""
# 返回字符串中的元音字母, 不区分大小写
def vowel(char):
    return char.lower() in 'aeiou'
list(filter(vowel, 'abcdesfg'))
# ['a', 'e']
# 返回字符串中的非元音字母, 不区分大小写
import itertools
list(itertools.filterfalse(vowel, 'abcdesfg'))
# ['b', 'c', 'd', 'e', 's', 'f', 'g']
# 同上
list(itertools.dropwhile(vowel, 'abcdesfg'))
# ['b', 'c', 'd', 'e', 's', 'f', 'g']

# 只要遇到非元音字母, 就停止
list(itertools.takewhile(vowel, 'abcdesfg'))
# ['a']

# 第二个可迭代对象中, 为真, 取出对应的第一个可迭代对象中的元素
list(itertools.compress('asdf', [1, 0, 1, 0]))
# ['a', 'd']

"""用于映射"""
# map, 可以接受多个可迭代对象, 与此同时映射函数的参数要匹配
import operator
list(map(operator.add, [1, 2, 3], [9, 8, 7]))
# [10, 10, 10]

# enumerate, 返回元组, 第二个参数可以设置
list(enumerate(range(1, 5), 1))
# [(1, 1), (2, 2), (3, 3), (4, 4)]

# accumulate 累积. 若无函数参数, 累积和
list(itertools.accumulate([1, 2, 3]))
# [1, 3, 6]
# 有函数参数
list(itertools.accumulate([1, 2, 3, 4], operator.mul))
# [1, 2, 6, 24]


"""用于合并"""

#1. one by one
# chain 将多个可迭代对象, 链接在一起
list(itertools.chain('abc', [1, 2, 3]))
# >>> ['a', 'b', 'c', 1, 2, 3]
# chain.from_iterable 接受的可迭代对象中的元素, 需要是可迭代对象
list(itertools.chain.from_iterable(enumerate('ABC')))
# >>> [0, 'A', 1, 'B', 2, 'C']


#2. mul to one
# zip 函数具有最短板效应
list(zip(range(10), 'ab'))
# >>> [(0, 'a'), (1, 'b')]
# zip_longest 函数具有最长板效应
list(itertools.zip_longest(range(4), 'ab', fillvalue='?'))
# >>> [(0, 'a'), (1, 'b'), (2, '?'), (3, '?')]
# 计算笛卡尔积
list(itertools.product('AB', 'abc'))
# >>> [('A', 'a'), ('A', 'b'), ('A', 'c'), ('B', 'a'), ('B', 'b'), ('B', 'c')]