# https://leetcode-cn.com/problems/word-ladder-ii/
# 国际版答案：https://leetcode.com/problems/word-ladder-ii/discuss/269012/Python-BFS%2BBacktrack-Greatly-Improved-by-bi-directional-BFS

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        '''自己写的BFS，使用类似于字典树的结构保存路径'''
        q = collections.deque([beginWord])
        res = collections.defaultdict(set)
        cont = False
        wordList = set(wordList)
        if endWord not in wordList: return []
        
        while q and not cont: 
            wordList -= set(q)
            for _ in range(len(q)):
                node = q.popleft()
                for adjword in [node[:i] + c + node[i+1:] for i in range(len(node)) for c in 'abcdefghijklmnopqrstuvwxyz']:
                    if adjword in wordList:
                        if adjword == endWord: 
                            cont = True
                        else:
                            q.append(adjword)
                        res[node].add(adjword)
        def getAns(word):
            return [[word]] if word == endWord else [[word] + j for i in res[word] for j in getAns(i)]
        # print(res)
        return getAns(beginWord)
        
        '''国际版解法1：BFS'''
#         tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
#         if endWord not in wordList: return []
        
#         found, q, nq = False, {beginWord}, set()
#         while q and not found:
#             words -= set(q)
#             for x in q:
#                 for y in [x[:i]+c+x[i+1:] for i in range(n) for c in 'qwertyuiopasdfghjklzxcvbnm']:
#                     if y in words:
#                         if y == endWord: 
#                             found = True
#                         else: 
#                             nq.add(y)
#                         tree[x].add(y)
#             q, nq = nq, set()
#         def bt(x): 
#             return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]
#         print(tree)
#         return bt(beginWord)

        '''国际版解法2：DBFS'''
        # tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
        # if endWord not in wordList: return []
        # found, bq, eq, nq, rev = False, {beginWord}, {endWord}, set(), False
        # while bq and not found:
        #     words -= set(bq)
        #     for x in bq:
        #         for y in [x[:i]+c+x[i+1:] for i in range(n) for c in 'qwertyuiopasdfghjklzxcvbnm']:
        #             if y in words:
        #                 if y in eq: 
        #                     found = True
        #                 else: 
        #                     nq.add(y)
        #                 tree[y].add(x) if rev else tree[x].add(y)
        #     bq, nq = nq, set()
        #     if len(bq) > len(eq): 
        #         bq, eq, rev = eq, bq, not rev
        # def bt(x): 
        #     return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]
        # return bt(beginWord)