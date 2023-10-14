class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        check = set(['a', 'i', 'u', 'e', 'o'])
        vwl = 0
        l = curr = 0
        mx = 0
        n = len(s)
        
        for r in range(n):
            curr += 1
            if (s[r] in check):
                vwl += 1
                
            while (curr > k):
                if (s[l] in check):
                    vwl -= 1
                l += 1
                curr -= 1
                    
            mx = max(mx, vwl)
            
        return mx
                