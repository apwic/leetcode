class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        
        for char in s:
            i = ord(char) - ord('a')
            a = max(0, i - k)
            b = min(25, i + k) + 1
            reach = []
            for j in range(a, b):
                reach.append(dp[j])
                
            dp[i] = max(reach) + 1
            
        return max(dp)