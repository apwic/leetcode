class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(n):
            max_before = 0 if i-2 < 0 else dp[i-2]
            dp[i] = max(max_before + nums[i], dp[i-1])

        return dp[n-1]
