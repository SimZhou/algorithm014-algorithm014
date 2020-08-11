# https://leetcode-cn.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        双指针：O(n)
        关键：为什么对应的数字较小的那个指针不可能再作为容器的边界了？
             因为不论如何移动大的那个指针，都不再可能比原先的面积更大了
        '''
        maxA = 0
        i, j = 0, len(height)-1
        while i < j:
            area = (j - i) * min(height[i], height[j])
            if area > maxA: maxA = area
            if height[i] <= height[j]: i += 1
            else: j -= 1
        return maxA
    
    # def maxArea(self, height: List[int]) -> int:
    #     '''
    #     暴力法：O(n**2)
    #     -超时
    #     '''
    #     maxA = 0
    #     for i in range(len(height)-1):
    #         for j in range(i, len(height)):
    #             area = (j - i) * min(height[i], height[j])
    #             if area > maxA: maxA = area
    #     return maxA