from collections import deque
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        vis = [[0] * n for _ in range(n)]
        move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        component_sizes = {}
        component_id = 2

        def valid(i, j):
            return 0 <= i < n and 0 <= j < n and grid[i][j] == 1 and vis[i][j] == 0

        def bfs(start, comp_id):
            size = 0
            pq = deque([start])
            vis[start[0]][start[1]] = comp_id
            state = [start]

            while pq:
                x, y = pq.popleft()
                size += 1

                for dx, dy in move:
                    nx, ny = x + dx, y + dy
                    if valid(nx, ny):
                        vis[nx][ny] = comp_id
                        pq.append((nx, ny))
                        state.append((nx, ny))

            component_sizes[comp_id] = size

        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1 and vis[x][y] == 0:
                    bfs((x, y), component_id)
                    component_id += 1

        max_size = max(component_sizes.values(), default=0)

        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0:
                    seen_components = set()
                    possible_size = 1 

                    for dx, dy in move:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and vis[nx][ny] > 1:
                            comp_id = vis[nx][ny]
                            if comp_id not in seen_components:
                                seen_components.add(comp_id)
                                possible_size += component_sizes[comp_id]

                    max_size = max(max_size, possible_size)

        return max_size
