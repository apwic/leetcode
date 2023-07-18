class Solution:
    def area(self, height, p, q):
        return (q - p) * min(height[p], height[q])
    
    def maxArea(self, height: List[int]) -> int:
        n = len(height) - 1
        p = 0
        q = n
        max_area = self.area(height, p, q)
        
        while (p < q):
            if (height[p] < height[q]):
                p += 1
            else:
                q -= 1
                
            temp_area = self.area(height, p, q)
            if (temp_area > max_area):
                max_area = temp_area
            
        return max_area
            
                