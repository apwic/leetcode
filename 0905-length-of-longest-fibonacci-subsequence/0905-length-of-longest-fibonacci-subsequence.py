class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        idx = {num: i for i, num in enumerate(arr)}
        dp = defaultdict(lambda: 2)
        ans = 0

        for i in range(2, n):
            for j in range(i):
                to_check = arr[i] - arr[j]
                if to_check in idx and idx[to_check] < j:
                    k = idx[to_check]
                    dp[(j, i)] = dp[(k, j)] + 1
                    ans = max(ans, dp[(j, i)])

        return ans if ans >= 3 else 0