# -- coding: utf-8--
# author:Jing
# datetime:2019/7/14 11:15
# software: PyCharm


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.root = None
        self.s = []

    def Serialize(self, root):
        res = []
        if root is None:
            res.append('$')
            return res
        else:
            res.append(root.val)
            res.extend(self.Serialize(root.left))
            res.extend(self.Serialize(root.right))
            return res

    def Deserialize(self, s):
        def doDeserialize():
            # print s
            if len(self.s) == 0 or self.s[0] == '$':
                if self.s[0] == '$':
                    self.s = self.s[1:]
                return None
            else:
                root = TreeNode(self.s[0])
                self.s = self.s[1:]
                root.left = doDeserialize()
                root.right = doDeserialize()
                return root
        self.s = s
        return doDeserialize()


if __name__ == '__main__':
    t = TreeNode(8)
    t1 = TreeNode(6)
    t2 = TreeNode(10)
    t3 = TreeNode(5)
    t4 = TreeNode(7)
    t5 = TreeNode(9)
    t6 = TreeNode(11)
    t.left = t1
    t.right = t2
    t1.left = t3
    t1.right = t4
    t2.left = t5
    t2.right = t6
    s = Solution()
    result = s.Serialize(t)
    print result
    print s.Serialize(s.Deserialize(result))