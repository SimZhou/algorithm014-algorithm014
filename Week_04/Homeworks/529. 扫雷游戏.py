# https://leetcode-cn.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click
        if board[x][y] == "M": 
            board[x][y] = "X"
            return board
        elif board[x][y] in set(list('12345678B')):
            return board
        
        visited = set()
        def dfs(board, x, y):
            if (x, y) in visited or x<0 or y<0 or x>=len(board) or y>=len(board[0]): return
            visited.add((x, y))
            
            if board[x][y] == 'E':
                # 判断周围雷数
                bombAmount = 0
                for m, n in [(x-1, y),(x+1, y),(x, y-1),(x, y+1),(x-1, y-1),(x+1, y+1),(x-1, y+1),(x+1, y-1)]:
                    if m>=0 and n>=0 and m<len(board) and n<len(board[0]) and board[m][n]=='M': bombAmount += 1
                if bombAmount == 0:
                    board[x][y] = 'B'
                    [dfs(board, m, n) for m, n in [(x-1, y),(x+1, y),(x, y-1),(x, y+1),(x-1, y-1),(x+1, y+1),(x-1, y+1),(x+1, y-1)]];
                else:
                    board[x][y] = str(bombAmount)
                    return
        dfs(board, x, y)
        return board