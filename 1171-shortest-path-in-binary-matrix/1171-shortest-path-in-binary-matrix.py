class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        def valid(x, y):
            return 0 <= x < n and 0 <= y < n and grid[x][y] == 0 and (x, y) not in seen

        moves = [(-1,-1), (-1, 0), (-1, 1), (1, 0), (1, 1), (0,1), (1, -1), (0,-1)]
        queue = deque([(0, 0, 1)])
        seen = set()

        while queue:
            x, y, step = queue.popleft()
            if (x, y) not in seen:
                seen.add((x, y))

                if x == n-1 and y == n-1:
                    return step

                for move in moves:
                    new_x, new_y = x + move[0], y + move[1]

                    if valid(new_x, new_y):
                        queue.append((new_x, new_y, step+1))

        return -1