from typing import List
import functools

def jump(nums: List[int]) -> int:
    '''贪心算法，每次找当前能跳到位置中能跳最远的，作为下一个落脚点，当到达边界时，更新边界为最远落脚点，并且steps+1'''
    maxPos, end, step = 0, 0, 0
    for i in range(len(nums)-1):
        maxPos = max(maxPos, i+nums[i])  # 更新最大值
        if i == end: # 该跳了
            end = maxPos
            step += 1
    return step

def jump2(nums: List[int]) -> int:
    '''DP'''
    if len(nums) == 1: return 0
    @functools.lru_cache(None)
    def dp(i):
        if i == 0: return 0
        return min(dp(j) + 1 for j in range(0, i) if nums[j] + j >= i)
    return dp(len(nums)-1)

if __name__ == '__main__':
    nums = [1] * 500
    print(jump(nums) == jump2(nums))