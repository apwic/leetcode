class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def valid(i, j):
            return 0 <= i < n and 0 <= j < n and (i, j) not in seen

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = {(0, 0)}
        x, y = 0, 0
        ans = [[1 for _ in range(n)] for _ in range(n)]
        num = 2

        while len(seen) < n*n:
            for dx, dy in directions:
                x, y = x + dx, y + dy

                while valid(x, y):
                    ans[x][y] = num
                    num += 1
                    seen.add((x, y))
                    x, y = x + dx, y + dy

                x, y = x - dx, y - dy

        return ans