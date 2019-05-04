#! /home/bingo/anaconda3/bin/python
# *- coding=utf-8 -*

__author__ = "ZzLee"
__date__ = "2019/05/01"
__mail__ = "zhangmeng.lee@foxmail.com"
__version__ = "1.0"

"""
    用双向链表实现stack
"""

class ListNode:
    """
    双向链表的节点
    data:节点值
    prev:前驱节点
    succ:后继节点
    """
    def __init__(self,data, prev=None, succ=None):
        self.data = data
        self.prev = prev
        self.succ = succ
    
    def insertAsPrev(self, e:'data'):
        # 创建新节点, 并且设置链接
        node = ListNode(data=e, prev=self.prev, succ=self)
        self.prev.succ = node
        self.prev = node
    
    def insertAsSucc(self, e:'data'):
        # 创建节点, 并且设置链接
        node = ListNode(data=e, prev=self, succ=self.succ)
        self.succ.prev = node
        self.prev = node
    def __repr__(self):
        """
        用字符串来显示这个节点
        """
        return repr(self.data)


# 用双线链表实现栈
class Stack:
    def __init__(self):
        self._size = 0
        # 创建头尾哨兵, 并且链接
        self.header = ListNode(data='header')
        self.trailer = ListNode(data='trailer')
        self.header.succ=self.trailer
        self.trailer.prev = self.header
    
    def __repr__(self):
        """
        用字符串的形式展示栈:即列出栈中的所有数据
        """
        nodes = []
        node = self.header.succ
        sentinal = self.trailer.data
        while (node.data != sentinal):
            nodes.append(repr(node.data))
            node = node.succ
        return '[' + ','.join(nodes) + ']'

    def size(self):
        """
        记录规模
        """
        return self._size
    
    def empty(self) :
        """
        判空
        """
        return self._size <= 0
    
    def insertAsLast(self, e:'data'):
        """
        插入作为尾节点
        """
        return self.trailer.insertAsPrev(e)
    

    
    def push(self, e:'data'):
        """
        入栈
        """
        self._size += 1
        self.insertAsLast(e)
    
    def pop(self):
        """
        出栈
        """
        if self.empty():
            raise LookupError("can't pop from empty stack")
        self._size -= 1
        # 保存尾节点
        node = self.trailer.prev
        node.prev.succ = self.trailer
        self.trailer.prev = node.prev
        node.prev = None
        node.succ = None
        return node

if __name__ == "__main__":
    s = Stack()
    s.push(2)
    s.push(3)
    s.push(4)
    print(s)
    s.pop()
    s.pop()
    print(s)

