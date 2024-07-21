class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits = list(map(int, digits))
        n = len(digits)

        if n == 0:
            return []

        letters = {
            2 : ["a", "b", "c"],
            3 : ["d", "e", "f"],
            4 : ["g", "h", "i"],
            5 : ["j", "k", "l"],
            6 : ["m", "n", "o"],
            7 : ["p", "q", "r", "s"],
            8 : ["t", "u", "v"],
            9 : ["w", "x", "y", "z"]
        }

        def backtrack(idx=0, path=[], ans=[]):
            if idx == n:
                ans.append(''.join(path))
                return ans

            for neighbor in letters[digits[idx]]:
                path.append(neighbor)
                ans = backtrack(idx+1, path, ans)
                path.pop()

            return ans

        return backtrack()