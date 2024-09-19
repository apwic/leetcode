class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        ops = {
            '+': lambda x,y : x+y,
            '-': lambda x,y : x-y,
            '*': lambda x,y : x*y,
        }

        def compute(expr):
            if expr in memo:
                return memo[expr]

            result = []

            for i in range(len(expr)):
                if expr[i] in ops:
                    left = compute(expr[:i])
                    right = compute(expr[i+1:])

                    for l in left:
                        for r in right:
                            result.append(ops[expr[i]](l, r))

            # result is not a list, means single expression == number
            if not result:
                result.append(int(expr))

            memo[expr] = result
            return result

        return compute(expression)
