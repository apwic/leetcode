class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        arr = []

        for i in range(m):
            for j in range(n):
                arr.append(grid[i][j])

        length = len(arr)
        arr.sort()
        target = arr[length // 2]

        ans = 0
        for num in arr:
            if num % x != target % x:
                return -1

            ans += abs(num - target) // x

        return ans