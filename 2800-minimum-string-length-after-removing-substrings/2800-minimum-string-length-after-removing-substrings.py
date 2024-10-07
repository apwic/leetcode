class Solution:
    def minLength(self, s: str) -> int:
        while "AB" in s or "CD" in s:
            n = len(s)
            for i in range(1, n):
                if s[i-1:i+1] == "AB" or s[i-1:i+1] == "CD":
                    s = s[:i-1] + s[i+1:]
                    break

        return len(s)