# reverse_list.py
# Created: 5 10 2019

"""
    递归:翻转单链表
"""

class ListNode:
    """链表节点"""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    def __repr__(self):
        return repr(self.data)
    
class List:
    """单链表"""
    def __init__(self):
        self.head = None
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
    def append(self, data):
        if not self.head:
            self.head = ListNode(data=data)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = ListNode(data = data)
    def extend(self, it):
        node = self.head
        while node.next:
            node = node.next
        tmp = ListNode(it[0])
        node.next = tmp
        for num in it[1:]:
            tmp.next = ListNode(data=num)
            tmp = tmp.next


    def reverse(self):
        """翻转单链表"""
        head = self.head
        # 递归基
        if head == None or head.next == None:
            return head
        # 等价关系式子:
        # (1)要相信reverse_list(head)可以翻转链表
        # (2)找到reverse(head)与reverse(head.next)的关系
        # 递归翻转链表
        self.head = head.next
        new_list = self.reverse()
        node = head.next
        node.next = head
        head.next = None
        self.head = new_list
        # 返回调整之后的链表
        return new_list

if __name__ == "__main__":
    ll = List()
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.extend([12])
    print(ll)
    ll.reverse()
    print(ll)
    
