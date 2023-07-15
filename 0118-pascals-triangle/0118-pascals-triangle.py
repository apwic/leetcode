class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        
        for i in range(1, numRows):
            p = [1]
            for j in range(0, len(pascal[i-1]) - 1):
                p.append(pascal[i-1][j] + pascal[i-1][j+1])
                
            p.append(1)
            pascal.append(p)
            
        return pascal