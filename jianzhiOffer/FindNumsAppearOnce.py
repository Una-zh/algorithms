# -- coding: utf-8--
# author:Jing
# datetime:2019/6/21 12:05
# software: PyCharm
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if array is None or len(array) < 2:
            return
        res = 0
        for i in array:
            res ^= i
        idx = 0
        while (res & 1) == 0:
            idx += 1
            res >>= 1
        a = b = 0
        for i in array:
            if self.isBit(i, idx):
                a ^= i
            else:
                b ^= i
        return [a, b]

    def isBit(self, num, idx):
        num >>= idx
        return num & 1


if __name__ == '__main__':
    a = [1, 2, 3, 4, 8, 3, 1, 4]
    s = Solution()
    print(s.FindNumsAppearOnce(a))