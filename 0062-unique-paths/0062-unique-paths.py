class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n] * m
        dp[0][0] = 1

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n

        for i in range(m):
            for j in range(n):
                top, left = i-1, j-1
                valid_top, valid_left = valid(top, j), valid(i, left)

                if valid_top and valid_left:
                    dp[i][j] = dp[top][j] + dp[i][left]
                elif valid_top:
                    dp[i][j] = dp[top][j]
                elif valid_left:
                    dp[i][j] = dp[i][left]

        return dp[-1][-1]