class Solution:
    import heapq, math
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)

        while k > 0:
            max_stone = heapq.heappop(piles)
            heapq.heappush(piles, max_stone - math.ceil(max_stone/2))
            k -= 1

        return -sum(piles)
        