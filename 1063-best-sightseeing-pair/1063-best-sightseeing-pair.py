class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        curr_max = values[0]
        ans = 0

        for i in range(1, n):
            curr_max -= 1 
            ans = max(ans, curr_max + values[i])
            curr_max = max(curr_max, values[i])

        return ans