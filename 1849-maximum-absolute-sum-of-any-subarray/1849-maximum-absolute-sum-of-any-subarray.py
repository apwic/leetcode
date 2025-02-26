class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = 0
        max_sum, min_sum = 0, 0
        ans = 0
        for num in nums:
            prefix += num

            max_sum = max(max_sum, prefix)
            min_sum = min(min_sum, prefix)

            if prefix >= 0:
                ans = max(ans, prefix - min_sum)
            else:
                ans = max(ans, max(abs(prefix), abs(prefix - max_sum)))

        return ans