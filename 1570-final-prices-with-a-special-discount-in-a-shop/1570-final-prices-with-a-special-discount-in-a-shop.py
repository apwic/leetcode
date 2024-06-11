class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                popped = stack.pop()
                prices[popped] -= prices[i]
                prices[popped] = max(0, prices[popped])
            stack.append(i)

        return prices
