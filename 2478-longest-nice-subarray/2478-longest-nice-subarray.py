class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        window = 0
        ans = 1

        for r in range(n):
            while window & nums[r] != 0:
                window ^= nums[l]
                l += 1

            window |= nums[r]
            ans = max(ans, r-l+1)

        return ans