class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def check(boundary):
            n = k+1
            curr = 0
            for sweet in sweetness:
                curr += sweet
                if curr >= boundary:
                    n -= 1
                    curr = 0

            return n <= 0

        l, r = min(sweetness), sum(sweetness)//(k+1)
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                l = mid+1
            else:
                r = mid-1

        return r
        