class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points) 
        closest = [(sqrt(x*x+y*y), [x, y]) for x, y in points]
        heapq.heapify(closest)

        ans = []
        while len(closest) > n-k:
            dist, point = heapq.heappop(closest)
            ans.append(point)

        return ans
        