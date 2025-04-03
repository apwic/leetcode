class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix, suffix = [0] * n, [0] * n
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]

        for i in range(1, n):
            prefix[i] = max(prefix[i-1], nums[i])
            suffix[n-i-1] = max(suffix[n-i], nums[n-i-1])

        ans = 0
        for i in range(1, n-1):
            ans = max(ans, (prefix[i-1] - nums[i]) * suffix[i+1])

        return ans