# -- coding: utf-8--
# author:Jing
# datetime:2019/6/18 10:58
# software: PyCharm
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        n = len(data)
        if n == 1:
            return n if data[0] == k else 0
        l, r = 0, n - 1
        start = n - 1
        end = 0
        while l <= r:
            m = l + ((r - l) >> 1)
            if k == data[m]:
                start = m
            if k < data[m]:
                r = m - 1
            else:
                l = m + 1
        l, r = 0, n - 1
        while l <= r:
            m = l + ((r - l) >> 1)
            if k == data[m]:
                end = m
            if k > data[m]:
                l = m + 1
            else:
                r = m - 1
        return max(end - start + 1, 0)


if __name__ == '__main__':
    a = [1,2,3,3,3,3,4,5]
    s = Solution()
    print(s.GetNumberOfK(a, 3))