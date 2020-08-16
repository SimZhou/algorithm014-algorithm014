# https://leetcode-cn.com/problems/bulls-and-cows/

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        '''
        
        '''
        c1= collections.Counter()
        i = 0
        A, B = 0, 0
        while i <= len(secret)-1:
            if secret[i] == guess[i]:
                A += 1
                i += 1
            else:
                c1.update({secret[i]: 1})
                i += 1
        for i in range(len(guess)):
            if secret[i] == guess[i]: continue
            elif c1[guess[i]] > 0: 
                c1.subtract({guess[i]: 1})
                B += 1
        return str(A) + "A" + str(B) + "B"