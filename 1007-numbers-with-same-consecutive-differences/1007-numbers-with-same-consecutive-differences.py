class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def valid(curr):
            # Leading zeros
            if curr[0] == 0:
                return False

            for i in range(1, len(curr)):
                a, b = curr[i-1], curr[i]
                if abs(a-b) != k:
                    return False

            return True

        def backtrack(curr=[], ans=[]):
            if len(curr) == n:
                str_curr = map(str, curr)
                ans.append(int("".join(str_curr)))
                return ans

            for num in range(0, 10):
                curr.append(num)
                if valid(curr):
                    backtrack(curr, ans)
                curr.pop()

            return ans

        return backtrack()
