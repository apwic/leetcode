class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for c in t:
            if (i == len(s)):
                return True
            
            if (c == s[i]):
                print(c)
                i += 1
        
        if (i == len(s)):
            return True
        
        return False