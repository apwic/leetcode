class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n, k = len(nums),  max(nums)
        curr, ans = 0, 0

        for i in range(1, n):
            if nums[i] != k:
                continue

            if nums[i-1] == nums[i]:
                curr += 1
                ans = max(curr, ans)
            else:
                curr = 0

        return ans+1