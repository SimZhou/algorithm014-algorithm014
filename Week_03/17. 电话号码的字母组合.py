# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        self.table = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []
        def dfs(digits, level, temp):
            if len(temp) == len(digits): 
                res.append(temp)
                return
            for i in self.table[digits[level]]:
                dfs(digits, level+1, temp+i)
        dfs(digits, 0, "")
        return res