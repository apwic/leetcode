class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        def rotate(x):
            return s[x:] + s[:x]
        
        n = len(s)
        
        for i in range(n):
            if (rotate(i) == goal):
                return True
            
        return False