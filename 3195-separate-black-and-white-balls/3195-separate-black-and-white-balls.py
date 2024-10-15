class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        black = [i for i in range(n) if s[i] == "1"]
        k = len(black)
        
        ans = 0
        for i in range(k):
            # using the n-1 as a pivot of the actual dist
            actual = n-1 - black[i]
            # k-1 as a pivot of the distance between black ball
            black_dist = k-1 - i
            # swap needed can be calculated by the actual - black_dist
            ans += actual - black_dist

        return ans
