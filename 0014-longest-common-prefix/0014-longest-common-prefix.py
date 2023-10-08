class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pr = ""
        i = 0
        f = True
        
        while f:
            j = 0
            
            if (len(strs[j]) - 1 < i):
                return pr
            
            temp = strs[j][i]
            
            while j < len(strs):
                if (len(strs[j]) - 1 < i):
                    return pr
                
                if (temp == strs[j][i]):
                    j += 1
                    continue
                else:
                    break
            
            if j == len(strs):
                pr += temp
            else:
                return pr
            
            i += 1