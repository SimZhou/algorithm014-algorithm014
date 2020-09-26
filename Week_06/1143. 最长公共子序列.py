# https://leetcode-cn.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''自顶向下'''
        # @functools.lru_cache(None)
        # def dp(i, j):
        #     if i < 0 or j < 0: return 0
        #     if text1[i] == text2[j]: return dp(i-1, j-1) + 1
        #     else: return max(dp(i-1, j), dp(i, j-1))
        # return dp(len(text1)-1, len(text2)-1)
        
        '''自底向上'''
        dp = [[0 for i in range(len(text1))] for j in range(len(text2))]
        for i in range(len(text1)):
            dp[0][i] = 1 if text2[0] == text1[i] else dp[0][i-1]
        for i in range(len(text2)):
            dp[i][0] = 1 if text1[0] == text2[i] else dp[i-1][0]
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                dp[j][i] = dp[j-1][i-1] + 1 if text1[i] == text2[j] else max(dp[j-1][i], dp[j][i-1])
        return dp[len(text2)-1][len(text1)-1]
        '''自底向上，优化空间复杂度为O(1)'''
        '''好像不可能'''