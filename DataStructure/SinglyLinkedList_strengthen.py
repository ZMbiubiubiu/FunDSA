#! /home/bingo/anaconda3/bin/python
# *- coding:utf-8 -*

__author__ = "ZzLee"
__date__ = "2019/04/26"
__mail__ = "zhangmeng.lee@foxmail.com"
"""
    A enhanced Singly linked list
"""

class ListNode:
    """
    a node in Linked list
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    def __repr__(self):
        return repr(self.data)
    
class SinglyLinkedList:
    """
    Create a singly linked-list
    With 'begin' sentinal!
    """
    def __init__(self):
        self.head = None
        self.begin = ListNode(data='begin', next=self.head)
        # self.end = ListNode(data='end')
        
    def __repr__(self):
        """
        return a string representation of the list
        takes O(n)
        """
        nodes = []
        cur = self.head
        while cur:
            nodes.append(repr(cur))
            cur = cur.next
        return '[' + ','.join(nodes) + ']'
    
    def prepend(self, data):
        """
        insert a node at the begining of the list
        """
        self.head = ListNode(data=data, next=self.head)
    def append(self, data):
        """
        inset a node at the end of the list
        """
        cur = self.begin
        while cur.next:
            cur = cur.next
        cur.next = ListNode(data=data)
    
    def find(self, key):
        """
        search for the fisrt node with 'data' matching the 'key'
        return the node or None if not found
        takes O(n) time
        """
        cur = self.head
        while cur and cur.data != key:
            cur = cur.next
        return cur #note that it will be None if not found
    def remove(self, key):
        """
        search for the first node with 'data' matching the 'key'
        remove the node 
        takes o(n) time
        """
        cur = self.begin
        pre = None
        while cur and cur.data != key:
            pre = cur
            cur = cur.next
        else:
            pre.next = cur.next
        
    def reverse(self):
        """
        reverse a list
        takes O(n) time
        """
        cur = self.head
        next_node = None
        pre_node = None
        while cur:
            # for save
            next_node = cur.next
            cur.next = pre_node
            pre_node = cur
            cur = next_node
        self.head = pre_node
            
            