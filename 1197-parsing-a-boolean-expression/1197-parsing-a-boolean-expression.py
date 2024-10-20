class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def parse(expression):
            first = expression[0]
            if first == 'f':
                return False

            if first == 't':
                return True

            if first == '!':
                return parse_not(expression[2:-1])

            if first == '&':
                return parse_and(expression[2:-1])

            if first == '|':
                return parse_or(expression[2:-1])

        def parse_not(expression):
            return not parse(expression)

        def parse_or(expression):
            boolean = False
            for expr in split(expression):
                boolean = boolean or parse(expr)

            return boolean

        def parse_and(expression):
            boolean = True
            for expr in split(expression):
                boolean = boolean and parse(expr)

            return boolean

        def split(expression):
            stack = []
            start = 0
            result = []

            for i, expr in enumerate(expression):
                if expr == '(':
                    stack.append(expr)

                if expr == ')':
                    stack.pop()

                if expr == ',' and not stack:
                    result.append(expression[start:i])
                    start = i + 1

            result.append(expression[start:])
            return result

        return parse(expression)

                    
                    