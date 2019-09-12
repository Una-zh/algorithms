# -- coding: utf-8 --
# author: una
# datetime: 2019-08-19 09:28
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
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


"""
示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true

示例 2:
输入: "race a car"
输出: false
"""