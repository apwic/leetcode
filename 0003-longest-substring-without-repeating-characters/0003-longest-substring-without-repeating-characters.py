class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        last_idx = {}
        n = len(s)
        l, count = 0, 0
        
        for r in range(n):
            if s[r] in last_idx and last_idx[s[r]] >= l:
                l = last_idx[s[r]] + 1
                
            last_idx[s[r]] = r
            count = max(count, r-l+1)
            
        return count