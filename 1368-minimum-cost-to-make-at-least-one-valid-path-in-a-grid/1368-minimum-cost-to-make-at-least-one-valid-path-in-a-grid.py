class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        def valid(i, j):
            return 0 <= i < m and 0 <= j < n

        m, n = len(grid), len(grid[0])
        move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # cost, x, y
        pq = [(0, 0, 0)]
        heapify(pq)
        visited = [[float('inf') for _ in range(n)] for _ in range(m)]

        # dijkstra
        while pq:
            cost, x, y = heappop(pq)

            if cost >= visited[x][y]:
                continue  
            visited[x][y] = cost

            if x == m-1 and y == n-1:
                return cost

            curr_move = move[grid[x][y]-1]
            for dx, dy in move:
                nx, ny = x + dx, y + dy

                if not valid(nx, ny):
                    continue

                if curr_move == (dx, dy):
                    heappush(pq, (cost, nx, ny))
                else:
                    heappush(pq, (cost+1, nx, ny))

        return -1
