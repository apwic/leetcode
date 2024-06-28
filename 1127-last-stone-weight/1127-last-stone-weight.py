class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, -1*abs(x-y))

        if stones:
            return -1*stones[0]
        else:
            return 0