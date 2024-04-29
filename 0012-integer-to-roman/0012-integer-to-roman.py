class Solution:
    def intToRoman(self, num: int) -> str:
        converter = [
            (1, "I"),
            (4, "IV"),
            (5, "V"),
            (9, "IX"),
            (10, "X"),
            (40, "XL"),
            (50, "L"),
            (90, "XC"),
            (100, "C"),
            (400, "CD"),
            (500, "D"),
            (900, "CM"),
            (1000, "M")
        ]
        
        i = len(converter) - 1
        ans = ""
        while num > 0:
            while num < converter[i][0]:
                i -= 1
                
            ans += converter[i][1]
            num -= converter[i][0]
            
        return ans