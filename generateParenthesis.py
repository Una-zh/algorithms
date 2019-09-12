# -- coding: utf-8--
# author:Jing
# datetime:2019/6/12 10:59
# software: PyCharm


class Solution:
    def generateParenthesis(self, n):
        if n == 0:
            return []
        old = set()
        cnt = 0
        s = ''
        while cnt < n * 2:
            new = set()
            if len(old) == 0:
                new.add(s + '(')
            for s in old:
                l = s.count('(')
                r = s.count(')')
                if l < n:
                    if l == r:
                        new.add(s + '(')
                    else:
                        new.add(s + '(')
                        new.add(s + ')')
                else:
                    new.add(s + ')')
            cnt += 1
            old = new
        return list(old)


if __name__ == '__main__':
    n = 3
    sol = Solution()
    sol.generateParenthesis(n)