# -- coding: utf-8 --
# author: una
# datetime: 2019-08-04 16:51
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        res = None
        for i in nums:
            if cnt == 0:
                res = i
                cnt += 1
            else:
                if res == i:
                    cnt += 1
                else:
                    cnt -= 1
        return res
