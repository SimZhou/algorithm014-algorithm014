# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ''''''
        '''自底向上，O(n) O(n)'''
        # if len(prices) == 0: return 0
        # dp = [[0 for i in range(2)] for j in range(len(prices))]
        # dp[0][0] = 0
        # dp[0][1] = -prices[0]
        # for i in range(1, len(prices)):
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])                      # 空仓 或 卖出
        #     dp[i][1] = max(dp[i - 1][1], (dp[i - 2][0] if i >= 2 else 0) - prices[i])   # 持仓 或 买入
        # return dp[len(prices) - 1][0]
    
        '''自底向上优化，O(n)，O(1)'''
        if len(prices) == 0: return 0
        prevProfit0 = 0
        profit0 = 0
        profit1 = -prices[0]
        for i in range(len(prices)):
            nextProfit0 = max(profit0, profit1 + prices[i])
            nextProfit1 = max(profit1, prevProfit0 - prices[i])
            prevProfit0 = profit0
            profit0 = nextProfit0
            profit1 = nextProfit1
        return profit0