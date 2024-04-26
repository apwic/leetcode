from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if (n == 1):
            return matrix[0][0]

        dp = [row[:] for row in matrix] # create deep copy

        for i in range(1, n):
            for j in range(n):
                l = float('inf') if j < 1 else dp[i-1][j-1]
                m = dp[i-1][j]
                r = float('inf') if j + 1  >= n else dp[i-1][j+1]

                dp[i][j] += min(l, m, r)

        return min(dp[-1])
        