class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ans = 0
        search = True
        text = list(text)
        
        while search:
            word = list("balloon")
            count = 0
            for ch in word:
                if ch in text:
                    text.remove(ch)
                    count += 1
                else:
                    search = False
                    
            if count == len(word):
                ans += 1
                    
        return ans