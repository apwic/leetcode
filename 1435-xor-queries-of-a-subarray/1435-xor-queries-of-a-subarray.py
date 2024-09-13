class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [0 for _ in range(n)]
        prefix[0] = arr[0]

        for i in range(1, n):
            prefix[i] = prefix[i-1] ^ arr[i]

        n_query = len(queries)
        ans = [0 for _ in range(n_query)]

        for i in range(n_query):
            l, r = queries[i]
            ans[i] = prefix[r] ^ prefix[l] ^ arr[l]

        return ans