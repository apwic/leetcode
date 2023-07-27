class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def sn(n):
            if (n == 1):
                return "0"
            
            p = sn(n-1)
            bit_mask = (1 << len(p)) - 1
            return p + "1" + (bin(int(p, 2) ^ bit_mask)[2:])[::-1]
        
        return sn(n)[k-1]
        