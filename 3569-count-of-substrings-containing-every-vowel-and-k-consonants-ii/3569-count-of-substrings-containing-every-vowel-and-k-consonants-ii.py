class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        def isVowel(c):
            return c in ["a", "i", "u", "e", "o"]

        def minK(k):
            res = 0
            start = end = 0
            vowel = {}
            cons = 0

            while end < n:
                curr = word[end]

                if isVowel(curr):
                    vowel[curr] = vowel.get(curr, 0) + 1
                else:
                    cons += 1
                    
                while len(vowel) == 5 and cons >= k:
                    res += n - end
                    start_ch = word[start]
                    if isVowel(start_ch):
                        vowel[start_ch] = vowel.get(start_ch) - 1
                        if vowel.get(start_ch) == 0:
                            vowel.pop(start_ch)
                    else:
                        cons -= 1
                    start += 1
                
                end += 1

            return res

        return minK(k) - minK(k+1)