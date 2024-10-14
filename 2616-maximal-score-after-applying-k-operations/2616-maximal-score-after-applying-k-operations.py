class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)

        ans = 0
        for _ in range(k):
            val = -heapq.heappop(nums)
            ans += val
            heapq.heappush(nums, -ceil(val/3))

        return ans