# -- coding: utf-8--
# author:Jing
# datetime:2019/6/24 10:49
# software: PyCharm
class Solution:
    def StrToInt(self, s):
        # write code here
        res = 0
        base = 1
        signal = 1
        for i in range(len(s)-1, -1, -1):
            if ord('0') <= ord(s[i]) <= ord('9'):
                res += base * (ord(s[i]) - ord('0'))
                base *= 10
            elif i == 0 and (s[i] == '+' or s[i] == '-'):
                signal = 1 if s[i] == '+' else -1
            else:
                return 0
        return res * signal


if __name__ == '__main__':
    # a = '+123'
    # print Solution().StrToInt(a)
    a = '1'
    print a & 0xf