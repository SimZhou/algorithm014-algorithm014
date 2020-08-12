# https://leetcode-cn.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''a'''
        carry = 0
        num, carry = (digits[-1] + 1)%10, (digits[-1] + 1)//10
        digits[-1] = num
        for i in range(len(digits)-2, -1, -1):
            num, carry = (digits[i]+carry)%10, (digits[i]+carry)//10
            digits[i] = num
        if carry == 1:
            return [1] + digits
        else: return digits
        
#         '''
#         递归
#         '''
#         n = len(digits)
#         last = digits[-1]
#         if n == 1 and last == 9: return [1, 0]
#         if n == 1: return [last + 1]
        
#         if n > 1 and last != 9: return digits[:n-1] + [last+1]
#         if n > 1 and last == 9: return self.plusOne(digits[:n-1]) + [0]