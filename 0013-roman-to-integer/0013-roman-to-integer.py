class Solution:
    def romanToInt(self, s: str) -> int:
        converter = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        s = [converter[char] for char in s]
        ans = 0
        i = 0
        while i < len(s) - 1:
            if s[i] < s[i+1]:
                ans += s[i+1] - s[i]
                i += 2
            else:
                ans += s[i]
                i += 1

        if i < len(s):
            ans += s[-1]
            
        return ans