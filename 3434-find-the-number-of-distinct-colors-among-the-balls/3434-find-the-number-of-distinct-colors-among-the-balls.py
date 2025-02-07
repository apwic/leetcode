class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n = len(queries)
        ans = []
        colors = {}
        balls = {}

        for i in range(n):
            ball, color = queries[i]

            if ball in balls:
                prev_color = balls[ball]
                colors[prev_color] -= 1

                if colors[prev_color] == 0:
                    del colors[prev_color]

            balls[ball] = color
            colors[color] = colors.get(color, 0) + 1
            ans.append(len(colors))

        return ans 