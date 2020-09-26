# https://leetcode-cn.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        dpmax[i] = max(dpmax[i-1] * nums[i], dpmin[i-1] * nums[i])
        dpmin[i] = min(dpmin[i-1] * nums[i], dpmax[i-1] * nums[i])
        '''
        dpmax = 1
        dpmin = 1
        _max = float('-inf')
        for i in range(len(nums)):
            dpmax, dpmin = max(dpmax * nums[i], dpmin * nums[i], nums[i]), min(dpmin * nums[i], dpmax * nums[i], nums[i])
            _max = max(_max, dpmax)
        return _max
        
        '''一定包含首尾中的一个'''
        # nums_ = nums[::-1]
        # for i in range(1, len(nums)):
        #     nums[i] = (nums[i-1] or 1) * nums[i]
        #     nums_[i] = (nums_[i-1] or 1) * nums_[i]
        # return max(nums+nums_)