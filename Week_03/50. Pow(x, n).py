# https://leetcode-cn.com/problems/powx-n/

# Pow(x, n)，此题求x的n次幂，x可为负值（-100, 100），n也可为负值，为int32整数。

# 此题是经典的递归DP问题，暴力法由于太过简单，不作展开。
# 方法1：动态规划，自顶向下
# 自顶向下的动态规划比较容易想到，递推式为：

	# dp(x, n) = 
	# dp(x, n/2) · dp(x, n/2)    if n > 0
	# dp(1/x, -n)                     if n < 0 

# 边界条件为当n==0时，return 1；当n==1时，return x本身。
# 这里需要注意的是，n大于0和n小于0的情况要分开讨论，n小于0时，直接求1/x的n次方即可。

# 方法2：动态规划，自底向上
# 自底向上的动态规划法不是特别容易想到，其关键在于找到何时需要补充乘x进入循环。
# 观察规律，我们发现：

	# 当n = 5时，ans = (x^2)^2 · x = x^2^2 · x                                  ，bin(5) = 101
	# 当n = 8时，ans = (((x^2)^2)^2) = x^(2^3)                                ，bin(8) = 1000
	# 当n = 13时，ans = (((x^2 · x)^2)^2 · x) = x^(2^3) · x^(2^2) · x ，bin(13) = 1101

# 可以发现哪个位置(i)上是1，就需要在最终答案中贡献出x^(2^i)。于是问题就迎刃而解了。

class Solution:
    def myPow(self, x: float, n: int) -> float:
            
    # @functools.lru_cache(None)
    # def myPow(self, x: float, n: int) -> float:
    #     if n < 0: return self.myPow(1/x, -n)
    #     if n == 0: return 1
    #     if n == 1: return x
    #     else:
    #         if not n % 2: return self.myPow(x, n/2) ** 2
    #         else: return (self.myPow(x, (n-1)/2) ** 2) * x
    
        '''自底向上'''
        if n < 0: return self.myPow(1/x, -n)
        if n == 0: return 1
        ans = 1
        while n:
            if n & 1: ans *= x
            x, n= x * x, n >> 1
        return ans