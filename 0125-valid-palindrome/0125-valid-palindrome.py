class Solution:
    import re
    def isPalindrome(self, s: str) -> bool:
        word = re.sub('[^a-z0-9]+', '', s.lower())
        return word == word[::-1]