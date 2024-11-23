class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        def addToRotated(stone, row, col):
            for i in range(col-stone, col):
                rotated[i][m-row-1] = '#'

        m, n = len(box), len(box[0])
        rotated = [['.' for _ in range(m)] for _ in range(n)]

        for row in range(m):
            stone = 0
            for col in range(n):
                if box[row][col] == '#':
                    stone += 1
                    continue

                if box[row][col] == '*':
                    rotated[col][m-row-1] = '*'
                    addToRotated(stone, row, col)
                    stone = 0

            if stone:
                addToRotated(stone, row, col+1)

        return rotated