# -- coding: utf-8--
# author:Jing
# datetime:2019/7/4 15:59
# software: PyCharm
from Queue import Queue
class Solution:
    # 返回对应char
    def __init__(self):
        self.count = dict()
        self.cur = None

    def FirstAppearingOnce(self):
        # write code here
        if self.cur is None or self.count[self.cur] > 1:
            return '#'
        else:
            return self.cur

    def Insert(self, char):
        # write code here
        cnt = self.count.setdefault(char, 0)
        self.count[char] = cnt + 1
        if self.cur is None or self.count[self.cur] > 1:
            for char, cnt in self.count.items():
                if cnt == 1:
                    self.cur = char
                    break


if __name__ == '__main__':
    a = dict()
    a[''] = 1
    print a