# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''自底向上，O(n) O(n)'''
        # if len(prices) == 0: return 0
        # dp = [[0 for _ in range(2)] for __ in range(len(prices))]
        # dp[0][1] = -prices[0]
        # for i in range(1, len(prices)):
        #     dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        #     dp[i][1] = max(dp[i-1][1],  - prices[i])
        # return dp[len(prices)-1][0]
        '''自底向上，O(n) O(1)'''
        if len(prices) == 0: return 0
        profit0, profit1 = 0, -prices[0]
        for i in range(1, len(prices)):
            profit0, profit1 = max(profit0, profit1 + prices[i]), max(profit1, -prices[i])
        return profit0
        '''自顶向下，O(n) O(n)'''
        # if not prices: return 0
        # @functools.lru_cache(None)
        # def dp(i, j):
        #     if i == 0 and j == 0: return 0
        #     if i == 0 and j == 1: return -prices[0]
        #     if j == 0: return max(dp(i-1, 0), dp(i-1, 1) + prices[i])
        #     if j == 1: return max(dp(i-1, 1), - prices[i])
        # return dp(len(prices)-1, 0)

        '''
        最低点到最高点，最低点要在最高点前面
        令dp[i]为当前处卖的最大收益，则dp[i]=prices[i]-min(prices[0:i])
        则ans=max(dp)
        '''
        # if not prices: return 0
        # dp = [0] * len(prices)
        # _min, _max = float("inf"), float("-inf")
        # for i in range(len(prices)):
        #     _min = min(_min, prices[i])
        #     _max = max(prices[i] - _min, _max)
        # return _max