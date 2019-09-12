# -- coding: utf-8--
# author:Jing
# datetime:2019/6/21 16:33
# software: PyCharm
import math
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = list()
        mark = set()
        _max = tsum // 2 + 1
        for r in range(1, _max + 1):
            delta = 1 - 4 * (2 * tsum - r ** 2 - r)
            if delta >= 0 and (1 + math.sqrt(delta)) / 2 in mark:
                res.append(list(range(int((1 + math.sqrt(delta)) / 2), r + 1)))
            mark.add(r)
        return res


if __name__ == '__main__':
    s = Solution()
    print s.FindContinuousSequence(100)