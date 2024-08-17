class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = points[0][:]

        for i in range(1, m):
            left = [0] * n
            right = [0] * n

            left[0] = dp[0]
            for j in range(1, n):
                left[j] = max(dp[j], left[j-1] - 1)

            right[n-1] = dp[n-1]
            for j in range(n-2, -1, -1):
                right[j] = max(dp[j], right[j+1] - 1)

            for j in range(n):
                dp[j] = points[i][j] + max(left[j], right[j])

        return max(dp)