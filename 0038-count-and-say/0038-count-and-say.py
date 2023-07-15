class Solution:
    def saySequence(self, say: str) -> str:
        if (len(say) == 1):
            return "1" + str(say)
        
        out = ""
        i = 0
        
        while (i < len(say)):
            char = say[i]
            count = 1

            j = i + 1
            while (j < len(say) and char == say[j]):
                count += 1
                j += 1

            out += str(count) + str(char)
            i = j

        return out
    
    def countAndSay(self, n: int) -> str:
        if (n == 1):
            return "1"
        
        return self.saySequence(self.countAndSay(n-1))
        
            
            