# -- coding: utf-8--
# author:Jing
# datetime:2019/6/26 16:59
# software: PyCharm
# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if len(s) == 0:
            if len(pattern) == 0:
                return True
            elif len(pattern) == 2 and pattern[1] == '*':
                return True
            else:
                return False
        else:
            if len(pattern) > 0:
                cur_match = pattern[0] in {s[0], '.'}
                if len(pattern) > 1 and pattern[1] == '*':
                    return self.match(s, pattern[2:]) or (cur_match and self.match(s[1:], pattern))
                else:
                    return cur_match and self.match(s[1:], pattern[1:])
            else:
                return False


if __name__ == '__main__':
    s = 'aaa'
    p = 'ab*a'
    print Solution().match(s, p)