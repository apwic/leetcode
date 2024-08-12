class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        free, hold = [0] * n, [0] * n
        hold[0] = -prices[0]

        for i in range(1, n):
            # Profit before or sell today -> from hold + price
            free[i] = max(free[i-1], hold[i-1] + prices[i] - fee)
            # Profit before or buy today -> from free - price
            hold[i] = max(hold[i-1], free[i-1] - prices[i])

        return max(free[-1], hold[-1])
