# https://leetcode-cn.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        book = {}
        for i in range(len(nums)):
            if target - nums[i] in book: return [book[target-nums[i]], i]
            else: book[nums[i]] = i