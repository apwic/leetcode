class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        pq = []
        start, end = 0, float('inf')
        max_val = float('-inf')

        for i in range(k):
            heapq.heappush(pq, (nums[i][0], i, 0))
            max_val = max(max_val, nums[i][0])

        # loop until one of the list is exhausted
        # couldn't add anymore to the pq
        while len(pq) == k:
            min_val, list_idx, el_idx = heapq.heappop(pq)

            if max_val - min_val < end - start:
                start = min_val
                end = max_val

            if el_idx + 1 < len(nums[list_idx]):
                next_val = nums[list_idx][el_idx + 1]
                heapq.heappush(pq, (next_val, list_idx, el_idx + 1))
                max_val = max(max_val, next_val)

        return [start, end]