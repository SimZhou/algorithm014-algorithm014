# https://leetcode-cn.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''自顶向下'''
        @functools.lru_cache(None)
        def dp(i, j):
            if i < 0: return j + 1
            if j < 0: return i + 1
            if word1[i] == word2[j]: return dp(i-1, j-1)
            else: return min( dp(i-1, j)+1, dp(i, j-1)+1, dp(i-1, j-1)+1 )
        return dp(len(word1)-1, len(word2)-1)
        '''自底向上'''
        # dp = [[0 for _ in range(len(word1)+1)] for __ in range(len(word2)+1)]
        # for i in range(1, len(word1)+1):
        #     dp[0][i] = i
        # for j in range(1, len(word2)+1):
        #     dp[j][0] = j
        # for i in range(1, len(word1)+1):
        #     for j in range(1, len(word2)+1):
        #         if word1[i-1] == word2[j-1]: dp[j][i] = dp[j-1][i-1]
        #         else: dp[j][i] = min(dp[j-1][i]+1, dp[j][i-1]+1, dp[j-1][i-1]+1)
        # return dp[len(word2)][len(word1)]