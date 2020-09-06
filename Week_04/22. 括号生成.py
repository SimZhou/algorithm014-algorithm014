# https://leetcode-cn.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(n, temp, l, r):
            if len(temp) == 2*n: 
                res.append(temp)
                return
            if l < n: 
                dfs(n, temp+"(", l+1, r)
            if l > r:
                dfs(n, temp+")", l, r+1)
        res = []
        dfs(n, "", 0, 0)
        return res