class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = []
        for i in range(n):
            dp.append([])
            for j in range(i+1):
                dp[i].append(0)

        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            for j in range(i+1):
                max_i = max(0, i-1)
                max_j = max(0, j-1)
                min_j = min(i-1, j)
                dp[i][j] = min(dp[max_i][max_j], dp[max_i][min_j]) + triangle[i][j]

        return min(dp[-1])