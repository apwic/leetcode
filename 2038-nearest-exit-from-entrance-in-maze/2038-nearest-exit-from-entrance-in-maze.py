class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        entrance = (entrance[0], entrance[1])

        def isExit(x, y):
            return (x, y) != entrance and maze[x][y] == '.' and (x == 0 or x == m-1 or y == 0 or y == n-1)

        def valid(x, y):
            return 0 <= x < m and 0 <= y < n and maze[x][y] == '.' and (x, y) not in seen

        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque([(entrance[0], entrance[1], 0)])
        seen = set({entrance})

        while queue:
            x, y, step = queue.popleft()

            if isExit(x, y):
                return step

            for move in moves:
                new_x, new_y = x + move[0], y + move[1]
                if valid(new_x, new_y):
                    seen.add((new_x, new_y))
                    queue.append((new_x, new_y, step+1))
                    
        return -1
        