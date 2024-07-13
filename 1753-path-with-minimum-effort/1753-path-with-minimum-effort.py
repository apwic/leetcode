class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def check(effort):
            seen = {(0, 0)}
            stack = [(0, 0)]

            while stack:
                x, y = stack.pop()

                if x == m-1 and y == n-1:
                    return True

                for dx, dy in moves:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in seen:
                        if abs(heights[x][y] - heights[new_x][new_y]) <= effort:
                            seen.add((new_x, new_y))
                            stack.append((new_x, new_y))

            return False

        l = 0
        r = max(max(row) for row in heights)
        while l <= r:
            mid = (l + r)//2
            if check(mid):
                r = mid-1
            else:
                l = mid+1

        return l
