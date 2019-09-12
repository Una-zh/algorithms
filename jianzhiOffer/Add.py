# -- coding: utf-8--
# author:Jing
# datetime:2019/6/24 9:26
# software: PyCharm
class Solution:
    def Add(self, num1, num2):
        # write code here
        s, c = 0, 0
        while num2 != 0:
            s = num1 ^ num2
            c = (num1 & num2) << 1
            num1, num2 = s, c
        return num1


if __name__ == '__main__':
    print 0xFFFFFFFF