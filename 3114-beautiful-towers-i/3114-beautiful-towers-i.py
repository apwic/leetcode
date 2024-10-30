class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        n = len(heights)
        ans = 0

        for peak in range(n):
            adjusted = heights[:]

            for i in range(peak-1, -1, -1):
                adjusted[i] = min(adjusted[i], adjusted[i+1])

            for i in range(peak+1, n):
                adjusted[i] = min(adjusted[i], adjusted[i-1])

            ans = max(ans, sum(adjusted))

        return ans