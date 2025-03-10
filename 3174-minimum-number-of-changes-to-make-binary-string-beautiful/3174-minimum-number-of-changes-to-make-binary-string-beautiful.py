class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(0, n, 2):
            if s[i] != s[i+1]:
                ans += 1 

        return ans