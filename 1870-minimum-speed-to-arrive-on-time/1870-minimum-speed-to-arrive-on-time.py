class Solution:    
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def complete(v):
            total = 0
            for i in range(len(dist)):
                count = dist[i]/v
                if (i != len(dist) - 1):
                    count = (dist[i] + v - 1)//v
                total += count
                
                if (total > hour):
                    return False
                
            if (total <= hour):
                return True
    
        l = 1
        r = 10**7
        while (l < r):
            v = (l + r)//2
            flag = complete(v)
                
            if (flag):
                r = v
            else:
                l = v + 1
                
        if (complete(l)):
            return l
            
        return -1
            
            
        
        
        
        
        