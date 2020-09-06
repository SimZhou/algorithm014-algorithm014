# https://leetcode-cn.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxNow = 0
        for i in range(len(nums)):
            maxNow = max(maxNow, i + nums[i])
            if i == len(nums) - 1: return True
            if i > maxNow or i == maxNow and not nums[i]: return False
        return True