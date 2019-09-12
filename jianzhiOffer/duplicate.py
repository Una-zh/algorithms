# -- coding: utf-8--
# author:Jing
# datetime:2019/6/26 10:06
# software: PyCharm
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if numbers is None:
            return False
        s = dict()
        length = len(numbers)
        for i in numbers:
            if i < 0 or i >= length:
                return False
            s[i] = s.setdefault(i, 0) + 1
            if s[i] == 2:
                duplication.append(i)
        return True if len(duplication) > 0 else False


if __name__ == '__main__':
    a = [2,1,3,1,4]
    d = []
    print Solution().duplicate(a, d)
    print d[0]