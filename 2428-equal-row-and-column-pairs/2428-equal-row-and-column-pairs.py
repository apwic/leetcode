class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        from collections import defaultdict
        n = len(grid)
        freq = defaultdict(int)

        cols = []
        for j in range(n):
            col = []
            for i in range(n):
                grid[i][j] = str(grid[i][j])
                col.append(grid[i][j])

            col = '-'.join(col)
            cols.append(col)
            freq[col] += 1
        
        ans = 0
        for row in grid:
            row = '-'.join(row)
            if freq[row]:
                ans += freq[row]

        return ans
