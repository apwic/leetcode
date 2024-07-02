class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = [-num for num in nums]
        heapq.heapify(heap)

        ans = 0
        while len(heap) > n-k:
            ans = heapq.heappop(heap)

        return -ans 