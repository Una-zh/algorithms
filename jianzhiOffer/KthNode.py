# -- coding: utf-8--
# author:Jing
# datetime:2019/7/15 9:36
# software: PyCharm


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if pRoot is None:
            return
        s = []
        node = pRoot
        idx = 0
        while node or s:
            while node:
                s.append(node)
                node = node.left
            node = s.pop()
            idx += 1
            if idx >= k:
                break
            node = node.right
        return node if idx == k else None


if __name__ == '__main__':
    a = [1]
    for i in range(len(a), 0, -1):
        print 'hello'