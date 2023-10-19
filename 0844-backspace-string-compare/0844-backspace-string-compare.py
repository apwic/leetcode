class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        bs = 0
        
        for i in range(len(s)-1, -1, -1):
            if (s[i] == '#'):
                s.pop(i)
                bs += 1
                continue
                
            if (bs > 0):
                s.pop(i)
                bs -= 1
          
        bs = 0
        for i in range(len(t)-1, -1, -1):
            if (t[i] == '#'):
                t.pop(i)
                bs += 1
                continue
                
            if (bs > 0):
                t.pop(i)
                bs -= 1
                
        s = ''.join(s)
        t = ''.join(t)
        
        print(s, t)
        
        return s == t
            
        