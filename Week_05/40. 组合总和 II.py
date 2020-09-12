# https://leetcode-cn.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # 排序后，如何去重？若当前树中，当前值上一次已经选过，则无序再选
        def dfs(temp, _sum, start):
            if _sum > target: return
            if _sum == target: 
                res.append(temp.copy())
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]: continue    # 注意这里的剪枝是i > start，要不然会多剪
                temp.append(candidates[i])
                dfs(temp, _sum + candidates[i], i + 1)
                temp.pop()
        res = []
        dfs([], 0, 0)
        return res