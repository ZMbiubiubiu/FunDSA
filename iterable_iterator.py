#! /home/bingo/anaconda3/bin/python
# *- coding=utf-8 -*


__date__ = "2019/05/04"
__author__ = "ZzLee"
__mail__ = "zhangmeng.lee@foxmail.com"
__version__ = "1.0"

"""
    可迭代对象/迭代器/生成器
    1.序列可以迭代的原因:iter函数
        解释器需要迭代对象 x 时,会自动调用 iter(x)。
        内置的 iter 函数有以下作用。
            (1) 检查对象是否实现了 __iter__ 方法,如果实现了就调用它,获取
                一个迭代器。(查看Sentence2)
            (2) 如果没有实现 __iter__ 方法,但是实现了 __getitem__ 方法,
                Python 会创建一个迭代器,尝试按顺序(从索引 0 开始)获取元素。(查看Sentence1)
            (3) 如果尝试失败,Python 抛出 TypeError 异常,通常会提示“C object
                is not iterable”(C 对象不可迭代),其中 C 是目标对象所属的类。
    我们要明确可迭代的对象和迭代器之间的关系:Python 从可迭代的对象中获取迭代器(可以查看Sentence2)

    2.如何构造迭代器?
        标准的迭代器接口有两个方法。(查看SentenceIterator的实现)
        __next__
            返回下一个可用的元素,如果没有元素了,抛出 StopIteration异常。
        __iter__
            返回 self,以便在应该使用可迭代对象的地方使用迭代器,例如在 for 循环中。
    3.关于迭代器的总结
        因为迭代器只需 __next__ 和 __iter__ 两个方法,所以除了调用
        next() 方法,以及捕获 StopIteration 异常之外,没有办法检查是
        否还有遗留的元素。此外,也没有办法“还原”迭代器。如果想再次迭
        代,那就要调用 iter(...),传入之前构建迭代器的可迭代对象。传
        入迭代器本身没用,因为前面说过 Iterator.__iter__ 方法的实现
        方式是返回实例本身,所以传入迭代器无法还原已经耗尽的迭代器.
    4.生成器
        (1) 生成器函数
            生成器函数的工作原理
                只要 Python 函数的定义体中有 yield 关键字,该函数就是生成器函
                数。调用生成器函数时,会返回一个生成器对象。也就是说,生成器函
                数是生成器工厂。
                如Sentence3, __iter__方法是生成器函数,调用时会构建一个实现了迭代器接口的生成器对象
        (2) 生成器表达式
            
"""

# 实现__getitem__实现可迭代
import reprlib
import re
WORD_RE = re.compile('\w+')
class Sentence1:
    def __init__(self, text):
        self.text = text
        self.words = WORD_RE.findall(self.text)
    
    def __getitem__(self, position):
        return self.words[position]
    
    def __len__(self):
        return len(self.words)
    
    def __repr__(self):
        return f'{type(self).__name__}({reprlib.repr(self.text)!r})'


# 实现标准的可迭代协议, 即实现__iter__, 返回一个迭代器
import re
import reprlib
WORD_RE = re.compile('\w+')

class Sentence2:
    def __init__(self, text):
        self.text = text
        self.words = WORD_RE.findall(self.text)
    
    def __repr__(self):
        return f'{type(self).__name__}({reprlib.repr(self.text)!r})'
    # 明确表明这个类可以迭代
    def __iter__(self):
        # 根据可迭代协议, 此方法返回一个Iterator
        return SentenceIterator(self.words)

class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0
    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word
    def __iter__(self):
        return self


# 使用生成器, 更符合python风格
import re
import reprlib

WORD_RE = re.compile('\w+')

class Sentence3:
    def __init__(self, text):
        self.text = text
        self.words = WORD_RE.findall(self.text)
    
    def __repr__(self):
        return f'{type(self).__name__}({reprlib.repr(self.text)!r})'
    # __iter__ 方法是生成器函数,调用时会构建一个实现了迭代
    # 器接口的生成器对象,因此不用再定义 SentenceIterator 类了。
    def __iter__(self):
        """
            利用生成器
        """
        for word in self.words:
            yield word


# 惰性实现
import re
import reprlib

class Sentence4:
    def __init__(self, text):
        self.text = text
    def __repr__(self):
        return f'{type(self).__name__}({reprlib.repr(self.text)!r})'
    def __iter__(self):
        # 调用此方法会得到一个生成器对象
        for match in WORD_RE.finditer(self.text):
            yield match.group()

# 更加厉害的多形实现, 使用生成器表达式
import re
import reprlib

class Sentence4:
    def __init__(self, text):
        self.text = text
    def __repr__(self):
        return f'{type(self).__name__}({reprlib.repr(self.text)!r})'
    def __iter__(self):
        # 调用此方法同样获得一个生成器对象
        return (match.group() for match in WORD_RE.finditer(self.text))