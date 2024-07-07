class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        MAX_WEIGHT = 5000
        weight.sort()

        ans = 0
        for w in weight:
            if MAX_WEIGHT - w >= 0:
                MAX_WEIGHT -= w
                ans += 1
            else:
                return ans

        return ans