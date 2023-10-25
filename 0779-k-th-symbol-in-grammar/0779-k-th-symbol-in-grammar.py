class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if (n == 0):
            return 0
        
        # if even, check the k origin from the previous row
        # because 01 is originated from 0
        # and 10 is originated from 1
        if (k % 2 == 0):
            return 1 - self.kthGrammar(n-1, k//2)
        else:
            return self.kthGrammar(n-1, (k+1)//2)