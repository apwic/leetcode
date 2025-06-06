class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(col+1)] for _ in range(row + 1)]

        ans = 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    continue

                dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j]) + 1
                ans += dp[i+1][j+1]

        return ans