# -- coding: utf-8 --
# author: una
# datetime: 2019-08-02 23:21


class Solution:
    def firstMissingPositive(self, nums: list) -> int:
        # 缺失的最小整数的范围：1 ~ N+1
        N = len(nums)
        i = 0
        while i < N:
            if nums[i] == 1:
                break
            else:
                i += 1
        if i == N:
            return 1
        else:
            nums += [1, 1]
            for i in range(N):
                if nums[i] <= 0:
                    nums[i] = 1
            for i in range(N):
                if abs(nums[i]) < N+2:
                    nums[abs(nums[i])] *= -1
            for i in range(1, N+2):
                if nums[i] > 0:
                    return i


if __name__ == '__main__':
    nums = [1, 1000]
    print(Solution().firstMissingPositive(nums))