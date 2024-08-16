class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m = len(arrays)
        mn, mx = arrays[0][0], arrays[0][-1]
        ans = 0

        for i in range(1, m):
            curr_mn, curr_mx = arrays[i][0], arrays[i][-1]

            ans = max(ans, abs(curr_mn - mx), abs(curr_mx - mn))
            mn = min(mn, curr_mn)
            mx = max(mx, curr_mx)

        return ans