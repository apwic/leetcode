class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isVowel(ch):
            return ch == 'a' or ch == 'i' or ch == 'e' or ch == 'u' or ch == 'o'
        
        vwl = 0
        l = curr = 0
        mx = 0
        n = len(s)
        
        for r in range(n):
            curr += 1
            if (isVowel(s[r])):
                vwl += 1
                
            while (curr > k):
                if (isVowel(s[l])):
                    vwl -= 1
                l += 1
                curr -= 1
                    
            mx = max(mx, vwl)
            
        return mx
                