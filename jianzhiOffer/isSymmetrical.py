# -- coding: utf-8--
# author:Jing
# datetime:2019/7/5 15:44
# software: PyCharm
from Queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        q1 = Queue()
        q2 = Queue()
        self.pre(pRoot, q1)
        self.post(pRoot, q2)
        while not q1.empty():
            print q1.get()
        print '============='
        while not q2.empty():
            print q2.get()
        while (not q1.empty()) and (not q2.empty()):
            if q1.get() != q2.get():
                return False
        return True

    def pre(self, root, q):
        # left -> root -> right
        if root is None:
            return
        if root.left is None:
            q.put('#')
        self.pre(root.left, q)
        q.put(root.val)
        if root.right is None:
            q.put('$')
        self.pre(root.right, q)

    def post(self, root, q):
        # right -> root -> left
        if root is None:
            return
        if root.right is None:
            q.put('#')
        self.post(root.right, q)
        q.put(root.val)
        if root.left is None:
            q.put('$')
        self.post(root.left, q)


if __name__ == '__main__':
    root = TreeNode(8)
    root.left = TreeNode(6)
    root.right = TreeNode(6)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(5)
    print Solution().isSymmetrical(root)