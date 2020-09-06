# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        其实这个问题就是在翻越一座座连续山峰中，只记录上山阶段的上升高度的问题
        '''
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] >= 0: profit += prices[i] - prices[i-1] 
        return profit