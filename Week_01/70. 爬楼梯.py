# https://leetcode-cn.com/problems/climbing-stairs/submissions/

class Solution:
    def __init__(self):
        self.cache = {}
    def climbStairs(self, n: int) -> int:
        '''
        快速幂解法
        快速幂的核心是二分法
        a^n = a^(n/2)^2 = a^(n/4)^2^2
        '''
        if n <= 1: return 1
        a, b, c, d = self.quickPower(n-1)
        return a + b
        
    def quickPower(self, n):
        '''
        1 1 的n次方，输入n，输出 a b
        1 0                    c d
        '''
        n = int(n)
        if n in self.cache: return self.cache[n]
        
        if n == 1: return 1, 1, 1, 0
        elif n & 1:
            print(n)
            a, b, c, d = self.quickPower((n-1)/2)
            a, b, c, d = a*a + b*c, a*b + b*d, c*a + d*c, c*b + d*d
            self.cache[n] = a + c, b + d, a, b
            return a + c, b + d, a, b
        else: 
            a, b, c, d = self.quickPower(n/2)
            self.cache[n] = a*a + b*c, a*b + b*d, c*a + d*c, c*b + d*d
            return a*a + b*c, a*b + b*d, c*a + d*c, c*b + d*d
        
#     def climbStairs(self, n: int) -> int:
#         '''
#         n阶阶梯的爬法有
#           n-1阶阶梯的爬法 加上
#           n-2阶阶梯的爬法
#           （最后一步可以一次爬1也可以一次爬2）
#         递推公式：
#           T(n) = T(n-1) + T(n-2)
          
#         以下是自底向上迭代法 2020.8.10
#         '''
#         a, b = 1, 1
        
#         for i in range(n-1):
#             a, b = b, a+b
        
#         return b

#     def climbStairs(self, n: int) -> int:
#         '''
#         n阶阶梯的爬法有
#           n-1阶阶梯的爬法 加上
#           n-2阶阶梯的爬法
#           （最后一步可以一次爬1也可以一次爬2）
#         递推公式：
#           T(n) = T(n-1) + T(n-2)
          
#         以下是自顶向下dp法 2020.8.10
#         '''
#         if n in self.cache: return self.cache[n]
        
#         if n == 0: 
#             return 1
#         if n == 1:
#             return 1
        
#         ans = self.climbStairs(n-1) + self.climbStairs(n-2)
#         self.cache[n] = ans
#         return ans