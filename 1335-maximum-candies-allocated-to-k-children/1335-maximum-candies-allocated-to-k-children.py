class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(num_candy):
            child = 0

            for candy in candies:
                child += candy // num_candy

            return child >= k
            
        max_candy = 0
        for candy in candies:
            max_candy = max(max_candy, candy)

        l, r = 0, max_candy

        while l < r:
            mid = (l + r + 1) // 2

            if check(mid):
                l = mid
            else:
                r = mid - 1

        return l