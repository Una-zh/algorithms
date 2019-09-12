# -- coding: utf-8--
# author:Jing
# datetime:2019/6/21 17:26
# software: PyCharm
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if len(array) < 2:
            return
        mult = None
        res = list()
        l, r = 0, len(array) - 1
        while l < r:
            s = array[l] + array[r]
            if s == tsum:
                tmp = array[l] * array[r]
                if mult is None or mult > tmp:
                    mult = tmp
                    res = [array[l], array[r]]
                r -= 1
            elif s > tsum:
                r -= 1
            else:
                l += 1
        return res


if __name__ == '__main__':
    a = [0, 1, 1, 2, 3, 4, 5, 6, 7, 9]
    s = Solution()
    print s.FindNumbersWithSum(a, 9)