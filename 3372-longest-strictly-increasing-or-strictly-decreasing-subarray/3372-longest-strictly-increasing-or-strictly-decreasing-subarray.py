class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc, dec = 1, 1
        ans = 1

        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                inc = 0
            inc += 1

            if nums[i-1] <= nums[i]:
                dec = 0
            dec += 1

            ans = max(ans, inc, dec)

        return ans
