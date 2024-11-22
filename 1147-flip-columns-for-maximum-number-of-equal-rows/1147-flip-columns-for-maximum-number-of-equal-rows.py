class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        pattern = [[] for _ in range(m)]

        for i in range(m):
            curr = 1
            for j in range(1, n):
                if matrix[i][j] == matrix[i][j-1]:
                    curr += 1
                else:
                    pattern[i].append(curr)
                    curr = 1

            pattern[i].append(curr)

        ans = 0
        for i in range(m):
            curr = 1
            for j in range(m):
                if i == j:
                    continue

                if pattern[i] == pattern[j]:
                    curr += 1

            ans = max(ans, curr)
        
        return ans 