# -- coding: utf-8 --
# author: una
# datetime: 2019-08-04 11:26


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not len(matrix) or not len(matrix[0]):
            return False
        i = 0
        while i < len(matrix[0]):
            if matrix[0][i] == target:
                return True
            if target < matrix[0][i]:
                break
            i += 1
        return self.searchMatrix(matrix[1:][:i], target)


if __name__ == '__main__':
    a = [[1], [3], [5]]
    b = 5
    print(Solution().searchMatrix(a, b))