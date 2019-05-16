# 二叉树节点类定义
from collections import deque

RB_RED = 0
RB_BLACK = 1
class BinNode:
    def __init__(self, data=None, parent=None, lc=None, rc=None, height=0, npl=1, color=RB_RED):
        """初始化"""
        self.data = data
        self.parent = parent
        self.lc = lc
        self.rc = rc
        self.height = height  # 高度
        self.npl = npl        # 左式堆
        self.color = color    # 红黑树

    def size(self):
        """统计当前节点后代总数"""
        pass

    def insertAsLC(self, data):
        """
            作为当前节点的左孩子插入新节点
        """
        self.lc = BinNode(data, parent=self)
        return self.lc

    def insertAsRC(self, data):
        """
            作为当前节点的右孩子插入新节点
        """
        self.rc = BinNode(data=data, parent=self)
        return self.rc

    def succ(self):
        """
            取当前节点的直接后继
        """
        pass

    # 遍历器
    def travLevel(self, func):
        """子树层次遍历"""
        queue = deque() # 辅助队列
        queue.append(self)
        while queue:
            cur = queue.popleft()
            func(cur.data)
            if cur.lc: # 如果有左孩子,那么入队
                queue.append(cur.lc)
            if cur.rc: # 如果有右孩子,那么入队
                queue.append(cur.rc)
    
    # 先序遍历
    def travPrev_R(self, node, func):
        """子树先序遍历,递归版"""
        if not node:
            return ;
        func(node.data)
        self.travPrev_R(node.lc, func)
        self.travPrev_R(node.rc, func)
    def travPrev_I1(self, node, func):
        """先序遍历,迭代版1"""
        stack = [] # 辅助栈
        if node:
            stack.append(node)
        while stack: # 当栈不为空时
            cur = stack.pop()
            func(cur.data)
            if cur.rc:   # 右孩子先入后出
                stack.append(cur.rc)
            if cur.lc:
                stack.append(cur.lc)  # 左孩子后入先出
    
    @staticmethod
    def visitAlongLeftBranch(node, func, stack,):
        """沿左侧通路自顶而下访问沿途节点"""
        while node:
            func(node.data)  # 访问当前节点
            if node.rc:
                stack.append(node.rc) # 当前节点右子树入栈
            node = node.lc   # 眼左侧分支深入一层
    def travPrev_I2(self, node, func):
        """
            先序遍历, 迭代版2
            先沿着左侧通路自顶而下访问沿途节点, 再自底而上依次遍历这些节点的右子树
            相比迭代版1, 省了所有的lChild的 push pop
        """
        stack = [] # 辅助栈,存储节点右子树
        while 1:
            self.visitAlongLeftBranch(node, func, stack)
            if not stack:
                break # 栈为空,说明遍历完毕,退出
            node = stack.pop() # 否则弹出栈顶元素
            
        
    # 中序遍历
    def travIn_R(self, node, func):
        """子树中序遍历,递归版"""
        if not node:
            return ;
        self.travIn_R(node.lc, func)
        func(node.data)
        self.travIn_R(node.rc, func)
        
    @staticmethod
    def goAlongLeftBranch(node, stack):
        while node:
            stack.append(node)
            node = node.lc
    def travIn_I(self, node, func):
        """中序遍历,迭代版"""
        stack = [] # 辅助栈,保存所有左侧链上的所有节点
        while 1:
            self.goAlongLeftBranch(node, stack) # 从当前节点出发,逐批入栈
            if not stack:
                return ; # 直到所有节点访问完毕
            cur = stack.pop() # 弹出栈顶节点并访问之
            func(cur.data)
            node = cur.rc # 转向右子树
        
    def travPost_R(self, node, func):
        """子树后序遍历,递归版"""
        if not node:
            return ;
        self.travPost_R(node.lc, func)
        self.travPost_R(node.rc, func)
        func(node.data)
    # 比较器
    def __lt__(self, node):
        """小于"""
        return self.data < node.data 
    def __eq__(self, node):
        """等于"""
        return self.data == node.data
if __name__ == "__main__":

    a = BinNode(data='a')
    b = a.insertAsLC(data='b')
    c = a.insertAsRC(data='c')
    d = c.insertAsLC(data='d')
    f = c.insertAsRC(data='f')
    e = d.insertAsRC(data='e')
    g = f.insertAsLC(data='g')

    # 先序遍历
    print("先序遍历")
    a.travPrev_R(a, print)
    a.travPrev_I1(a, print)
    a.travPrev_I2(a, print)
    # 中序遍历
    print("后序遍历")
    a.travIn_R(a, print)
    a.travIn_I(a, print)
    # 层次遍历
    print("层次遍历")
    a.travLevel(print)