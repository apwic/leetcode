class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digitSum(num):
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //= 10
            return digit_sum

        freq = [0] * 82 # Cover all sum 0 to 81
        ans = -1
        for num in nums:
            digit_sum = digitSum(num)
            val_sum = freq[digit_sum]
            if val_sum > 0:
                ans = max(ans, val_sum + num)

            freq[digit_sum] = max(val_sum, num)

        return ans
