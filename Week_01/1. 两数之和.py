# https://leetcode-cn.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Intuition理解：
        每个人进入会场后，查表看自己对象是否在会场中，如果不在，则把自己登记上去
        '''
        hashTable = {}
        for i in range(len(nums)):
            if target - nums[i] in hashTable:
                return [i, hashTable.get(target-nums[i])]
            else:
                hashTable[nums[i]] = i
        return []