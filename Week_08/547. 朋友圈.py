# https://leetcode-cn.com/problems/friend-circles/

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        '''DFS'''
#         def dfs(i, visited):
#             if i in visited: return
#             visited.add(i)
#             for j in range(0, len(M)):
#                 if M[i][j] == 1: 
#                     dfs(j, visited)

#         count, visited = 0, set()
#         for i in range(len(M)):
#             if i not in visited:
#                 count += 1
#                 dfs(i, visited)
#         return count
        
        '''并查集'''
        def find(i):
            root = i
            while root != table[root]: root = table[root]
            while i != root: i, table[i] = table[i], root
            return root
        def union(i, j):
            x, y = find(i), find(j)
            table[x] = y
        
        table = list(range(len(M)))
        for i in range(len(M)):
            for j in range(i, len(M)):
                if M[i][j] == 1:
                    union(i, j)
        return len(set(find(i) for i in table))