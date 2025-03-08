class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = n = len(blocks)
        l = w = 0
        for r in range(n):
            if blocks[r] == "W":
                w += 1
                
            if r-l+1 == k:
                ans = min(ans, w)

                if blocks[l] == "W":
                    w -= 1

                l += 1
            
        return ans