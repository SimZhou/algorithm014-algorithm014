# https://leetcode-cn.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        tab = set()
        while 1:
            n = sum([int(i)**2 for i in list(str(n))])
            if n == 1: return True
            elif n in tab: return False
            else:
                tab.add(n)