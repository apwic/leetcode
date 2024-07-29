class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n+1)  

        for i in range(n-1, -1, -1):
            point, power = questions[i]
            j = power + i + 1
            # Either take this question, or take the latter
            dp[i] = max(point + dp[min(n, j)], dp[i+1])

        return dp[0]