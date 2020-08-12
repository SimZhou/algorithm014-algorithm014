# https://leetcode-cn.com/problems/surrounded-regions/

# 方法1：遍历每个O点，开始进行搜索，如果碰到边界则该点需要更新为O，否则为X
# 方法2：从边界开始遍历每个O，开始进行搜索，搜索到的O点都保留O，其余为X
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        方法2
        """
        if board == []: return []
        self.res = []
        x = len(board)
        y = len(board[0])
        for i in range(x):
            self._dfs((i, 0), board)
            self._dfs((i, y-1), board)
        for j in range(y):
            self._dfs((0, j), board)
            self._dfs((x-1, j), board)
            
        for i in range(x):
            for j in range(y):
                board[i][j] = "X"
        for i, j in self.res:
            board[i][j] = "O"
    
    def _dfs(self, point, board):
        i, j = point
        # 终止条件
        # 如果输入点为X，停止搜索
        # 如果输入点已经在res表中，则停止搜索
        if board[i][j] == "X": return
        elif (i, j) in self.res: return
        
        # 否则，将当前点添加到res表，并搜索它的上下左右点
        else:
            self.res.append((i, j))
            # 上
            if i-1 >= 0:
                self._dfs((i-1, j), board)
            # 下
            if i+1 <= len(board)-1:
                self._dfs((i+1, j), board) 
            # 左
            if j-1 >= 0:
                self._dfs((i, j-1), board)
            # 右
            if j+1 <= len(board[0])-1:
                self._dfs((i, j+1), board)