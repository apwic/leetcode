class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        turn = 1
        
        while (n != 1):
            for i in range(1, n):
                if (n % i == 0):
                    turn += 1
                    n -= i
                    break
                    
        if (turn % 2 == 0):
            return True
        else:
            return False
            