# -- coding: utf-8--
# author:Jing
# datetime:2019/6/13 15:52
# software: PyCharm


class Solution:
    def strStr(self, haystack, needle):
        l2 = len(needle)
        if l2 == 0:
            return 0
        l1 = len(haystack)
        if l1 == 0 or l1 > l2:
            return -1
        i = 0
        while i + l2 <= l1:
            while i < l1 and haystack[i] != needle[0]:
                i += 1
            if l1 - i >= l2:
                p, q = i, 0
                while q < l2 and haystack[p] == needle[q]:
                    p += 1
                    q += 1
                if q == l2:
                    return i
                else:
                    i += 1
        return -1


if __name__ == '__main__':
    s = 'hello'
    n = 'll'
    sol = Solution()
    sol.strStr(s, n)
