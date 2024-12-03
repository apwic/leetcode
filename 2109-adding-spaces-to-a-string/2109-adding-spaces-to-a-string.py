class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        for idx, space in enumerate(spaces):
            s = s[:idx+space] + " " + s[idx+space:]

        return s