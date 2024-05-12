class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        new_n = n - 2
        matr = [[0 for _ in range(new_n)] for _ in range(new_n)]
        
        for i in range(new_n):
            for j in range(new_n):
                max_val = 0
                for a in range(i, i+3):
                    for b in range(j, j+3):
                        temp = grid[a][b]
                        if temp > max_val:
                            max_val = temp
                
                matr[i][j] = max_val
                
        return matr