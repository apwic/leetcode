class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        days = set(days)
        dp = [0] * (last_day + 1)
        min_cost = min(costs)

        for day in range(1, last_day+1):
            if day not in days:
                dp[day] = dp[day-1]
                continue

            cost1 = dp[day-1] + costs[0]
            cost2 = dp[max(0, day-7)] + costs[1]
            cost3 = dp[max(0, day-30)] + costs[2]
            dp[day] = min(cost1, cost2, cost3)

        return dp[-1]