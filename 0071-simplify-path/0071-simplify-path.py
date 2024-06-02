class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []

        for p in path:
            if p == '' or p == '.':
                continue

            if p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)

        if stack:
            return '/' + '/'.join(stack)
        else:
            return '/'