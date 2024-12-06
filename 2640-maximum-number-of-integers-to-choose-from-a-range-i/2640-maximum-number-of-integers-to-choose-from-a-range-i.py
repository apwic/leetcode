class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        ans = 0
        curr = 0

        for i in range(1, n+1):
            if i not in banned and curr + i <= maxSum:
                curr += i
                ans += 1

            if curr + i > maxSum:
                break

        return ans