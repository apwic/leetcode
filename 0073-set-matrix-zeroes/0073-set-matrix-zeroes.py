class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row, col = set(), set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        row, col = list(row), list(col)
        for i in row:
            for j in range(n):
                matrix[i][j] = 0

        for j in col:
            for i in range(m):
                matrix[i][j] = 0
