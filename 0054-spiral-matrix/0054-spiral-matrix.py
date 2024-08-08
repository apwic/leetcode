class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        def valid(i, j):
            return 0 <= i < m and 0 <= j < n and (i, j) not in seen

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        seen = {(0, 0)}
        ans = [matrix[0][0]]

        while len(seen) < m * n:
            for dx, dy in directions:
                x, y = x + dx, y + dy
    
                while valid(x, y):
                    ans.append(matrix[x][y])
                    seen.add((x, y))
                    x, y = x + dx, y + dy
    
                x, y = x - dx, y - dy

        return ans