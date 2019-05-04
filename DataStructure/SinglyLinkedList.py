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
    create a singly linked-list
    """
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
    
    def prepend(self, data):
        """
        insert a node at the begining of the list
        """
        self.head = ListNode(data=data, next=self.head)
    def append(self, data):
        """
        inset a node at the end of the list
        """
        if not self.head:
            self.head = ListNode(data=data)
        cur = self.head
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
        Note: this approch has a bug! When list is empty
        takes o(n) time
        """
        cur = self.head
        pre = None
        while cur and cur.data != key:
            pre = cur
            cur = cur.next

        # if self.head.data == key
        if not pre:
            self.head = cur.next
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
            # rebuild a link
            cur.next = pre_node
            # just forward
            pre_node = cur
            cur = next_node
        # notice the return
        self.head = pre_node
            