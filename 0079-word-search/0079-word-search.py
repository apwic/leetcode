class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word = list(word)
        m, n = len(board), len(board[0])
        move = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        candidate = []
        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0]:
                    candidate.append((row, col))

        def check(x, y, seen):
            return 0 <= x < m and 0 <= y < n and (x, y) not in seen

        def backtrack(x, y, curr=[],seen=[]):
            if curr == word:
                return True

            for dx, dy in move:
                new_x, new_y = x + dx, y + dy
                if check(new_x, new_y, seen):
                    curr.append(board[new_x][new_y])
                    seen.append((new_x, new_y))
                    if curr == word[:len(curr)]:
                        if backtrack(new_x, new_y, curr, seen):
                            return True
                    curr.pop()
                    seen.pop()

            return False

        for x, y in candidate:
            if backtrack(x, y, [board[x][y]], [(x, y)]):
                return True

        return False
                        