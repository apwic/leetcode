class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(idx=1, curr=[], ans=[]):
            if len(curr) == k and sum(curr) == n:
                ans.append(curr[:])
                return ans

            for num in range(idx, 10):
                curr.append(num)
                backtrack(num+1, curr, ans)
                curr.pop()

            return ans

        return backtrack()