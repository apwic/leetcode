class Solution:
    import heapq
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)

        ans = 0
        while len(sticks) > 1:
            a, b = heapq.heappop(sticks), heapq.heappop(sticks)
            heapq.heappush(sticks, a+b)
            ans += a + b

        return ans
        