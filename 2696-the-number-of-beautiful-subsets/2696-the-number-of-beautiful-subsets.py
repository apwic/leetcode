class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        n = len(nums)
        dp = defaultdict(int)

        def backtrack(idx, dp):
            if idx == n:
                return 1

            take = 0
            val = nums[idx]

            if dp[val - k] == 0 and dp[val + k] == 0:
                dp[val] += 1
                take = backtrack(idx+1, dp)
                dp[val] -= 1

            not_take = backtrack(idx+1, dp)
            return take + not_take

        return backtrack(0, dp) - 1