class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        move = [(-1, 0), (1,0), (0, -1), (0, 1)]

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n and grid[i][j] != 0

        def bfs(start, visited):
            pq = deque([start])
            fish = 0
            while pq:
                node = pq.popleft()
                i, j = node

                if visited[i][j] == 1:
                    continue
                visited[i][j] = 1

                fish += grid[i][j]

                for di, dj in move:
                    ni, nj = i + di, j + dj
                    if not valid(ni, nj):
                        continue

                    pq.append((ni, nj))

            return fish

        ans = 0
        visited = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or visited[i][j] == 1:
                    continue

                fish = bfs((i, j), visited)
                ans = max(ans, fish)

        return ans