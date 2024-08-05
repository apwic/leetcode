class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * n] * m
        dp[0][0] = grid[0][0]

        def valid(x, y):
            return 0 <= x < m and 0 <= y < n

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                top, left = i-1, j-1
                top_val, left_val = float('inf'), float('inf')

                if valid(top, j):
                    top_val = dp[top][j]
                if valid(i, left):
                    left_val = dp[i][left]

                dp[i][j] = min(top_val, left_val) + grid[i][j]

        return dp[-1][-1]