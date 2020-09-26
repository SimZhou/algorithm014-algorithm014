# https://leetcode-cn.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = obstacleGrid.copy()
        if dp[m-1][n-1]: return 0
        dp[m-1][n-1] = 1 
        for i in range(m-2, -1, -1):
            dp[i][n-1] = dp[i+1][n-1] if not dp[i][n-1] else 0
        for j in range(n-2, -1, -1):
            dp[m-1][j] = dp[m-1][j+1] if not dp[m-1][j] else 0
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1] if not dp[i][j] else 0
        return dp[0][0]