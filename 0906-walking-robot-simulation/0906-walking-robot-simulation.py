class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y, pos = 0, 0, 90
        obstacles = set(map(tuple, obstacles))

        directions = {
                90: (0, 1),    # north
                0: (1, 0),     # east
                270: (0, -1),  # south
                180: (-1, 0)   # west
            }

        def rotate(command, pos):
            return (pos - 90) % 360 if command == -1 else (pos + 90) % 360

        ans = 0
        for command in commands:
            if command == -1 or command == -2:
                pos = rotate(command, pos)
                continue

            dx, dy = directions[pos]
            for _ in range(command):
                next_x, next_y = x + dx, y + dy
                if (next_x, next_y) in obstacles:
                    break
                x, y = next_x, next_y

            ans = max(ans, x*x + y*y)

        return ans
                        
