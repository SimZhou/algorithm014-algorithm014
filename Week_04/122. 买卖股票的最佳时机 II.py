# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        其实这个问题就是在翻越一座座连续山峰中，只记录上山阶段的上升高度的问题
        '''
        # profit = 0
        # for i in range(1, len(prices)):
        #     if prices[i-1] <= prices[i]: profit += prices[i] - prices[i-1]
        # return profit
        '''
        亦可以尝试用DP来解，定义dp(i, j)为当前到i，状态为j时能吃到的最大利润，例如：
             7, 1, 5, 3, 6, 4
        j=0  0, 0, 4, 4, 7, 7
        j=1 -7,-1,-1, 1, 1, -
        '''
        dp = [[0 for _ in range(2)] for __ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
        return dp[len(prices)-1][0]