# -- coding: utf-8--
# author:Jing
# datetime:2019/6/11 11:54
# software: PyCharm


class Solution:
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        nums.sort()
        if nums[0] > target:
            return []
        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    tmp = nums[i] + nums[j] + nums[l] + nums[r]
                    if tmp < target:
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        l += 1
                    elif tmp > target:
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        r -= 1
        return res


if __name__ == '__main__':
    a = [1, -2, -5, -4, -3, 3, 3, 5]
    t = -11
    sol = Solution()
    print(sol.fourSum(a, t))