class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            gift = heapq.heappop(gifts)
            left = floor(sqrt(-gift))
            heapq.heappush(gifts, -left)

        return -sum(gifts)