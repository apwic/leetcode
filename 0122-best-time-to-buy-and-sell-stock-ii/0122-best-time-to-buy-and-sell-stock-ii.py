class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        free, hold = [0] * n, [0] * n
        hold[0] = -prices[0]

        for i in range(1, n):
            hold[i] = max(hold[i-1], free[i-1] - prices[i])
            free[i] = max(free[i-1], hold[i-1] + prices[i])
            
        return free[-1]