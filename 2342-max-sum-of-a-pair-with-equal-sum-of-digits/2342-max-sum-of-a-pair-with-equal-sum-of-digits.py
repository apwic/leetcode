class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        freq = {}
        ans = -1
        
        for num in nums:
            digit_sum = list(str(num))
            digit_sum = sum([int(el) for el in digit_sum])
            
            if digit_sum in freq:
                val = freq[digit_sum]
                ans = max(ans, num + val)
                freq[digit_sum] = max(num, val)
            else:
                freq[digit_sum] = num
                
        return ans