class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num, i) for i, num in enumerate(nums)]
        heapify(heap)

        for _ in range(k):
            pop, i = heapq.heappop(heap)
            heapq.heappush(heap, (pop*multiplier, i))

        for num, i in heap:
            nums[i] = num

        return nums