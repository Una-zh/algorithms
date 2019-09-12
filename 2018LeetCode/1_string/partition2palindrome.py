# -- coding: utf-8 --
# author: una
# datetime: 2019-08-19 10:03
from typing import List
import re


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = list()

        def isPalindrome(s: str) -> bool:
            if s is None:
                return False
            if len(s) <= 1:
                return True
            # 提取所有数字和字母，并将所有字母统一为小写
            s = re.findall(r'[0-9a-zA-Z]', s)
            s = ''.join(s)
            s = s.lower().replace(' ', '')
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def dfs(tmp_res, remain_s):
            if len(remain_s) == len(s):
                tmp_res = []
            if not remain_s:
                res.append(tmp_res)
                return
            for i in range(len(remain_s)):
                if isPalindrome(remain_s[: i + 1]):
                    dfs(tmp_res[:] + [remain_s[: i + 1]], remain_s[i+1:])

        dfs([], s)
        return res


if __name__ == '__main__':
    s = "aab"
    print(Solution().partition(s))

