class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        heap = arr[:]
        heapq.heapify(heap)
        freq = defaultdict(int)

        rank = 1
        while heap:
            num = heapq.heappop(heap)
            if not freq[num]:
                freq[num] = rank
                rank += 1

        ans = []
        for num in arr:
            ans.append(freq[num])

        return ans