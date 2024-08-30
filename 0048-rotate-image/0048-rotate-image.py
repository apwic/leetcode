class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        matrix[:] = [[matrix[j][i] for j in range(n)] for i in range(m)]
        matrix[:] = [row[::-1] for row in matrix]