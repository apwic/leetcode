class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n

        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0, 0)])
        visited = [[float('inf')] * n for _ in range(m)]
        visited[0][0] = 0

        while queue:
            i, j, obstacle = queue.popleft()

            for dx, dy in directions:
                x, y = i + dx, j + dy

                if not (valid(x, y) and visited[x][y] == float('inf')):
                    continue

                val = grid[x][y]

                if val == 0:
                    queue.appendleft((x, y, obstacle + val))
                else:
                    queue.append((x, y, obstacle + val))

                visited[x][y] = obstacle + val

        return visited[-1][-1]