# https://leetcode-cn.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''
        由于组合的性质，选完一个数后，只需要选其后面的数即可
        '''
        res = []
        def dfs(n, k, temp, start):
            if len(temp) == k:
                res.append(temp)
                return
            
            for i in range(start, n):
                dfs(n, k, temp+[i+1], i+1)
        dfs(n, k, [], 0)
        return res