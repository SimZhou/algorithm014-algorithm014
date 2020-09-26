# https://leetcode-cn.com/problems/friend-circles/

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        '''DFS，对对角线做dfs即可'''
        def dfs(visited, i):
            for j in range(len(M)):
                if M[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(visited, j)
        visited = set()
        ret = 0
        for i in range(len(M)):
            if i not in visited:
                dfs(visited, i)
                ret += 1
        return ret
        '''并查集'''
#         self.p = [i for i in range(len(M))]
#         for i in range(len(M)):
#             for j in range(len(M)):
#                 if M[i][j] == 1: self.union(i, j)
#         res = set()
#         for i in self.p:
#             res.add(self.find(i))
#         return len(res)
        
#     def union(self, i, j):
#         p1 = self.find(i)
#         p2 = self.find(j)
#         self.p[p1] = p2

#     def find(self, i):
#         root = i
#         while self.p[root] != root:
#             root = self.p[root]
#         while self.p[i] != i: # 路径压缩
#             self.p[i], i = root, self.p[i]
#         return root
        '''并查集2 - 自己写的'''
        p = [i for i in range(len(M))]
        def union(i, j):
            p1 = find(i)
            p2 = find(j)
            p[p1] = p2
        def find(i):
            root = i
            while root != p[root]: root = p[root]
            while i != p[i]: p[i], i = root, p[i]
            return i
        for i in range(len(M)):
            for j in range(len(M)):
                if M[i][j] == 1: union(i, j)
        return len(set(find(i) for i in p))