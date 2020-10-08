# https://leetcode-cn.com/problems/generate-parentheses/

class Solution:
    @functools.lru_cache(None)
    def generateParenthesis(self, n: int) -> List[str]:
        '''DP，自底向上'''
        # pass
        
        '''DP，自顶向下'''
        '''
        n = 1: () --- (0)0
        n = 2: (()), ()() --- (1)0 + (0)1
        n = 3: ((())), (()()); (())(); ()(()), ()()() --- (2)0 + (1)1 + (0)2
        n = n: --- (n-1)0 + (n-2)1 + ... + (0)n-1
        '''
        if n == 0: return [""]
        if n == 1: return ["()"]
        res = []
        for i in range(n):
            for p in self.generateParenthesis(i):
                for q in self.generateParenthesis(n-1-i):
                    res.append("("+p+")"+q)
        return res
        
        '''DFS'''
        # def dfs(temp, l, r):
        #     if len(temp) == 2*n: 
        #         res.append(temp)
        #         return
        #     if l < n: dfs(temp+"(", l+1, r)
        #     if r < l: dfs(temp+")", l, r+1)
        # res = []
        # dfs("", 0, 0)
        # return res