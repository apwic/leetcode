class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mx = 0
        prefix = [0]
        
        for i in range(len(gain)):
            mx = max(mx, prefix[-1])
            prefix.append(prefix[i] + gain[i]) 
            
        return max(mx, prefix[-1])
        