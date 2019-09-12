# -- coding: utf-8--
# author:Jing
# datetime:2019/6/16 23:13
# software: PyCharm


def heap_adjust(nums, l, r):
    while l <= r // 2:
        t = 2 * l
        if t < r and nums[t + 1] < nums[t]:
            t += 1
        if nums[l] <= nums[t]:
            break
        nums[t], nums[l] = nums[l], nums[t]
        l = t


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        n = len(tinput)
        if n < k:
            return []
        nums = [0] + tinput
        res = []
        for i in range(n // 2, 0, -1):
            heap_adjust(nums, i, n)
        for i in range(n, n - k, -1):
            nums[i], nums[1] = nums[1], nums[i]
            res.append(nums[i])
            heap_adjust(nums, 1, i - 1)
        return res


if __name__ == '__main__':
    a = [4,5,1,6,2,7,3,8]
    s = Solution()
    print(s.GetLeastNumbers_Solution(a, 4))