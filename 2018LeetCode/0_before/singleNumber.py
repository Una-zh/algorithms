# -- coding: utf-8 --
# author: una
# datetime: 2019-08-04 16:45
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
         异或运算
         1. x ^ x = 0
         2. x ^ 0 = x
         3. x ^ y = y ^ x
        """
        res = 0
        for i in nums:
            res ^= i
        return res
