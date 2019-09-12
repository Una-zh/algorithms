# -- coding: utf-8 --
# author: una
# datetime: 2019-08-04 16:52


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
        # 多维list数组不可以用ndarray的切片方式，必须使用for循环对每一行进行切片
        return self.searchMatrix([matrix[j][:i] for j in range(1, len(matrix))], target)
