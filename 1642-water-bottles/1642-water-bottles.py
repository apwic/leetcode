class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = 0
        ans = 0

        while numBottles:
            ans += numBottles
            emptyBottles += numBottles

            numBottles = emptyBottles // numExchange
            emptyBottles = emptyBottles % numExchange
            
        return ans
