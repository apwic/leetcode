class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        prefix = [0] * n
        prefix[0] = grid[0][0]
        suffix = [0] * n
        suffix[n-1] = grid[1][n-1]

        for i in range(1, n):
            prefix[i] = prefix[i-1] + grid[0][i]
            suffix[n-i-1] = suffix[n-i] + grid[1][n-i-1]

        ans = float('inf')
        prefix_max, suffix_max = prefix[n-1], suffix[0]
        for i in range(n):
            ans = min(ans, max(prefix_max - prefix[i], suffix_max - suffix[i]))

        return ans