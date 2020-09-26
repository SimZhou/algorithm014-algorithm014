# https://leetcode-cn.com/problems/search-a-2d-matrix-ii/

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        x, y = len(matrix)-1, 0
        while x >= 0 and y <= len(matrix[0])-1:
            if matrix[x][y] == target: return True
            elif matrix[x][y] > target: x -= 1
            elif matrix[x][y] < target: y += 1
        return False