class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            new_dp = defaultdict(int)
            for key, val in dp.items():
                new_dp[key + num] += val
                new_dp[key - num] += val

            dp = new_dp

        return dp[target]