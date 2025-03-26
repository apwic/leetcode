class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        arr = []

        if m * n == 1:
            return 0

        for i in range(m):
            for j in range(n):
                arr.append(grid[i][j])

        arr.sort()
        target = arr[(m*n)//2]

        ans = 0
        for num in arr:
            if num % x != 0:
                return -1

            ans += abs(num - target) // x

        return ans