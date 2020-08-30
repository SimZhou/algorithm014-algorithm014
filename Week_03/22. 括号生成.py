# https://leetcode-cn.com/problems/generate-parentheses/

# n=1 1 ()
# n=2 2 (()) ()()
# n=3 5 ((())) (())() ()(()) ()()() (()())
# 解构
# (
# ((   ()(
# (((  (()(   ()((   (())(  ()()(   ×())((

class Solution:
    @functools.lru_cache
    def generateParenthesis(self, n: int) -> List[str]:
        # # (a)b 法，
        # # 比如n=1，a，b为0，
        # #     n=2，()()或(())，
        # #     n=3，20,11,02, ((())), (()()), (())(),()(()), ()()()
        # if not n: return [""]
        # res = []
        # for i in range(n):
        #     for a in self.generateParenthesis(i):
        #         for b in self.generateParenthesis(n-i-1):
        #             res.append("({}){}".format(a, b))
        # return res
        
#         # 递归剪枝2
        res = []
        def dfs(temp, left, right):
            if len(temp) == 2*n: res.append(temp)
            if left < n: dfs(temp+"(", left + 1, right)
            if left > right: dfs(temp+")", left, right + 1)
        dfs("", 0, 0)
        return res
        
        
        # 递归剪枝1
#         res = []
#         self._dfs(n, n, res, "", 0)
#         return res
        
#     def _dfs(self, a, b, res, temp, count):  # a,b分别代表左右括号，使用count来进行开放括号计数
#         # print(a, b, temp, res, count)
#         if a == b == 0:
#             res.append(temp)
#             return
        
#         # 如果a不为0，则可以选择左括号。选择后count+1，a-1
#         # 如果b不为0，且count不为0，则可以选择右括号，选择后，count-1，b-1
#         for p in "()":
#             if p == "(" and a:
#                 count, a, temp = count + 1, a - 1, temp + p
#                 self._dfs(a, b, res, temp, count)
#                 count, a, temp = count - 1, a + 1, temp[:-1]
#             elif p == ")" and b and count:
#                 count, b, temp = count - 1, b - 1, temp + p
#                 self._dfs(a, b, res, temp, count)
#                 count, b, temp = count + 1, b + 1, temp[:-1]