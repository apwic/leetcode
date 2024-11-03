class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n, n_goal = len(s), len(goal)

        if n != n_goal:
            return False

        for i, ch in enumerate(s):
            if ch != goal[0]:
                continue

            count = 0
            for j in range(n):
                if s[(i+j) % n] != goal[j]:
                    break
                count += 1

            if count == n:
                return True

        return False
