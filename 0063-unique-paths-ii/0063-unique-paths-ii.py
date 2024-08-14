class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n and obstacleGrid[i][j] == 0

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue

                top, left = i-1, j-1
                valid_top, valid_left = valid(top, j), valid(i, left)

                if valid_top and valid_left:
                    dp[i][j] = dp[top][j] + dp[i][left]
                elif valid_top:
                    dp[i][j] = dp[top][j]
                elif valid_left:
                    dp[i][j] = dp[i][left]

        return dp[-1][-1]
        