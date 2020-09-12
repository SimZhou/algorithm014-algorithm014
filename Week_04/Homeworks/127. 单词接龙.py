# https://leetcode-cn.com/problems/word-ladder/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        BFS，从beginword出发寻找所有满足条件的word，入队。
        对于队中所有word，继续寻找满足条件的word，直到找到位置
        visited过的不必再入队
        时间：O(n**2)，最坏情况下路径为一条线，每次遍历会遍历一遍所有元素
        空间：O(n)，最坏储存所有节点
        '''
        # q = deque([beginWord])
        # visited = [0] * len(wordList)
        # count = 0
        # while q:
        #     count += 1
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         for i in range(len(wordList)):
        #             if not visited[i] and self.distance(wordList[i], node) == 1:
        #                 # print(node, wordList[i], count)
        #                 if wordList[i] == endWord: return count+1
        #                 q.append(wordList[i])   
        #                 visited[i] = 1
        # return 0
    # def distance(self, str1, str2):
    #     return sum([0 if i == j else 1 for i, j in zip(str1, str2)])
        '''另一种思路，生成式判断距离'''
        q = deque([beginWord])
        wordSet = set(wordList)
        count = 0
        while q:
            count += 1
            for _ in range(len(q)):
                candidate = q.popleft()
                for i in range(len(candidate)):
                    for sub in 'abcdefghijklmnopqrstuvwxyz':
                        new_candidate = candidate[:i] + sub + candidate[i+1:]
                        if new_candidate == candidate: continue
                        if new_candidate in wordSet: 
                            if new_candidate == endWord: return count + 1
                            q.append(new_candidate)
                            wordSet.remove(new_candidate)
        return 0
        '''双向BFS'''