class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        
        def binSearchRow(row, target):
            l = 0
            r = len(row) - 1
            mid = 0
            
            while l <= r:
                mid = l + (r-l)//2
                
                if (target == row[mid]):
                    return True
                
                if (target < row[mid]):
                    r = mid - 1
                
                if (target > row[mid]):
                    l = mid + 1
        
        l = 0
        r = m
        
        while l <= r:
            mid = l + (r-l)//2
            
            if (matrix[mid][0] <= target and target <= matrix[mid][-1]):
                return binSearchRow(matrix[mid], target)
            
            if (target < matrix[mid][0]):
                r = mid - 1
                
            if (target > matrix[mid][-1]):
                l = mid + 1 
                
        return False    
        
            
            
                
            
                
        