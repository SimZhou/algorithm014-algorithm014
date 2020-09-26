# https://leetcode-cn.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''原味DP'''
        if not grid: return 0
        for i in range(1, len(grid)): grid[i][0] += grid[i-1][0]
        for i in range(1, len(grid[0])): grid[0][i] += grid[0][i-1]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] = min(grid[i][j]+grid[i-1][j], grid[i][j]+grid[i][j-1])
        return grid[len(grid)-1][len(grid[0])-1]
    
        '''Dijkstra'''
        # visited = set()
        # pq = []
        # heapq.heappush(pq, (grid[0][0], (0, 0)))
        # distance = {(m, n): float('inf') for m in range(len(grid)) for n in range(len(grid[0]))}
        # distance[(0, 0)] = grid[0][0]
        # while pq:
        #     dis, (x, y) = heapq.heappop(pq)
        #     if (x, y) in visited: continue
        #     visited.add((x, y))
        #     for m, n in [(x+1, y), (x, y+1)]:
        #         if m >= len(grid) or n >= len(grid[0]): continue
        #         new_dis = distance[(x, y)] + grid[m][n]
        #         if new_dis < distance[(m, n)] and (m, n) not in visited:
        #             distance[(m, n)] = new_dis
        #             heapq.heappush(pq, (distance[(m, n)], (m, n)))
        # return distance[(len(grid)-1, len(grid[0])-1)]