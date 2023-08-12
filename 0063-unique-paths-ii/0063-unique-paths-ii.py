class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        grid = [[-1 for j in range(n)] for i in range(m)]
        
        def path(i, j):
            if (i == m or j == n):
                return 0
            
            if (obstacleGrid[i][j] == 1):
                return 0
            
            if (i == m-1 and j ==n-1):
                grid[i][j] = 1
            
            if (grid[i][j] != -1):
                return grid[i][j]
            
            grid[i][j] = path(i, j+1) + path(i+1, j)
            return grid[i][j]
                
        return path(0, 0)