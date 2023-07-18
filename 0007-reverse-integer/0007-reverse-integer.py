class Solution:
    import math
    
    def reverse(self, x: int) -> int:
        if (x == 0):
            return x
    
        neg = False
        if (x < 0):
            x *= -1
            neg = True
            
        rev = 0
        div = 10 ** (math.floor(math.log10(x)))
        while (x > 0):
            temp = x % 10
            x = (x - temp) // 10
            rev += temp * div 
            div = div // 10
            
        if (neg):
            rev *= -1
        
        if (rev <= -2**31 or rev >= 2**31 -1):
            return 0
        
        return rev
            