import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if(n <= 2):
            return 0
        
        prime = [True for i in range(n)]
        
        p = 2
        while(p*p <= n):
            if (prime[p] == True):
                for i in range(p*p, n, p):
                    prime[i] = False
            p += 1
                   
        count = 0
        for p in range(2, n):
            if (prime[p]):
                print(p)
                count += 1
                        
        return count
                