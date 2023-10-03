from math import factorial as f

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        def combinator(m, n):
            return f(m) // (f(n) * f(m-n))
        
        hm = [0 for i in range(100)]
        
        for i in nums:
            hm[i-1] += 1
            
        total = 0
        for i in hm:
            if i > 1:
                total += combinator(i, 2)
                
        return total
        