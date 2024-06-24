class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        def valid(x, y):
            return 0 <= x < m and 0 <= y < n

        queue = deque([(0, 0, 0, k)])
        seen = set({(0, 0, k)})
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while queue:
            x, y, dist, rem = queue.popleft()

            if x == m-1 and y == n-1:
                return dist

            for move in moves:
                new_x, new_y = x + move[0], y + move[1]

                if valid(new_x, new_y):
                    if grid[new_x][new_y] == 1 and rem > 0 and (new_x, new_y, rem-1) not in seen:
                        queue.append((new_x, new_y, dist+1, rem-1))
                        seen.add((new_x, new_y, rem-1))

                    if grid[new_x][new_y] == 0 and (new_x, new_y, rem) not in seen:
                        queue.append((new_x, new_y, dist+1, rem))
                        seen.add((new_x, new_y, rem))

        return -1
        