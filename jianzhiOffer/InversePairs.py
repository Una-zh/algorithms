# -- coding: utf-8--
# author:Jing
# datetime:2019/6/17 20:13
# software: PyCharm
class Solution:
    def InversePairs(self, data):
        # write code here
        n = len(data)
        if n <= 0:
            return 0
        copy = data[:]
        return self.core(data, copy, 0, n - 1)

    def core(self, data, copy, start, end):
        if start == end:
            return 0
        m = start + (end - start) >> 1
        left = self.core(data, copy, start, m)
        right = self.core(data, copy, m + 1, end)
        cnt = 0
        i = m
        j = end
        k = end
        while i >= start and j >= m + 1:
            if data[i] > data[j]:
                copy[k] = data[i]
                cnt += j - m
                i -= 1
            else:
                copy[k] = data[j]
                j -= 1
            k -= 1
        while i >= start:
            copy[k] = data[i]
            i -= 1
            k -= 1
        while j >= m + 1:
            copy[k] = data[j]
            j -= 1
            k -= 1
        for i in range(start, end+1):
            data[i] = copy[i]
        return (left + right + cnt) % 1000000007


if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,0]
    s = Solution()
    s.InversePairs(a)