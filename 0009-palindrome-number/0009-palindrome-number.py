from math import log, floor

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False

        if (x == 0):
            return True
            
        digits = 10 ** (floor(log(x, 10)))
        new_x = 0
        temp_x = x

        while (temp_x > 0):
            rem = temp_x % 10
            temp_x = (temp_x - rem) / 10
            new_x += rem * digits
            digits /= 10

        if (new_x == x):
            return True

        return False