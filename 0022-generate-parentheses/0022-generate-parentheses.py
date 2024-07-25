class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(start=n, end=n, curr=[], ans=[]):
            if start == 0 and end == 0:
                ans.append("".join(curr))
                return ans

            if start:
                curr.append("(")
                backtrack(start-1, end, curr, ans)
                curr.pop()
                
            if end - start > 0:
                curr.append(")")
                backtrack(start, end-1, curr, ans)
                curr.pop()

            return ans

        return backtrack()