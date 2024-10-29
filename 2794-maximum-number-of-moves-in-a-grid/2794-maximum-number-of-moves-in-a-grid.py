class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        def valid(i, j):
            return 0 <= i < row and 0 <= j < col

        row, col = len(grid), len(grid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]

        for j in range(col-2, -1, -1):
            for i in range(row-1, -1, -1):
                top, mid, bot = -1, -1, -1

                if valid(i-1, j+1) and grid[i-1][j+1] > grid[i][j]:
                    top = dp[i-1][j+1]
                if valid(i, j+1) and grid[i][j+1] > grid[i][j]:
                    mid = dp[i][j+1]
                if valid(i+1, j+1) and grid[i+1][j+1] > grid[i][j]:
                    bot = dp[i+1][j+1]

                dp[i][j] = max(top, mid, bot) + 1

        return max([row[0] for row in dp])
