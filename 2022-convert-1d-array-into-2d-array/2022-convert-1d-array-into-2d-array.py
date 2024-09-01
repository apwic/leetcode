class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        size = len(original)

        if size != m*n:
            return []

        ans = [[0 for _ in range(n)] for _ in range(m)]
        idx = 0

        for i in range(m):
            for j in range(n):
                ans[i][j] = original[idx]
                idx += 1

        return ans