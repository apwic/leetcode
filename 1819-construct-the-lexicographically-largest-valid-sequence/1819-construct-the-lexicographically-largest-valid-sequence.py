class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        len_n = 2*n - 1
        ans = [0] * len_n
        vis = [0] * (n+1)

        def backtrack(i = 0):
            if i == len_n:
                return True

            if ans[i]:
                return backtrack(i + 1)

            for num in range(n, 0, -1):
                if vis[num]:
                    continue

                nxt = i + num if num > 1 else i

                if nxt >= len_n or ans[nxt] != 0:
                    continue

                ans[i] = ans[nxt] = num
                vis[num] = 1

                if backtrack(i + 1):
                    return True

                ans[i] = ans[nxt] = 0
                vis[num] = 0

            return False

        backtrack()
        return ans