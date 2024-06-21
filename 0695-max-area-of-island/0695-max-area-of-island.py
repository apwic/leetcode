class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def valid(node):
            x, y = node
            return 0 <= x < m and 0 <= y < n and grid[x][y] == 1

        moves = [[1,0], [-1, 0], [0, 1], [0, -1]]

        def dfs(node):
            area = 0
            if node not in seen:
                area = 1
                seen.add(node)
                x, y = node
                for move in moves:
                    new_x = x + move[0]
                    new_y = y + move[1]
                    neighbor = (new_x, new_y)

                    if valid(neighbor):
                        area += dfs(neighbor)
                        
            return area

        seen = set()
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                node = (i, j)
                if node not in seen:
                    ans = max(ans, dfs(node))
                    print(seen)

        return ans