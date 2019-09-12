# -- coding: utf-8--
# author:Jing
# datetime:2019/6/14 11:24
# software: PyCharm

class Solution:
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        l, r = 0, len(nums)
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            # 左半边有序
            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m
                else:
                    l = m + 1
            # 右半边有序
            else:
                if nums[m+1] <= target <= nums[m]:
                    l = m + 1
                else:
                    r = m
        return -1


if __name__ == '__main__':
    # a = [5,1,3]
    # b = 3
    # s = Solution()
    # s.search(a, b)
    print(5 / 2)
    print(5 // 2)