class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pc = [[1]]
        
        for i in range(1, rowIndex + 1):
            prev = pc[-1]
            nxt = [1]
            
            for j in range(1, len(prev)):
                nxt.append(prev[j-1] + prev[j])
            
            nxt.append(1)
            pc.append(nxt)
            
        return pc[rowIndex]