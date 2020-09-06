# https://leetcode-cn.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        m = [i for l in matrix for i in l]
        l, r = 0, len(m)-1
        while l < r:
            mid = (l+r)//2
            if m[mid] == target: return True
            if m[mid] < target:
                l = mid + 1
            elif m[mid] > target:
                r = mid - 1
        return m[l] == target