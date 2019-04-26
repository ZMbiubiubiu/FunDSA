#! /home/bingo/anaconda3/bin/python
# *- coding:utf-8 -*

__author__ = "ZzLee"
__date__ = "2019/04/26"
__mail__ = "zhangmeng.lee@foxmail.com"
"""
    A simple Doubly linked list
"""

class ListNode:
    """
    a double linked listnode
    """
    def __init__(self, data=None, pre=None, next=None):
        self.data = data
        self.pre = pre
        self.next = next
    def __repr__(self):
        return repr(self.data)
    
class DoublyLinkedList:
    """
    Create a doubly linked-list
    """
    def __init__(self):
        self.head = None
    def __repr__(self):
        """
        Return a string representation of the list
        """
        nodes = []
        cur = self.head
        while cur:
            nodes.append(repr(cur))
            cur = cur.next
        return '[' + ','.join(nodes) + ']'
    
    def prepend(self, data):
        """
        Insert a node at the begin of the list
        Takes O(1) time
        """
        new_head = ListNode(data=data, next=self.head)
        if self.head:
            self.head.pre = new_head
        self.head = new_head
    
    def append(self, data):
        """
        Insert a node at the end of the list
        Takes O(n) time
        """
        if not self.head:
            self.prepend(data)
        cur = self.head
        while cur.next:
            cur = cur.next
        new_tail = ListNode(data=data, pre=cur)
        cur.next = new_tail
        
    def find(self, key):
        """
        Search for the first node with 'data' matching 'key'
        Return the node or None if not found
        Takes O(n) time
        """
        cur = self.head
        while cur and cur.data != key:
            cur = cur.next
        return cur # Will be None if not found
    
    def remove_node(self, node:ListNode):
        """
        Unlink an node from the list.
        Takes O(1) time.
        """
        if node.pre:
            node.pre.next = node.next
        if node.next:
            node.next.pre = node.pre
        if node is self.head:
            self.head = node.next
        node.prev = None
        node.next = None
        
    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        node = self.find(key)
        if not node:
            return
        self.remove_node(node)

    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        cur = self.head
        pre_node = None
        while cur:
            # for save
            pre_node = cur.pre
            # exchange the pointer
            cur.pre = cur.next
            cur.next = pre_node
            # forward
            cur = cur.pre
        self.head = pre_node.pre