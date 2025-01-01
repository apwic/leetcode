class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)

        left = [0] * n
        right = [0] * n
        score_left = score_right = 0
        for i in range(n):
            score_left += 1 if s[i] == "0" else 0
            score_right += 1 if s[n-i-1] == "1" else 0

            left[i] = score_left
            right[n-i-1] = score_right

        ans = 0
        for i in range(n-1):
            ans = max(ans, left[i] + right[i+1])

        return ans
