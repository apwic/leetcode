class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        mx, idx = 0, 0

        for i, row in enumerate(grid):
            temp = sum(row)
            if temp > mx:
                mx = temp
                idx = i

        return idx
