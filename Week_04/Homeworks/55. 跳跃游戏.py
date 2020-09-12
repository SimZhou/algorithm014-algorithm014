# https://leetcode-cn.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''正序贪心，从前往后更新每个点的最远跳跃距离'''
        # maxNow = 0
        # for i in range(len(nums)):
        #     maxNow = max(maxNow, i + nums[i])
        #     if maxNow >= len(nums)-1: return True
        #     if i >= maxNow: return False
        
        '''倒序贪心，从后往前找可达到位置，如果没找到，则不行'''
        cur = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= cur: cur = i
        return cur == 0