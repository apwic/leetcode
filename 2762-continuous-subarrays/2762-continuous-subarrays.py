class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        min_heap = []
        max_heap = []
        l = r = 0
        ans = 0

        for r in range(n):
            heapq.heappush(min_heap, (nums[r], r))
            heapq.heappush(max_heap, (-nums[r], r))

            # shrink windows if condition is violated
            while l < r and -max_heap[0][0] - min_heap[0][0] > 2:
                l += 1

                # delete from heap if index is outside
                while min_heap and min_heap[0][1] < l:
                    heapq.heappop(min_heap)
                while max_heap and max_heap[0][1] < l:
                    heapq.heappop(max_heap)

            ans += r - l + 1

        return ans