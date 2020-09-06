# https://leetcode-cn.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # return collections.Counter(nums).most_common(1)[0][0]
    
        '''摩尔投票法'''
        '''摩尔投票法基于这样的假设：所有非多数元素的投票都会被多数元素的投票给抵消'''
        voter, count = nums[0], 0
        for i in range(len(nums)):
            if nums[i] == voter: count += 1
            elif count == 1:
                voter = nums[i]
            else: count -= 1
        return voter