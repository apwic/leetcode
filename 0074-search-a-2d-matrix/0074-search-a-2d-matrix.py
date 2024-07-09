class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        l, r = 0, m-1
        if r > 0:
            while l <= r:
                mid = (l+r)//2
                if matrix[mid][0] == target:
                    return True
    
                if matrix[mid][0] > target:
                    r = mid-1
                else:
                    l = mid+1

        row = l-1
        l, r = 0, n-1
        mid = 0
        if r > 0:
            while l <= r:
                mid = (l+r)//2
                if matrix[row][mid] == target:
                    return True
    
                if matrix[row][mid] > target:
                    r = mid-1
                else:
                    l = mid+1

        return matrix[row][mid] == target