class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        step = [0] * n
        
        for i in range(n-2, -1, -1):
            j = nums[i]
            if (i + j >= n-1):
                step[i] = 1
            else:
                reach = [step[i+k] for k in range(1, j+1) if i+k < n]
                step[i] = min(reach) + 1 if len(reach) > 0 else 10**4
                
        return step[0]
            