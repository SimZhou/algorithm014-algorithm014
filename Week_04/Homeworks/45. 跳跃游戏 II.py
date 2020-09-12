# https://leetcode-cn.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        '''贪心算法，每次找当前能跳到位置中能跳最远的，作为下一个落脚点，当到达边界时，更新边界为最远落脚点，并且steps+1'''
        maxPos, end, step = 0, 0, 0
        for i in range(len(nums)-1):
            maxPos = max(maxPos, i+nums[i])  # 更新最大值
            if i == end: # 该跳了
                end = maxPos
                step += 1
        return step
        '''
        2 3 1 1 4
        0 1 1 2
        dp[i] = min(dp[j] + 1 for j in range(0, i) if nums[j] + j >= i)
        dp[0] = 0
        动态规划超时了，代码应该是对的
        '''
        # if len(nums) == 1: return 0
        # @functools.lru_cache(None)
        # def dp(i):
        #     if i == 0: return 0
        #     return min(dp(j) + 1 for j in range(0, i) if nums[j] + j >= i)
        # return dp(len(nums)-1)