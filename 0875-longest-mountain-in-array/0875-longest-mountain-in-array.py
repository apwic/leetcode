class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        LIS, LDS = [1] * n, [1] * n

        for i in range(1, n):
            if arr[i] > arr[i-1]:
                LIS[i] = LIS[i-1] + 1

        for i in range(n-2, -1, -1):
            if arr[i] > arr[i+1]:
                LDS[i] = LDS[i+1] + 1

        ans = 0
        for i in range(n):
            if LIS[i] > 1 and LDS[i] > 1:
                ans = max(ans, LIS[i] + LDS[i] - 1) 

        return ans