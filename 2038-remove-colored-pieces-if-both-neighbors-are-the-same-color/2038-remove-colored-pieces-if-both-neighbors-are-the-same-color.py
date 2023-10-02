class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        def countMoves(s: str, turn: str) -> int:
            count, total = 0, 0
            for char in s:
                if char == turn:
                    count += 1
                    total += max(0, count - 2)
                else:
                    count = 0
            return total

        A_moves = countMoves(colors, 'A')
        B_moves = countMoves(colors, 'B')
        
        return A_moves > B_moves
    