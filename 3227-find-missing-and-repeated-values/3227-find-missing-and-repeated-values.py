class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        count = [1] * (n*n)

        for i in range(n):
            for j in range(n):
                count[grid[i][j] - 1] -= 1
                
        ans = [0, 0]
        for i in range(n*n):
            if count[i] == -1:
                ans[0] = i+1
            if count[i] == 1:
                ans[1] = i+1
                
        return ans