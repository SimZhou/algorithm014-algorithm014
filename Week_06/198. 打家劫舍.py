# https://leetcode-cn.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        '''dp(i) = max(dp(i-2) + nums[i], dp(i-3) + nums[i-1])'''
        '''其实就是 dp(i) = max(dp(i-2) + nums[i], dp(i-1)'''
        # @functools.lru_cache(None)
        # def dp(i):
        #     if i < 0: return 0
        #     if i == 0: return nums[0]
        #     return max(nums[i] + dp(i-2), dp(i-1))
        # return dp(len(nums)-1)
        '''自底向上'''
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
        pre, now = 0, 0
        for i in range(len(nums)):
            pre, now = now, max(pre + nums[i], now)
        return now