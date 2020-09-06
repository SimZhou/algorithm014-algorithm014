# https://leetcode-cn.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # return collections.Counter(nums).most_common(1)[0][0]
    
        '''摩尔投票法'''
        init, count = nums[0], 0
        for i in range(len(nums)):
            if init == nums[i]:
                count += 1
            elif count == 1:
                init = nums[i]
            else:
                count -= 1
        return init