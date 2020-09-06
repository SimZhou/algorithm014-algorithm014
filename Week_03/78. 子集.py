# https://leetcode-cn.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # def dfs(nums, k, path, start):
        #     if len(path) == k: 
        #         res.append(path.copy())
        #         return
        #     for i in range(start, len(nums)):
        #         dfs(nums, k, path + [nums[i]], i + 1)
        # for k in range(len(nums) + 1):
        #     dfs(nums, k, [], 0)
        # return res
        '''一遍回溯'''
        # res = []
        # def dfs(nums, path, start):
        #     res.append(path.copy())
        #     for i in range(start, len(nums)):
        #         dfs(nums, path + [nums[i]], i+1)
        # dfs(nums, [], 0)
        # return res
        '''枚举'''
        # res = [[]]     # 空集的自己就是它本身
        # for i in nums:
        #     for j in range(len(res)):
        #         res.append(res[j]+[i])
        # return res
        '''位'''
        res = []
        for c in range(2**len(nums)):
            temp, i = [], 0
            while c:
                if c & 1: temp.append(nums[i])
                c, i = c >> 1, i + 1
            res.append(temp)
        return res