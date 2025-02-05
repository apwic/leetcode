class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        diff = 0
        s1a, s1b = "", ""
        s2a, s2b = "", ""

        for i in range(n):
            if s1[i] != s2[i]:
                diff += 1
                
                if diff == 1:
                    s1a = s1[i]
                    s2a = s2[i]
                
                if diff == 2:
                    s1b = s1[i]
                    s2b = s2[i]
                    
            if diff > 2:
                return False

        return diff == 0 or (diff == 2 and s1a == s2b and s1b == s2a)