class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        cliffs = []
        for i in range(1, len(nums)):
            cliffs.append(nums[i] - nums[i-1])
        
        cliffs.append(nums[0] - nums[n-1])

        ans = 0
        for cliff in cliffs:
            ans += 1 if cliff < 0 else 0

        return ans <= 1