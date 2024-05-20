class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        
        for i in range(1 << n):
            xor_sum = 0
            
            for j in range(n):
                if i & (1 << j):
                    xor_sum ^= nums[j]
                    
            ans += xor_sum
            
        return ans