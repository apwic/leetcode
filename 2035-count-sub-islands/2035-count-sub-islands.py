class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 0:
                    continue

                if grid1[i][j]:
                    grid1[i][j] = 2
                else:
                    grid1[i][j] = 3
                    
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n and not visited[i][j]

        def dfs(i, j):
            if grid1[i][j] == 3:
                return False

            visited[i][j] = True
            valid = True

            for dx, dy in directions:
                x, y = i + dx, j + dy

                if 0 <= x < m and 0 <= y < n and not visited[x][y] and grid2[x][y] == 1:
                    if not dfs(x, y):
                        valid = False

            return valid

        visited = [[False for _ in range(n)] for _ in range(m)]
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid1[i][j] != 2:
                    continue

                if not visited[i][j]:
                    if dfs(i, j):
                        ans += 1

        return ans