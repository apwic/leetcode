class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        bitCount = [0] * 32
        n = len(nums)
        curr = 0
        l = 0
        result = float('inf')

        for r in range(n):
            curr |= nums[r]

            for bit in range(32):
                if nums[r] & (1 << bit):
                    bitCount[bit] += 1

            while curr >= k and l <= r:
                result = min(result, r-l+1)
                update = 0

                # undo the OR
                for bit in range(32):
                    if nums[l] & (1 << bit):
                        bitCount[bit] -= 1
                    if bitCount[bit] > 0:
                        update |= (1 << bit)

                curr = update
                l += 1

        return result if result != float('inf') else -1
        