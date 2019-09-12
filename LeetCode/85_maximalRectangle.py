# -- coding: utf-8 --
# author: una
# datetime: 2019-08-15 15:55
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        def largestRectangleArea(heights):
            if not heights:
                return 0
            stack = list([-1])
            area = 0
            for i in range(len(heights)):
                if stack[-1] == -1 or heights[stack[-1]] <= heights[i]:
                    stack.append(i)
                else:
                    while stack[-1] > -1 and heights[stack[-1]] > heights[i]:
                        tmp_h = heights[stack.pop()]
                        area = max(area, tmp_h * (i - stack[-1] - 1))
                    stack.append(i)
            i += 1
            while stack[-1] > -1:
                tmp_h = heights[stack.pop()]
                area = max(area, tmp_h * (i - stack[-1] - 1))
            return area

        heights = list(map(int, matrix[0]))
        final_res = largestRectangleArea(heights)
        for i in range(1, len(matrix)):
            heights = [heights[j] + 1 if matrix[i][j] == '1' else 0 for j in range(len(matrix[i]))]
            final_res = max(final_res, largestRectangleArea(heights))
        return final_res


if __name__ == '__main__':
    a = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

    print(Solution().maximalRectangle(a))
