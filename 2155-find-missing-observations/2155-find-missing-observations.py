class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        missing = mean * (m+n) - sum(rolls)
        true_avg = missing / n

        if not (1 <= true_avg <= 6):
            return []

        avg, rem = missing // n, missing % n
        ans = [avg] * n

        for i in range(rem):
            ans[i] += 1

        return ans