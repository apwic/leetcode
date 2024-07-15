class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (l+r)//2
            if mid*mid >= x:
                r = mid-1
            else:
                l = mid+1

        return l if l*l == x else l-1
        