class Solution:
    import heapq
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        roads = [0] * (max(trip[2] for trip in trips) + 1)
        n = len(roads)

        for (cap, start, end) in trips:
            roads[start] += cap
            roads[end] -= cap

        curr = 0
        for i in range(n):
            curr += roads[i]

            if curr > capacity:
                return False

        return True