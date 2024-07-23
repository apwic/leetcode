class Solution:
    def totalNQueens(self, n: int) -> int:
        def check(board):
            n_board = len(board)
            for i in range(n_board):
                for j in range(n_board):
                    if i == j:
                        continue

                    # Horizontal
                    if board[i] == board[j]:
                        return False

                    # Diagonal
                    if abs(i - j) == abs(board[i] - board[j]):
                        return False

            return True

        def backtrack(col=0, board=[], ans=0):
            if col == n:
                return ans + 1

            for row in range(n):
                board.append(row)
                if check(board):
                    ans = backtrack(col+1, board, ans)
                board.pop()

            return ans

        return backtrack()        