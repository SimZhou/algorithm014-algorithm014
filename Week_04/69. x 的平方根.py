# https://leetcode-cn.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        '''牛顿迭代法'''
        # if x <= 1: return x
        # start, diff = x, 1
        # while diff > 1e-15:
        #     start, diff = x/(2*start) + start/2, abs(x/(2*start) + start/2 - start)
        # return int(start)
        '''二分法'''
        '''二分法的实质是要找到一个整数m，m**2 <= x, (m+1)**2 > x'''
        l, r = 0, x // 2 + 1        # 0 一定小于等于x的平方根，x//2 + 1 一定大于
        while l < r:
            # print(l, r)
            mid = (l + r) // 2 + 1
            if mid * mid == x: return mid
            if mid * mid < x: 
                l = mid
            else:
                r = mid - 1
        return l