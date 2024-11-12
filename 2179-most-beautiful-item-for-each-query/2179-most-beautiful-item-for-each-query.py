class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(items), len(queries)
        queries_idx = [[queries[i], i] for i in range(n)]

        items.sort()
        queries_idx.sort()

        ans = [0] * n
        i = 0
        mx = 0
        for query, j in queries_idx:
            while i < m and items[i][0] <= query:
                mx = max(mx, items[i][1])
                i += 1

            ans[j] = mx

        return ans
