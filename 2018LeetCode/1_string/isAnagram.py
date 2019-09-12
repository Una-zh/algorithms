# -- coding: utf-8 --
# author: una
# datetime: 2019-09-01 10:25
from collections import defaultdict


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_s = defaultdict(int)
        char_t = defaultdict(int)
        for c in s:
            char_s[c] += 1
        for c in t:
            char_t[c] += 1
        if len(char_s) != len(char_t):
            return False
        for c in char_s.keys():
            if c not in char_t.keys() or char_s[c] != char_t[c]:
                return False
        return True


if __name__ == '__main__':
    s = "a"
    t = "ab"
    print(Solution().isAnagram(s, t))