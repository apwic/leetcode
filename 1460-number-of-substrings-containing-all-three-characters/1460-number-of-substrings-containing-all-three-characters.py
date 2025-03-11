class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        freq = {"a": -1, "b": -1, "c": -1}
        ans = 0
        
        for i in range(n):
            freq[s[i]] = i
            ans += 1 + min(freq.values())

        return ans