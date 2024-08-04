class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if sequence == word:
            return 1

        n = len(sequence)
        m = len(word)
        dp = [0] * n

        for i in range(n-m+1):
            curr = sequence[i:i+m]
            if curr == word:
                dp[i] = dp[i-m] + 1

        return max(dp)
