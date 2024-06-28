class Solution:
    import heapq
    def halveArray(self, nums: List[int]) -> int:
        sums = sum(nums)
        nums = [-num for num in nums]
        heapq.heapify(nums)

        curr_sums = sums
        half_sums = sums/2
        ans = 0
        while curr_sums > half_sums:
            max_num = heapq.heappop(nums)
            heapq.heappush(nums, max_num/2)
            curr_sums += max_num/2
            ans += 1

        return ans