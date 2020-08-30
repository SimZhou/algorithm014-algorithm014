# https://leetcode-cn.com/problems/permutations/

# 本题是经典的回溯算法问题。
# 回溯问题去重的方法一般是不选取已选择的数据。
# 由于[全排列I](https://leetcode-cn.com/problems/permutations/)的序列中没有重复数字，所以可以直接判断当前元素是否在路径中存在即可。
# 当然，也可以创建visited_index哈希set，将已访问的节点放入其中，这样会更快一点。


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, path, visited):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in nums:
                if i not in visited: 
                    dfs(nums, path + [i], visited.union({i}))
        dfs(nums, [], set())
        return res