class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []

        def backtrack(arr=[]):
            if len(ans) == k:
                return

            if len(arr) > n:
                return

            if len(arr) == n:
                ans.append(arr[:])

            for ch in ["a", "b", "c"]:
                if arr and arr[-1] == ch:
                    continue

                arr.append(ch)
                backtrack(arr)
                arr.pop()

        backtrack()
        return "" if k > len(ans) else "".join(ans[-1])