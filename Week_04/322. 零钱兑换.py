# https://leetcode-cn.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        定义dp(i)为amount为i时可以够成的组合数目，则
        dp(i) = min(dp(i-m) + 1 for m in coins) （if i-m >= 0）
              = 
        dp(0) = 0
        当[dp(i-m) + 1 for m in coins if i-m >= 0] 列表为空时，返回-1
        例如：[5], 6。dp(6) = dp(1) + 1；dp(1) 列表为空。
        '''
        # @functools.lru_cache(None)
        # def dp(i):
        #     if i < 0: return -1
        #     if i == 0: return 0
        #     good = []
        #     for coin in coins:
        #         if dp(i-coin) == -1: continue
        #         good.append(dp(i-coin) + 1)
        #     return -1 if not good else min(good)
        # return dp(amount)
        '''
        自底向上
        '''
        # 数组大小为 amount + 1，初始值也为 amount + 1
        dp = [amount + 1] * (amount + 1)
        # base case
        dp[0] = 0
        # 外层 for 循环在遍历所有状态的所有取值
        for i in range(len(dp)):
            # 内层 for 循环在求所有选择的最小值
            for coin in coins:
                # 子问题无解，跳过
                if i - coin < 0: continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] == amount + 1 and -1 or dp[amount]