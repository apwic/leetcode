class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []

        for c in s:
            if c == '#':
                if stack_s: 
                    stack_s.pop()
            else:
                stack_s.append(c)

        stack_t = []

        for c in t:
            if c == '#':
                if stack_t:  
                    stack_t.pop()
            else:
                stack_t.append(c)

        return stack_s == stack_t                
