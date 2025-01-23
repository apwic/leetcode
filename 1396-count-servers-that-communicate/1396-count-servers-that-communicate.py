class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            sr = None
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                if sr == None:
                    sr = (i, j)
                else:
                    visited[sr[0]][sr[1]] = 1
                    visited[i][j] = 1

        for i in range(n):
            sr = None
            for j in range(m):
                if grid[j][i] == 0:
                    continue

                if sr == None:
                    sr = (j, i)
                else:
                    visited[sr[0]][sr[1]] = 1
                    visited[j][i] = 1

        return sum(sum(row) for row in visited)