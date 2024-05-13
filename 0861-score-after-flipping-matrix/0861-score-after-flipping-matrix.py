class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1
                    
        for j in range(1, n):
            count_zero = 0
            for i in range(m):
                count_zero += 1 if grid[i][j] == 0 else 0
                
            if count_zero > m - count_zero:
                for i in range(m):
                    grid[i][j] ^= 1
                    
        score = 0
        for row in grid:
            score += int(''.join([str(el) for el in row]), base=2)
            
        return score