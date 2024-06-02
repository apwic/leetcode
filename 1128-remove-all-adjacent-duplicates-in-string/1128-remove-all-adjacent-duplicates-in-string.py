class Solution:
    def removeDuplicates(self, s: str) -> str:
        s = list(s)
        stack = []
        
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)