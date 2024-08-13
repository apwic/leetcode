class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        free, hold, reset = float('-inf'), float('-inf'), 0

        for price in prices:
            prev_free = free
            free = hold + price
            hold = max(hold, reset - price)
            reset = max(reset, prev_free)

        return max(free, reset)
