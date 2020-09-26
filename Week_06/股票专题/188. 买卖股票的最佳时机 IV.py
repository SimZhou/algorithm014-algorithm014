# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        '''DP，自底向上，O(nk)，O(nk)，买入记1'''
#         if not prices or not k: return 0
#         dp = [[[0 for _ in range(2)] for __ in range(k + 1)] for ___ in range(len(prices))]
#         if k >= len(prices) // 2: return self.maxp(prices)
#         for i in range(1, k+1):
#             dp[0][i][0] = 0
#             dp[0][i][1] = -prices[0]
        
#         for i in range(1, len(prices)):
#             for j in range(1, k+1):
#                 dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
#                 dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
#         return dp[len(prices)-1][k][0]
        '''DP，自底向上优化，O(nk)，O(k)'''
        if not prices or not k: return 0
        if k >= len(prices) // 2: return self.maxp(prices)
        dp = [[0 for _ in range(2)] for __ in range(k + 1)]
        for i in range(1, k+1):
            dp[i][0] = 0
            dp[i][1] = -prices[0]
        for i in range(1, len(prices)):
            for j in range(1, k+1):
                dp[j][0] = max(dp[j][0], dp[j][1] + prices[i])
                dp[j][1] = max(dp[j][1], dp[j-1][0] - prices[i])
        return dp[k][0]
    
    def maxp(self, prices):
        _sum = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]: _sum += prices[i] - prices[i-1]
        return _sum