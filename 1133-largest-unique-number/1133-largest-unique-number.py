class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        from collections import defaultdict
        
        freq = defaultdict(int)
        
        for num in nums:
            freq[num] += 1
            
        largest = -1
        for key, val in freq.items():
            if val > 1:
                continue
            
            if key > largest:
                largest = key
                
        return largest