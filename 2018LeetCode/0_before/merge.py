# -- coding: utf-8 --
# author: una
# datetime: 2019-08-04 16:53
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 两个数组从后往前比较，比如：如果nums[-1] < nums2[-1]，则将nums2[-1]赋值到nums1[m+n-1]。
        # 然后将nums2的下标前移，再比较nums1[-1]和nums[-2]，将较大者赋值到nums1[m+n-2]。
        i = m - 1
        j = n - 1
        p = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[p] = nums2[j]
                j -= 1
            else:
                nums1[p] = nums1[i]
                i -= 1
            p -= 1
        if j >= 0:
            nums1[:j + 1] = nums2[:j + 1]


