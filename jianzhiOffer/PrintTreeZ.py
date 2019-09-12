# -- coding: utf-8--
# author:Jing
# datetime:2019/7/7 10:53
# software: PyCharm


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        res = list()
        s_lr = list()  # 存储顺序：r->l
        s_rl = list()  # 存储顺序：l->r
        s_lr.append(pRoot)
        while len(s_lr) + len(s_rl) > 0:
            while len(s_lr) > 0:
                # 本轮的pop/push顺序为：l->r
                t = s_lr.pop()
                if t.left:
                    s_rl.append(t.left)
                if t.right:
                    s_rl.append(t.right)
                res.append(t.val)

            while len(s_rl) > 0:
                # 本轮的pop/push顺序为：r->l
                t = s_rl.pop()
                if t.right:
                    s_lr.append(t.right)
                if t.left:
                    s_lr.append(t.left)
                res.append(t.val)
        return res


if __name__ == '__main__':
    a = TreeNode(8)
    a.left = TreeNode(6)
    a.right = TreeNode(10)
    a.left.left = TreeNode(5)
    a.left.right = TreeNode(7)
    a.right.left = TreeNode(9)
    a.right.right = TreeNode(11)
    print Solution().Print(a)