# https://leetcode-cn.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
#         '''dp(i) = '''
#         if len(nums) == 1: return nums[0]
#         return max(self.robSub(nums[1:]), self.robSub(nums[:-1]))
    
#     def robSub(self, nums):
#         s0, s1 = 0, 0
#         for i in range(len(nums)):
#             if i % 2: s0 = max(s0+nums[i], s1)
#             else: s1 = max(s1+nums[i], s0)
#         return max(s0, s1)

        '''自底向上，优化'''
        if len(nums) == 1: return nums[0]
        pre, now1 = 0, 0
        for i in range(len(nums)-1):
            pre, now1 = now1, max(pre + nums[i], now1)
        pre, now2 = 0, 0
        for i in range(1, len(nums)):
            pre, now2 = now2, max(pre + nums[i], now2)
        return max(now1, now2)