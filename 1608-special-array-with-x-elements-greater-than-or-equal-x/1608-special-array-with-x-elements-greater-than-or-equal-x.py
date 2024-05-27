class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums = sorted(nums)
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        l, r = 0, len(nums)
        while l <= r:
            mid = (l + r) // 2
            count = 0
            for key in freq.keys():
                if key >= mid:
                    count += freq[key]

            if count == mid:
                return count

            if count > mid:
                l = mid + 1
            else:
                r = mid - 1

        return -1

