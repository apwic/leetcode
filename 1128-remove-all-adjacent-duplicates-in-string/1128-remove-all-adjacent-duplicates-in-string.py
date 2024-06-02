class Solution:
    def removeDuplicates(self, s: str) -> str:
        s = list(s)
        stack = [s[0]]
        i = 1

        while i < len(s):
            if stack and stack[-1] == s[i]:
                # remove adjacent
                s.pop(i-1)
                s.pop(i-1)
                # remove current stack
                stack.pop()
                i -= 1
            else:
                stack.append(s[i])
                i += 1

        return ''.join(s)