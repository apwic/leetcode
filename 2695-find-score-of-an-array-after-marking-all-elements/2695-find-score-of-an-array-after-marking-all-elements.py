class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)

        marked = [False] * n
        nums = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(nums)

        ans = 0
        while nums:
            num, idx = heapq.heappop(nums)
            if marked[idx]:
                continue

            ans += num
            if idx - 1 >= 0:
                marked[idx-1] = True

            if idx + 1 < n:
                marked[idx+1] = True

        return ans