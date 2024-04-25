class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        result = set()
        
        if bound <= 1:
            return result
        
        a = 1 if x == 1 else int(log(bound, x))
        b = 1 if y == 1 else int(log(bound, y))
        
        for i in range(a + 1):
            for j in range(b + 1):
                val = x**i + y**j
                
                if val <= bound:
                    result.add(val)
                    
        return result
