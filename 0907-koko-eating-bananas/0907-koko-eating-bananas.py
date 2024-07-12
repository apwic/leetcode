class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            total_k = 0

            for pile in piles:
               total_k += ceil(pile / k) 

            return total_k <= h

        l, r = 1, max(piles)
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                r = mid-1
            else:
                l = mid+1

        return l
        