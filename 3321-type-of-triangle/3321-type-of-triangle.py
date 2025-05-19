class Solution:
    def triangleType(self, nums: List[int]) -> str:
        freq = Counter(nums)
        keys = len(freq.keys())

        if keys == 1:
            return "equilateral"
        
        sums = sum(nums)
        if sums - nums[0] > nums[0] and sums - nums[1] > nums[1] and sums - nums[2] > nums[2]:
            if keys == 2:
                return "isosceles"

            return "scalene"

        return "none"