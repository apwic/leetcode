class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        move = [(-1, 0), (1, 0), (0, -1), (0 ,1)]
        m, n = len(heightMap), len(heightMap[0])

        def valid(x, y):
            return 0 <= x < m and 0 <= y < n


        visited = [[False for _ in range(n)] for _ in range(m)]
        pq = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    heappush(pq, (heightMap[i][j], i, j))
                    visited[i][j] = True

        ans = 0
        while pq:
            height, x, y = heappop(pq)

            for dx, dy in move:
                nx, ny = x + dx, y + dy

                if valid(nx, ny) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    next_height = heightMap[nx][ny]

                    if height > next_height:
                        ans += height - next_height

                    heappush(pq, (max(height, next_height), nx, ny))

        return ans
