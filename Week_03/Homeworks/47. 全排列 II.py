# https://leetcode-cn.com/problems/permutations-ii/

# 全排列I的进阶版，全排列II
# 由于结果中可包含重复数字，但又需要返回不重复的全排列，所以这里的去重就比较tricky了。
# 这里不光要去重已选择的元素，还需要去重已选择的路径，所以能够想到一个利用预排序，然后首次选择中不选择重复元素的方法（参考三数之和，四数之和）。（直接忽略暴力判断法）


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(nums, path, visited):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and i-1 not in visited: continue  # i-1 not in visited, 这句非常重要
                if i not in visited: 
                    backtrack(nums, path + [nums[i]], visited.union({i}))
        backtrack(nums, [], set())
        return res