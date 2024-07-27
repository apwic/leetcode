class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        def dp(step):
            if step == 0 or step == 1:
                return 0

            if step in memo:
                return memo[step]
                
            memo[step] = min(dp(step-1) + cost[step-1], dp(step-2) + cost[step-2])
            return memo[step]

        return dp(n)
        