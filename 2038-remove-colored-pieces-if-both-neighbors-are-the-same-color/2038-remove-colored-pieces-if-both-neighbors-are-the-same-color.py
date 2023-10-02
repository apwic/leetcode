class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        A, B = 0, 0
        count_A, count_B = 0, 0
        
        for char in colors:
            if char == 'A':
                count_A += 1
                A += max(0, count_A - 2)
                count_B = 0
            else:
                count_B += 1
                B += max(0, count_B - 2)
                count_A = 0
        
        return A > B
    