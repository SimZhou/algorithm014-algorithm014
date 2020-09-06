# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        最低点到最高点，最低点要在最高点前面
        令dp[i]为当前处卖的最大收益，则dp[i]=prices[i]-min(prices[0:i])
        则ans=max(dp)
        '''
        if not prices: return 0
        dp = [0] * len(prices)
        _min = float("inf")
        for i in range(len(prices)):
            _min = min(_min, prices[i])
            dp[i] = prices[i] - _min
        return max(dp)