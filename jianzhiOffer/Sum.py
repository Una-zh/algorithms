# -- coding: utf-8--
# author:Jing
# datetime:2019/6/22 17:18
# software: PyCharm
class Solution:
    def Sum_Solution(self, n):
        # write code here
        res = n
        tmp = res and self.Sum_Solution(n-1)
        res += tmp
        return res