# https://leetcode-cn.com/problems/assign-cookies/

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        '''对于每个小孩，我们挑选饼干中恰好能满足他胃口的最小饼干去满足他'''
        '''其实是双指针'''
        g.sort(), s.sort()
        i = j = 0
        count = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]: 
                count, i, j = count + 1, i + 1, j + 1
            else:
                j += 1
        return count