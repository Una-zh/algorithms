# -- coding: utf-8 --
# author: una
# datetime: 2019-08-04 17:32
from typing import List


def quick_sort(nums: List[int], start: int, end: int) -> None:
    if start >= end:
        return
    p = partition(nums, start, end)
    quick_sort(nums, start, p-1)
    quick_sort(nums, p+1, end)


def partition(nums: List[int], start: int, end: int) -> int:
    p = nums[start]
    i, j = start, end
    while i < j:
        while i < j and nums[j] > p:
            j -= 1
        nums[i] = nums[j]
        while i < j and nums[i] <= p:
            i += 1
        nums[j] = nums[i]
    nums[i] = p
    return i


if __name__ == '__main__':
    a = [3, 1, 4, 9, 6]
    quick_sort(a, 0, len(a)-1)
    print(a)