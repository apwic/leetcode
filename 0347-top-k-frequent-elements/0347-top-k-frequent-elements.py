class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        heap = [(val, key) for key, val in freq.items()]
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)

        return [key for _, key in heap]
        