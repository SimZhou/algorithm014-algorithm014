# https://leetcode-cn.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        '''定义2个变量，分别用来记录5元，10元零钱数量'''
        coin5, coin10 = 0, 0
        for i in bills:
            if i == 5: coin5 += 1
            if i == 10: coin5, coin10 = coin5 - 1, coin10 + 1
            if i == 20: 
                if coin10 <= 0:
                    coin5 -= 3
                else:
                    coin5, coin10 = coin5 - 1, coin10 - 1
            if not coin5 >= 0 or not coin10 >= 0: return False
        return True