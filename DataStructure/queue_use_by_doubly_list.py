#! /home/bingo/anaconda3/bin/python
# *- coding=utf-8 -*

__author__ = "ZzLee"
__date__ = "2019/05/01"
__mail__ = "zhangmeng.lee@foxmail.com"
__version__ = "1.0"

"""
    用双向链表实现queue
"""

class ListNode:
    def __init__(self, data, prev=None, succ=None):
        self.data = data
        self.prev = prev
        self.succ = succ
    
    def __repr__(self):
        return repr(self.data)
    
    def insertAsPrev(self, e:'data'):
        node = ListNode(data=e, prev=self.prev, succ=self)
        self.prev.succ = node
        self.prev = node
    def insertAsSucc(self, e:'data'):
        node = ListNode(data=e, prev=self, succ=self.succ)
        self.succ.prev = node
        self.succ = node

# 用双向链表实现队列
class Queue:
    def __init__(self):
        # 规模
        self._size = 0
        # 创建头尾哨兵节点
        self.header = ListNode(data='header')
        self.trailer = ListNode(data='trailer')
        self.header.succ = self.trailer
        self.trailer.prev = self.header
    def __repr__(self):
        """
        用字符串展示队列, 打印队列中个节点的值
        """
        nodes = []
        node = self.header.succ
        sentinal = self.trailer.data
        while node.data != sentinal:
            nodes.append(repr(node.data))
            node = node.succ
        return '[' + ','.join(nodes) + ']'

    def size(self):
        """
        输出规模
        """
        return self._size
    
    def empty(self):
        """
        判空
        """
        return self.size() <= 0
    
    def insertAsLast(self, e:'data'):
        """
        """
        self.trailer.insertAsPrev(e)
    
    def enque(self, e:'data'):
        """
        入队
        """
        self._size += 1
        self.insertAsLast(e)

    def deque(self):
        """
        出队
        """
        if self.empty():
            raise LookupError("can't deque from empty queue")
        self._size -= 1
        node = self.header.succ
        self.header.succ = node.succ
        node.succ.prev = self.header
        node.prev = None
        node.succ = None
        return node
        

if __name__ == "__main__":
    q = Queue()
    q.enque(2)
    q.enque(3)
    q.enque(4)
    q.enque(5)
    q.enque(6)
    q.enque(7)
    print(q)
    q.deque()
    q.deque()
    q.deque()
    q.deque()
    print(q.size())
    print(q)
