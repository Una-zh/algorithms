# -- coding: utf-8 --
# author: una
# datetime: 2019-08-03 11:21


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre:
            return None
        root = TreeNode(pre[0])
        for i in range(len(tin)):
            if tin[i] == root.val:
                break
        root.left = self.reConstructBinaryTree(pre[1: i + 1], tin[:i])
        root.right = self.reConstructBinaryTree(pre[i + 1:], tin[i + 1:])
        return root


if __name__ == '__main__':
    pre = [1, 2, 3, 4, 5, 6, 7]
    tin = [3, 2, 4, 1, 6, 5, 7]
    root = Solution().reConstructBinaryTree(pre, tin)

    def levelOrder(root):
        if root is None:
            return
        myQueue = []
        myQueue.append(root)
        while myQueue:
            node = myQueue.pop(0)
            print(node.val, end=' ')
            if node.left:
                myQueue.append(node.left)
            if node.right:
                myQueue.append(node.right)

    levelOrder(root)