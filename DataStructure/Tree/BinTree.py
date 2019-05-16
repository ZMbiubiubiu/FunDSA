from BinNode import BinNode

class BinTree:
    def __init__(self):
        self._size = 0
        self._root = None
    
    def size(self):
        """返回二叉树节点个数"""
        return self._size
    def empty(self):
        """判空"""
        return not self._root
    def root(self):
        """树根"""
        pass
    def insertAsRoot(self, data):
        """插入根节点"""
        pass
    def insertAsLC(self, node, data):
        """将e作为node的左孩子(原无)插入"""
        pass
    def insertAsRC(self, node, data):
        """将e作为node的右孩子(原无)插入"""
        pass
    def attachAsLC(self, node, tree):
        """将tree作为node的左子树(原无)插入"""
        pass
    def attachAsRC(self, node, tree):
        """将tree作为node的右子树(原无)插入"""
        pass
    
    # 遍历器
    def travLevel(self, func):
        """子树层次遍历"""
        if self._root:
            self._root.travLevel(func)
    def travPrev(self, func):
        """子树先序遍历"""
        if self._root:
            self._root.travPrev(func)
    def travIn(self, func):
        """子树中序遍历"""
        if self._root:
            self._root.travIn(func)
    def travPost(self, func):
        """子树后序遍历"""
        if self._root:
            self._root.travPost(func)

    # 比较器(需要自行补充)
    # 比较的都是树的根节点
    def __lt__(self, tree):
        return self._root and tree._root and (self._root < tree._root)
    def __eq__(self, tree):
        return self._root and tree._root and (self._root == tree._root)
        

    