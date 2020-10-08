# https://leetcode-cn.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        dpmax[i] = max(dpmax[i-1] * nums[i], dpmin[i-1] * nums[i])
        dpmin[i] = min(dpmin[i-1] * nums[i], dpmax[i-1] * nums[i])
        '''
        dmin, dmax, _max = 1, 1, float('-inf')
        for i in range(len(nums)):
            dmin, dmax = min(dmin * nums[i], dmax * nums[i], nums[i]), max(dmax * nums[i], dmin * nums[i], nums[i])
            _max = max(_max, dmax)
        return _max