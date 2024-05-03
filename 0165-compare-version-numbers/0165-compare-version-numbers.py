class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        n1 = len(version1)
        n2 = len(version2)
        
        i, j = 0, 0
        while i < n1 and j < n2:
            a, b = int(version1[i]), int(version2[j])
            
            if a < b:
                return -1
            
            if a > b:
                return 1
            
            i += 1
            j += 1
            
        # check for the remaining
        while i < n1:
            a = int(version1[i])
            if a == 0:
                i += 1
            
            if a > 0:
                return 1
            
        while j < n2:
            b = int(version2[j])
            if b == 0:
                j += 1
                
            if b > 0:
                return -1
            
        return 0
            
        