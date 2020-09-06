# https://leetcode-cn.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''暴力法，O(n^2)，O(1)'''
        # pass
        '''自顶向下'''
        # @functools.lru_cache(None)
        # def dp(i):
        #     if i == 0: return nums[0]
        #     return max(dp(i-1) + nums[i], nums[i])
        # dpTab = map(dp, range(0, len(nums)))
        # return max(dpTab)
        '''自底向上'''
        # _max, tempMax = float("-inf"), 0
        # for i in nums:
        #     if tempMax + i >= i: 
        #         _max, tempMax = max(tempMax + i, _max), tempMax + i
        #     else: 
        #         _max, tempMax = max(i, _max), i
        # return _max
        '''贪心算法，O(n), O(1)'''
        # i, j, _max, temp = 0, 0, float("-inf"), 0
        # if len(nums) == 1: return nums[0]
        # while j < len(nums):
        #     temp += nums[j]
        #     _max = max(_max, temp)
        #     if temp < 0: 
        #         i, j = j+1, j+1
        #         temp = 0
        #         continue
        #     else:
        #         j += 1
        # return _max