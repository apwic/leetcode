class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0]) 
        ans = [[0 for _ in range(n)] for _ in range(m)] 
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        def valid(x, y, seen):
            return 0 <= x < m and 0 <= y < n and mat[x][y] == 1 and (x, y) not in seen

        queue = deque()
        seen = set()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    seen.add((i, j))

        while queue:
            x, y, dist = queue.popleft()
            ans[x][y] = dist
                
            for move in directions:
                new_x, new_y = x + move[0], y + move[1]
                if valid(new_x, new_y, seen):
                    queue.append((new_x, new_y, dist+1))
                    seen.add((new_x, new_y))

        return ans
                