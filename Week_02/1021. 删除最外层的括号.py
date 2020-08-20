# https://leetcode-cn.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        '''
        1. 原语化。2. 拆除各原语最外层括号。
        双指针查找各原语下标
        (()())()
        12121010
        '''
        # 双指针 原语化
        pri_ind = []
        temp = 0
        j = 0
        for i in range(len(S)):
            if S[i] == "(": temp += 1
            elif S[i] == ")": temp -= 1
            if temp == 0: 
                pri_ind.append((j, i))
                j = i + 1
        # 提取原语
        res = ''
        for m, n in pri_ind:
            res += S[m+1:n]
        return res