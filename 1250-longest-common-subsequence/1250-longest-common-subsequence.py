class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        @cache
        def dp(i, j):
            if i == n1 or j == n2:
                return 0

            if text1[i] == text2[j]:
                return 1 + dp(i+1, j+1)

            return max(dp(i+1, j), dp(i, j+1))

        return dp(0, 0)
        