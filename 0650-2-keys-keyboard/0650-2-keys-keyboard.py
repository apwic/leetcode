class Solution:
    def minSteps(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        dp[1] = 0

        for i in range(1, n+1):
            for j in range(1, i):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + (i//j))

        return dp[-1]