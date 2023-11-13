class Solution:
    def sortVowels(self, s: str) -> str:
        VOWEL = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowel = []
        
        for c in s:
            if c in VOWEL:
                vowel.append(c)
                
        vowel.sort()
        
        res = []
        i = 0
        for c in s:
            if c in VOWEL:
                res.append(vowel[i])
                i += 1
            else:
                res.append(c)
                
        return ''.join(res)