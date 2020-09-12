# https://leetcode-cn.com/problems/subarray-sum-equals-k/

class Solution:
    # def subarraySum(self, nums: List[int], k: int) -> int:
#         '''n^2, 1'''
#         pass
#         '''前缀和'''
#         '''定义preSum[i]为下标为0-i的子数组的和'''
#         '''O(n^2), O(n)'''
#         preSum, _sum = [0] * (len(nums) + 1), 0
#         for i in range(1, len(nums)+1):
#             _sum += nums[i-1]
#             preSum[i] = _sum
#         res = 0
#         for i in range(1, len(nums)+1):  # [j~i]
#             for j in range(0, i):
#                 if preSum[i] - preSum[j] == k: res += 1
#         return res
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''优化前缀和，若以i为结尾的所有子数组中，存在答案，'''
        '''则一定满足：preSum[j] == preSum[i] - k in HashTable'''
        '''注意，需要初始化hashTable[0]为1，因为当 preSum[i] - k = 0 时，nums[i]即为答案'''
        hashTable, _sum, count = {0: 1}, 0, 0
        for i in range(len(nums)):
            _sum += nums[i]
            if _sum - k in hashTable:
                count += hashTable[_sum - k]
            hashTable[_sum] = hashTable.get(_sum, 0) + 1
        return count
            