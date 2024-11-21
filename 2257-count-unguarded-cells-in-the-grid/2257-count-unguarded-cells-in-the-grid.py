class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def seen(i, j):
            return 0 <= i < m and 0 <= j < n and grid[i][j] != WALL and grid[i][j] != GUARD

        WALL = -99
        GUARD = 1
        SEEN = -1

        grid = [[0 for _ in range(n)] for _ in range(m)]

        for i, j in walls:
            grid[i][j] = WALL

        for i, j in guards:
            grid[i][j] = GUARD

        for i, j in guards:
            north = j+1
            while seen(i, north):
               grid[i][north] = SEEN
               north += 1 

            south = j-1
            while seen(i, south):
                grid[i][south] = SEEN
                south -= 1

            west = i-1
            while seen(west, j):
                grid[west][j] = SEEN
                west -=1

            east = i+1
            while seen(east, j):
                grid[east][j] = SEEN
                east += 1

        unseen = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    unseen += 1
                    
        return unseen