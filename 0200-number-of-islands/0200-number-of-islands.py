class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        moves = [[-1,0], [1,0], [0,-1], [0,1]]
        def dfs(node):
            if node not in seen:
                x, y = node
                seen.add((x, y))
                for move in moves:
                    new_x = x + move[0]
                    new_y = y + move[1]
                    if new_x < 0 or new_x > m-1 or new_y < 0 or new_y > n-1:
                        continue

                    if (new_x, new_y) in seen:
                        continue
                        
                    if grid[new_x][new_y] == "0":
                        continue

                    dfs((new_x, new_y))

        seen = set()
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue

                if (i, j) not in seen:
                    ans += 1
                    dfs((i, j))

        return ans