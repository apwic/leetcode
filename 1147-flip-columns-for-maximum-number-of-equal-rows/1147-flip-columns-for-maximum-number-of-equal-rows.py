class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        freq_pattern = defaultdict(int)

        for row in matrix:
            pattern = "".join("T" if el == row[0] else "F" for el in row)
            freq_pattern[pattern] += 1

        return max(freq_pattern.values())