# -- coding: utf-8 --
# author: una
# datetime: 2019-09-10 16:45
from typing import List


def lengthOfLIS_1(nums: List[int]) -> int:
    # n**2
    if not nums:
        return 0
    dp = []
    for i in range(len(nums)):
        dp.append(1)
    for i in range(len(nums)):
        print(dp)
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def lengthOfLIS_2(nums: List[int]) -> int:
    # n * log(n)
    if not nums:
        return 0
    res = []
    for x in nums:
        if not res:
            res.append(x)
        else:
            if x > res[-1]:
                res.append(x)
            else:
                l, h = 0, len(res) - 1
                while l <= h:
                    m = l + (h - l) // 2
                    if res[m] >= x:
                        h = m - 1
                    else:
                        l = m + 1
                res[l] = x
    return len(res)


if __name__ == '__main__':
    nums = [3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]
    print(lengthOfLIS_2(nums))
