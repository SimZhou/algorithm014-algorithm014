# https://leetcode-cn.com/problems/ugly-number-ii/

# 使用栈预先计算
# 每次把2k,3k,5k入栈，k为栈顶最小值
# n不超过1690，
# 复杂度：1690次操作，每次操作包含：3x（+logk）


# 使用栈预先计算
# 每次把2k,3k,5k入栈，k为栈顶最小值
# n不超过1690，
# 复杂度：1690次操作，每次操作包含：3x（+logk）

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 三指针解法
        res = [0] * 1690
        res[0] = 1
        p2 = p3 = p5 = 0
        for i in range(1, 1690):
            a = res[p2] * 2
            b = res[p3] * 3
            c = res[p5] * 5
            ugly = min(a, b, c)
            if ugly == a: p2 += 1
            if ugly == b: p3 += 1
            if ugly == c: p5 += 1
            # if res[i-1] < min(a,b,c):  
            res[i] = ugly
        return res[n-1]

# 堆预计算法
#     def __init__(self):
#         self.res = []
#         self.hp = [1]
#         self.visited = set()
        
#         for _ in range(1690):
#             element = heapq.heappop(self.hp)
#             self.res.append(element)
#             for i in [2,3,5]:
#                 if element*i not in self.visited:
#                     heapq.heappush(self.hp, element*i)
#                     self.visited.add(element*i)

#     def nthUglyNumber(self, n: int) -> int:
#         return self.res[n-1]