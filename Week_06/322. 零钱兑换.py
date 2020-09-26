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
        #     candidates = []
        #     for c in coins:
        #         if dp(i-c) == -1: continue                            # 注意这里的判断逻辑，只添加递归过后大于等于0的结果
        #         candidates.append(dp(i-c)+1)
        #     return -1 if not candidates else min(candidates)
        # return dp(amount)
            
        '''
        自底向上，转移方程：dp[i] = min(dp[i-c]+1 for c in coins)  (if i-c >= 0)
        '''
        dp = [float('inf')] * (amount + 1) # 为什么要amount+1，因为要考虑dp[0]的情况
        dp[0] = 0                          # amount为0，需要0个硬币
        for i in range(1, len(dp)):
            for c in coins:
                if i-c < 0: continue
                dp[i] = min(dp[i], dp[i-c]+1)
        return -1 if dp[amount] == float('inf') else dp[amount]