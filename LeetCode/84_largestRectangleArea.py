# -- coding: utf-8 --
# author: una
# datetime: 2019-08-15 11:23
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def divideConquer(heights, left, right):
            if left > right:
                return 0
            if left == right:
                return heights[left]
            center = left
            for i in range(left, right + 1):
                if heights[i] < heights[center]:
                    center = i
            center_Area = (right - left + 1) * heights[center]
            left_Area = divideConquer(heights, left, center - 1)
            right_Area = divideConquer(heights, center + 1, right)
            return max(center_Area, left_Area, right_Area)

        return divideConquer(heights, 0, len(heights) - 1)


class Solution_2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 单调递增栈
        stack = list([-1])
        # 答案
        res = 0
        for i in range(len(heights)):
            if stack[-1] == -1 or heights[stack[-1]] <= heights[i]:
                stack.append(i)
            else:
                while stack[-1] > -1 and heights[stack[-1]] > heights[i]:
                    tmp_h = heights[stack.pop()]
                    res = max(res, tmp_h * (i-stack[-1]-1))
                stack.append(i)
        i += 1
        while stack[-1] > -1:
            tmp_h = heights[stack.pop()]
            res = max(res, tmp_h * (i-stack[-1]-1))
        return res


if __name__ == '__main__':
    heights = [2,1,5,6,2,3]
    print(Solution_2().largestRectangleArea(heights))
