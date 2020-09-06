# https://leetcode-cn.com/problems/number-of-islands/

# 200题，岛屿数量。

# 此题是经典的搜索问题。

## 方法1：DFS递归
# 为此，我们定义一个mask矩阵。对于每一个搜索到的岛屿点，我们需要对其进行mask操作。

# 对于图上每一个点都进行递归深入操作，如果碰到如下情况，则岛屿数量+1：
# * Map当前值为1
# * Mask对应值为0
def numIslands(self, grid: List[List[str]]) -> int:
    ''''''
    gridMask = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
    count = 0
    def dfs(grid, i, j):

        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]): return
        if gridMask[i][j] or grid[i][j] == '0': return
        if grid[i][j] == '1': gridMask[i][j] = 1
        dfs(grid, i-1, j) # 上
        dfs(grid, i+1, j) # 下
        dfs(grid, i, j-1) # 左
        dfs(grid, i, j+1) # 右
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1' and gridMask[i][j] == 0:
                count += 1
            dfs(grid, i, j)
    return count

## 方法2：BFS
# 广度优先使用一个辅助队列，把访问过的节点加入到队列中去。

# 注意入队需要同时满足要求：
# * 没访问过（因此入队时就要把更新该节点的访问标记）
# * 该节点本身不为零
# 同时，满足这样要求的节点，也符合一个新岛屿的标准。

# 这道题的情况比较特殊，我们对于每一步都要分别设置一个q节点。

def numIslands(self, grid: List[List[str]]) -> int:
    ''''''
    gridMask = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
    count = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1' and not gridMask[i][j]:
                count += 1
                q = deque([(i, j)])
                gridMask[i][j] = 1
                while q:
                    x, y = q.popleft()
                    if x - 1 >= 0 and grid[x-1][y] == "1" and not gridMask[x-1][y]:
                        q.append((x-1, y))
                        gridMask[x-1][y] = 1
                    if x + 1 < len(grid) and grid[x+1][y] == '1' and not gridMask[x+1][y]:
                        q.append((x+1, y))
                        gridMask[x+1][y] = 1
                    if y - 1 >= 0 and grid[x][y-1] == '1' and not gridMask[x][y-1]:
                        q.append((x, y-1))
                        gridMask[x][y-1] = 1
                    if y + 1 < len(grid[0]) and grid[x][y+1] == '1' and not gridMask[x][y+1]:
                        q.append((x, y+1))
                        gridMask[x][y+1] = 1
    return count
