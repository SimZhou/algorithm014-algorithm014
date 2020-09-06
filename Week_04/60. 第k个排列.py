# https://leetcode-cn.com/problems/permutation-sequence/

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        '''字典序算法，O(kn)，O(n)'''
        def nextPermute(s):
            for i in range(len(s)-2, -1, -1):
                if s[i] < s[i+1]:
                    break
            else:
                s[:] = s[::-1]
                return
            for j in range(len(s)-1, -1, -1):
                if s[j] > s[i]: 
                    break
            s[i], s[j] = s[j], s[i]
            s[i+1:] = reversed(s[i+1:])
            return s
        
        res = list(range(1, n+1))
        for i in range(k-1):
            nextPermute(res)
        return "".join([str(_) for _ in res])
        '''DFS，超时'''
        # def dfs(n, path, visited, k):
        #     if len(res) == k: return
        #     if len(path) == n:
        #         res.append(path)
        #         return
        #     for i in range(1, n+1):
        #         if i not in visited:
        #             dfs(n, path + str(i), visited.union({i}), k)
        # res = []
        # dfs(n, "", set(), k)
        # return res[-1]