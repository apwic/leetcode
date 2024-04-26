class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if n == 1:
            return grid[0][0]

        dp = [row[:] for row in grid]

        for i in range(1, n):
            for j in range(n):
                dp[i][j] += min([dp[i-1][col] for col in range(n) if col != j])

        return min(dp[-1])