class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(curr):
            start, end = curr, curr
            steps = 0

            while start <= n:
                steps += min(n+1, end+1) - start
                start = start * 10
                end = end * 10 + 9

            return steps

        curr = 1
        k -= 1

        while k > 0:
            steps = count(curr)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1

        return curr