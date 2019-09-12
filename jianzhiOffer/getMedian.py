# -- coding: utf-8--
# author:Jing
# datetime:2019/7/15 10:48
# software: PyCharm


class Solution:
    def __init__(self):
        self.nums = []

    def Insert(self, num):
        self.nums.append(num)
        if len(self.nums) < 2:
            return
        for i in range(len(self.nums)-1, 0, -1):
            if self.nums[i] < self.nums[i - 1]:
                self.nums[i], self.nums[i - 1] = self.nums[i - 1], self.nums[i]
            else:
                break

    def GetMedian(self):
        length = len(self.nums)
        return self.nums[length // 2] / 1.0 if length % 2 == 1 \
            else (self.nums[length // 2] + self.nums[length // 2 - 1]) / 2.0


if __name__ == '__main__':
    nums = [5,2,3,4,1,6,7,0,8]
    s = Solution()
    for i in range(len(nums)):
        s.Insert(nums[i])
        print s.GetMedian()