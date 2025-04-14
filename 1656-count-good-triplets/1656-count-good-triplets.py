class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        def check(i , j, k):
            if abs(arr[i] - arr[j]) > a:
                return False

            if abs(arr[j] - arr[k]) > b:
                return False

            if abs(arr[i] - arr[k]) > c:
                return False

            return True

        ans = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if not check(i, j, k):
                        continue

                    ans += 1

        return ans
