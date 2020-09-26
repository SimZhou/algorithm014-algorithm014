# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices: return 0
        empt = 0
        hold = -prices[0]
        for i in range(1, len(prices)):
            empt = max(empt, hold + prices[i] - fee)            
            hold = max(hold, empt - prices[i])
        return empt
        