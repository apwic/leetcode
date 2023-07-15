class Solution:
    
    def checkRow(self, row: int, board: List[List[str]]):
        nums = {}
        
        for j in range(9):
            temp = board[row][j] 
            if (temp != '.'):
                if (nums.get(temp) != None):
                    return False
                else:
                    nums[temp] = 1
        
        return True
            
        
    def checkCol(self, col: int, board: List[List[str]]):
        nums = {}
        
        for i in range(9):
            temp = board[i][col] 
            if (temp != '.'):
                if (nums.get(temp) != None):
                    return False
                else:
                    nums[temp] = 1
        
        return True
    
    # Grid look like this:
    # 0 1 2
    # 3 4 5
    # 6 7 8
    def checkGrid(self, grid_row: int, grid_col: int, board: List[List[str]]):
        nums = {}
        
        row = grid_row * 3
        col = grid_col * 3
        
        for i in range(row, row+3):
            for j in range(col, col+3):
                temp = board[i][j]
                if (temp != '.'):
                    if (nums.get(temp) != None):
                        return False
                    else:
                        nums[temp] = 1

        return True
        
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            if (not self.checkRow(i, board)):
                return False
            
        for i in range(9):
            if (not self.checkCol(i, board)):
                return False
            
        for i in range(3):
            for j in range(3):
                if (not self.checkGrid(i, j, board)):
                    return False
                
        return True
            