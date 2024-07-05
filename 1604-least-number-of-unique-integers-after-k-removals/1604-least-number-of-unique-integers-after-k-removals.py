class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freqs = defaultdict(int)

        for num in arr:
            freqs[num] += 1

        heaps = [(val, key) for key, val in freqs.items()]
        heapq.heapify(heaps)

        while k:
            val, key = heapq.heappop(heaps)
            to_reduce = min(k, val)
            freqs[key] -= to_reduce
            k -= to_reduce

            if freqs[key]:
                heapq.heappush(heaps, (key, freqs[key]))

        return len(heaps)