# https://leetcode-cn.com/problems/walking-robot-simulation/

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        start = [0, 0]
        go = (0, 1)
        obstacles = set((i, j) for i, j in obstacles)
        res = 0
        '''逆时针90°：[[0,-1],[1,  0]]'''
        '''顺时针90°：[[0, 1],[-1, 0]]'''
        a, b, c, d = 0, -1, 1, 0
        a_, b_, c_, d_ = 0, 1, -1, 0
        for com in commands:
            if com == -2: go = go[0]*a + go[1]*b, go[0]*c + go[1]*d
            if com == -1: go = go[0]*a_ + go[1]*b_, go[0]*c_ + go[1]*d_
            else:
                for _ in range(com):
                    if (start[0]+go[0], start[1]+go[1]) not in obstacles:
                        start = [start[0]+go[0], start[1]+go[1]]
                        res = max(res, start[0]**2 + start[1]**2)
        return res