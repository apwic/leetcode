class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
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

        def board_maker(board):
            result = []
            for col in board:
                row = ["."] * n
                row[col] = "Q"
                result.append(''.join(row))

            return result

        def backtrack(col=0, board=[], ans=[]):
            if col == n:
                ans.append(board_maker(board))
                return ans

            for row in range(n):
                board.append(row)
                if check(board):
                    ans = backtrack(col+1, board, ans)
                board.pop()

            return ans

        return backtrack()         