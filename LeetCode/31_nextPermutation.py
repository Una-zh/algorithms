# -- coding: utf-8--
# author: Jing
# datetime:2019/6/13 19:30
# software: PyCharm


class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = length - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
        else:
            nums[i-1], nums[i] = nums[i], nums[i-1]
            nums = nums[:i] + nums[i:].sort()


if __name__ == '__main__':
    a = [1, 2, 3]
    sol = Solution()
    sol.nextPermutation(a)
    print(a)