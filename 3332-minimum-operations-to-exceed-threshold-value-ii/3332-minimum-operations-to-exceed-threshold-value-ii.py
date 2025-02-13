class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        ans = 0

        while len(nums) >= 2 and nums[0] < k:
            x = heappop(nums)
            y = heappop(nums)
            heappush(nums, 2*x + y)
            ans += 1

        return ans
        