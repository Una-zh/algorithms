# -- coding: utf-8--
# author:Jing
# datetime:2019/6/22 17:05
# software: PyCharm
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n == 0:
            return
        circle = list(range(0, n))
        number = 0
        cnt = 0
        while len(circle) > 1:
            if cnt == m - 1:
                circle.remove(circle[number])
            cnt += 1
            if cnt == m:
                cnt = 0
            number += 1
            if number == len(circle):
                number = 0
        return circle[0]


if __name__ == '__main__':
    n = 5
    m = 3
    s = Solution()
    print s.LastRemaining_Solution(n, m)