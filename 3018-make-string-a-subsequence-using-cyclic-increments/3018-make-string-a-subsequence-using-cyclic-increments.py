class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        def increment(ch):
            if ch == 'z':
                return 'a'

            return chr(ord(ch) + 1)

        n1, n2 = len(str1), len(str2)

        if n2 > n1:
            return False

        i, j = 0, 0 
        
        while i < n1 and j < n2:
            if j == n2:
                return True

            if str2[j] == str1[i] or str2[j] == increment(str1[i]):
                i += 1
                j += 1
            else:
                i += 1

        if j == n2:
            return True
             
        return False