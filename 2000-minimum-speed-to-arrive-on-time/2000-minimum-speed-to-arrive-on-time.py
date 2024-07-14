class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)
        def check(speed):
            total = 0

            for i in range(n):
                time = dist[i]/speed
                if i != n-1:
                    time = math.ceil(time)
                total += time

            return total <= hour

        l, r = 1, 10**7
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                r = mid-1
            else:
                l = mid+1

        return l if l <= 10**7 else -1
        