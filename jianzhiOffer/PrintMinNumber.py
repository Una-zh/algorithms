# -- coding: utf-8--
# author:Jing
# datetime:2019/6/17 11:48
# software: PyCharm
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        s = [str(i) for i in numbers]
        s = sorted(s, cmp=lambda a, b: cmp(a+b, b+a))
        return ''.join(s)


if __name__ == '__main__':
    a = [3, 32, 321]
    s = Solution()
    print(s.PrintMinNumber(a))