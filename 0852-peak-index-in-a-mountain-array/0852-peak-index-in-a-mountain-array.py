class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        found = False
        l = 0
        r = len(arr)-1
        
        while (not found):
            n = (l + r)//2
            mx = arr[n]
            
            if (arr[n-1] < mx and mx > arr[n+1]):
                found = True
            
            if (mx < arr[n-1]):
                r = n
                
            if (mx < arr[n+1]):
                l = n
                
        return n
            