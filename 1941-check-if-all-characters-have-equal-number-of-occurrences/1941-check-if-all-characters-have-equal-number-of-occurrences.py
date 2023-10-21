from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hm = defaultdict(int)
        
        for c in s:
            hm[c] += 1
            
        x = hm[s[0]]
        for i in hm:
            if hm[i] != x:
                return False
            
        return True