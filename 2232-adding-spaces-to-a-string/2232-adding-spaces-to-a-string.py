class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = [s[:spaces[0]], " "]
        for i in range(1, len(spaces)):
            result.append(s[spaces[i-1]:spaces[i]])
            result.append(" ")

        result.append(s[spaces[-1]:])

        return ''.join(result)