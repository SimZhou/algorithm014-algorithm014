https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''三维DP，自底向上 O(n) O(n)，买入时计数'''
        # if len(prices) == 0: return 0
        # dp = [[[0 for _ in range(2)] for __ in range(3)] for ___ in range(len(prices))]
        # dp[0][1][0] = 0
        # dp[0][1][1] = -prices[0]
        # dp[0][2][0] = 0
        # dp[0][2][1] = -prices[0]
        # for i in range(1, len(prices)):
        #     dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
        #     dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i])
        #     dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + prices[i])
        #     dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0] - prices[i])
        # return dp[len(prices)-1][2][0]
        '''卖出时计数'''
        # if len(prices) == 0: return 0
        # dp = [[[0 for _ in range(2)] for __ in range(3)] for ___ in range(len(prices))]
        # dp[0][0][1] = -prices[0]
        # dp[0][1][0] = 0
        # dp[0][1][1] = -prices[0]
        # dp[0][2][0] = 0
        # for i in range(1, len(prices)):
        #     dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][0][0] - prices[i])
        #     dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][1] + prices[i])
        #     dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][1][0] - prices[i])
        #     dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][1][1] + prices[i])
        # return dp[len(prices)-1][2][0]
        '''为什么这样奏效？因为此表格只更新到k=2，后面便不再更新'''
        '''自底向上，O(n) O(1)'''
        if len(prices) == 0: return 0
        hold0, empt1, hold1, empt2 = -prices[0], 0, -prices[0], 0
        for i in range(1, len(prices)):
            hold0, empt1, hold1, empt2 = max(hold0, -prices[i]), max(empt1, hold0+prices[i]), max(hold1, empt1-prices[i]), max(empt2, hold1+prices[i])
        return empt2