#! /home/bingo/anaconda3/bin/python
# *- coding=utf-8 -*

__author__ = "ZzLee"
__date__ = "2019/04/27"
__mail__ = "zhangmeng.lee@foxmail.com"
__version__ = "1.0"

"""
    参照清华大学邓俊辉老师的<数据结构>, 用python实现
    ps: 会不断补充此结构
"""
# 双向链表加强版之链表节点
class ListNode:
    """
    双向链表的节点
    data: 节点值
    prev: 前驱节点
    succ: 后继杰点
    """
    def __init__(self, data, prev=None, succ=None):
        self.data = data
        self.prev = prev
        self.succ = succ
    def insertAsPrev(self, e):
        # 创建新节点, 并且设置链接
        new_node = ListNode(data=e, prev=self.prev, succ=self)
        self.prev.succ = new_node
        self.prev = new_node
        # 返回新节点
        return new_node
    def insertAsSucc(self, e):
        new_node = ListNode(data=e, prev=self, succ=self.succ)
        self.succ.prev = new_node
        self.succ = new_node
        
    def __repr__(self):
        """
        Use a string to representation the listnode itself
        """
        return repr(self.data)

# 双向链表加强版之链表
class List:
    def __init__(self):
        # 记录规模
        self._size = 0
        # 创建头尾哨兵
        self.header = ListNode(data = "header")
        self.trailer = ListNode(data = "trialer")
        self.header.succ = self.trailer
        self.trailer.prev = self.header
        
    def __repr__(self):
        """
        Use a string to representation this list itself
        O(n)
        """
        nodes = []
        node = self.header.succ
        while node.data != self.trailer.data:
            nodes.append(repr(node))
            node = node.succ
        return '[' + ','.join(nodes) + ']'
        
        
    """ 
    只读访问接口
    """
    def size(self) ->int:
        """
        返回规模
        O(1)
        """
        return self._size
    def empty(self) ->bool:
        """
        判空
        O(1)
        """
        return self._size <= 0
    def first(self) ->ListNode:
        """
        返回首节点
        O(1)
        """
        return self.header.succ
    def last(self) ->ListNode:
        """
        返回末节点
        O(1)
        """
        return self.trailer.prev
    def __getitem__(self, n:int) ->ListNode:
        """
        类似C++的重载运算符'[]'
        O(n)
        """
        node = self.first()
        while n:
            node = node.succ
            n -= 1
        return node
 
    def insertAsFirst(self, e) ->ListNode:
        """
        插入作为首节点 insertAsFirst(self, e:ListNode) ->ListNode
        O(1)
        """
        self._size += 1
        return self.header.insertAsSucc(e)
    def insertAsLast(self, e) ->ListNode:
        """
        插入作为尾节点 insertAsLast(self, e:ListNode) ->ListNode
        O(1)
        """
        self._size += 1
        return self.trailer.insertAsPrev(e)
    def insertA(self, node:ListNode, e) ->ListNode:
        """
        在node节点之后插入一个节点 insertA(self, node:ListNode, e) ->ListNode
        O(1)
        """
        self._size += 1
        return node.insertAsSucc(e)
    def insertB(self, node:ListNode, e) ->ListNode:
        """
        在node节点之前插入一个节点 insertB(self, node:ListNode, e) ->ListNode
        O(1)
        """
        self._size += 1
        return node.insertAsPrev(e)
    
    def find(self, e, n=None, node=None) ->ListNode:
        """
        在无序链表中节点node的n个真前驱, 找到等于data=e的最后者
        O(n)
        """
        # 设置默认值
        if n == None:
            n = self._size
        if node == None:
            node = self.trailer
        # 设置迭代
        cur = node.prev
        while n:
            if cur.data == e:
                return cur
            n -= 1
            cur = cur.prev
        return None
    
    """ 写操作 """
    def remove(self, node:ListNode) :
        """
        删除合法节点 remove(self, node:ListNode)
        """
        data = node.data
        node.prev.succ = node.succ
        node.succ.prev = node.prev
        # 断掉指向
        node.prev = None
        node.succ = None
        # 更新规模
        self._size -= 1
        return data
    def clear(self) ->int:
        """
        清除所有的节点, 返回原有的节点数目
        takes O(n)
        """
        old_size = self._size
        # 反复删除首节点
        while self._size:
            remove(header.succ)
            self._size -= 1
        return old_size
    
    def deduplicate(self) ->int:
        """
        删除链表内部的重复节点, 进行唯一化. 返回删除的节点数
        takes O(n^2) time : 首先需要做n次迭代, 每次迭代中
          有会调用find方法, find操作的时间复杂度正比于查找区间的宽度,即当前节点的秩
        """
        if self._size < 2:
            return 0
        
        old_size = self._size
        # 设置迭代节点
        cur = self.header.succ
        # 真前驱数
        r = 0
        # 设置迭代结束的哨兵
        sentinal = self.trailer.data
        while cur.data != sentinal:
            found = self.find(cur.data, r, cur) # 在当前节点的真前驱中寻找相同节点
            if found:
                self.remove(found)
            else:
                r += 1
            cur = cur.succ
        return old_size - self._size

if __name__ == "__main__":
    l = List()
    l.insertAsFirst(2)
    l.insertAsLast(3)
    l.insertA(l.first(), 33)
    l.insertAsFirst(2)
    l.insertAsFirst(55)
    l.insertAsFirst(55)
    l.insertAsFirst(55)
    print(l)
    l.deduplicate()
    print(l)