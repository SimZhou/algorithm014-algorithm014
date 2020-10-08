# https://leetcode-cn.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        '''dp[i] = max(dp[i-1], dp[i-2]+nums[i])'''
        '''自顶向下'''
        # @functools.lru_cache(None)
        # def dp(i):
        #     if i < 0: return 0
        #     return max(dp(i-1), dp(i-2) + nums[i])
        # return dp(len(nums)-1)
        '''自底向上'''
        if nums == []: return 0
        if len(nums) == 1: return nums[0]
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[len(nums)-1]
        '''自底向上2'''
        '''
          [1, 2, 3, 1]
        0  1  2  4  4
        '''
        # s0, s1 = 0, 0
        # for i in range(len(nums)):
        #     if i % 2 == 0: 
        #         s0 = max(nums[i] + s0, s1)
        #     else:
        #         s1 = max(nums[i] + s1, s0)
        # return max(s1, s0)
        '''自底向上，优化'''
        '''
        prev  now  max(prev+nums[i], now)
              prev        now
        '''
        # pre, now = 0, 0
        # for i in range(len(nums)):
        #     pre, now = now, max(pre + nums[i], now)
        # return now