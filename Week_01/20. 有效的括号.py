# https://leetcode-cn.com/problems/valid-parentheses/

class Solution:        
    def isValid(self, s: str) -> bool:
        '''
        栈解法
        '''
        q = collections.deque()
        for i in s:
            if i in "(": q.append(")")
            elif i in "[": q.append("]")
            elif i in "{": q.append("}")
            elif i in ")]}":
                if not q: return False
                if q.pop() != i: return False
        if len(q) == 0: return True
        else: return False