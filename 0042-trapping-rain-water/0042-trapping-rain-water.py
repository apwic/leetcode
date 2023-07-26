class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        l_mx = 0
        r_mx = 0
        water = 0
        
        while (l < r):
            if (height[l] < height[r]):
                if (height[l] >= l_mx):
                    l_mx = height[l]
                else:
                    water += l_mx - height[l]
                l += 1
            else:
                if (height[r] >= r_mx):
                    r_mx = height[r]
                else:
                    water += r_mx - height[r]
                r -= 1
                
        return water