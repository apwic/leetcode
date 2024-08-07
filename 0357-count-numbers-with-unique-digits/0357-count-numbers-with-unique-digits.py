class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        dp = [0] * (n)
        dp[0] = 10 
        digit = 9
        avail = 9

        for i in range(1, n):
            avail = avail * digit
            dp[i] = dp[i-1] + avail
            digit = max(digit-1, 0)

        return dp[n-1]