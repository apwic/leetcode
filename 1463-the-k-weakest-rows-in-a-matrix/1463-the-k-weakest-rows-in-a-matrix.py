class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = [(sum(row), i) for i, row in enumerate(mat)]
        heapq.heapify(soldiers)

        ans  = []
        while k:
            _, idx = heapq.heappop(soldiers)
            ans.append(idx)
            k -= 1

        return ans
    