# https://leetcode-cn.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        '''
        费马平方和定理：
        如果质数c可以被表示为4k+1的形式，那么它就可以被平方和分解；如果是4k+3的形式，则不能
        '''
        # for i in range(2, int(math.sqrt(c))+1):
        #     count = 0
        #     if c % i == 0:
        #         while c % i == 0:
        #             count += 1
        #             c /= i
        #         if i % 4 == 3 and count % 2 != 0:
        #             return False
        # return c % 4 != 3
        
        '''
        双指针 + sqrt函数
        '''
        l, r = 0, int(math.sqrt(c))
        while l <= r:
            if l**2 + r**2 == c: return True
            elif l**2 + r**2 < c: l += 1
            else: r -= 1
        return False