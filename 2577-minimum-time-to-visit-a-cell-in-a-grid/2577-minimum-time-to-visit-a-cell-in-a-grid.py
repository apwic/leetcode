class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        def valid(i, j):
            return 0 <= i < m and 0 <= j < n and not visited[i][j]

        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])

        visited = [[0] * n for _ in range(m)]
        visited[0][0] = 1
        queue = [(0, 0, 0)]
        heapq.heapify(queue)

        while queue:
            time, i, j= heapq.heappop(queue)

            if i == m-1 and j == n-1:
                return time

            for dx, dy in directions:
                x, y = i + dx, j + dy

                if not valid(x, y):
                    continue

                wait = 0
                if (grid[x][y] - time) % 2 == 0:
                    wait += 1

                next_time = max(grid[x][y] + wait, time+1)
                visited[x][y] = 1
                heapq.heappush(queue, (next_time, x, y))

        return -1
                