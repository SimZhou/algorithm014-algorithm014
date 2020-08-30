# https://leetcode-cn.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        方法1；暴力O(n**3)，查找n**2，验证n
        '''
        pass
        
        '''
        方法2：二维DP
        dp(i, j)代表i->j位置的子串是否是回文串
        转移方程：dp(i, j) = dp(i+1, j-1) and (s[i] == s[j])
        - 为什么是二维？
        因为是二维的输入，产生了2维的dp表
        斐波那契算二维dp么吗？不算，因为它只产生了一维线性的状态表，只不过有重叠子问题
        使它的计算过程变成了一颗树。
        - 二维dp的初始状态从哪里计算？
        从边界条件开始计算。
        在这个问题中，边界条件为：当i==j或者j-i==1时(没有字符或者字符个数为1时，为回文串)
        因此，起始点有大约 2*len(s) 个
        - 如何设计循环来填写这张表格？
        首先，对于每一个i，j=i+1，都有一个初始值，
        然后，对于每一个初始值，都可以向外扩散直到边界，并且在扩散时，记录最大长度对应的i,j
        复杂度分析：O(n**2) O(n**2)
        '''
        # dp = [[False for _ in range(len(s))] for __ in range(len(s))]
        # # 计算顺序：先计算i==j的情况，然后i+1==j......
        # _max, _maxIndex = 0, (0, 0)
        # for sep in range(0, len(s)):
        #     for i in range(0, len(s) - sep):
        #         if sep == 0: dp[i][i+sep] = True                             # 边界条件
        #         else: dp[i][i+sep] = (dp[i+1][i+sep-1] or sep < 2) and s[i] == s[i+sep]   # 转移方程
        #         if dp[i][i+sep] and sep+1 >= _max: _maxIndex = i, i+sep      # 更新最大值
        # return s[_maxIndex[0]:_maxIndex[1]+1]
        '''
        方法3：二维DP，自顶向下递归，带缓存
        二维dp也需要两层循环进行初始化，只不过方向不同（从右上角开始）
        '''
#         if not s: return ""
        
#         @functools.lru_cache(None)
#         def dp(s, i, j): 
#             if i >= j: return True
#             else: return (dp(s, i+1, j-1) or j-i < 2) and s[i] == s[j]
            
#         for sep in range(len(s)-1, -1, -1):
#             for i in range(len(s) - sep):
#                 if dp(s, i, i + sep): return s[i:i+sep+1]
        '''
        方法4：中心扩散法，很好理解，使用双指针，O(n**2), O(1)，但是要注意分奇偶数情况
        '''
        longest = ''
        for i in range(len(s)):
            m, n = i, i
            while m >= 0 and n <= len(s)-1 and s[m] == s[n]: 
                if n-m+1 > len(longest): longest = s[m:n+1]
                m, n = m-1, n+1
        for j in range(len(s)-1):
            m, n = j, j+1
            while m >= 0 and n <= len(s)-1 and s[m] == s[n]:
                if n-m+1 > len(longest): longest = s[m:n+1]
                m, n = m-1, n+1
        return longest
        '''
        方法5：Manacher算法
        '''