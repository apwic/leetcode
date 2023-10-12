class Solution:
    def reverseOnlyLetters(self, s: str) -> str:     
        s = [i for i in s]
        i, j  = 0, len(s) - 1
        while (i < j):
            i_s = s[i].isalpha()
            j_s = s[j].isalpha()
            if (i_s and j_s):
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            
            if (not i_s):
                i += 1
            
            if (not j_s):
                j -= 1
            
        return ''.join(s)
        
        
        