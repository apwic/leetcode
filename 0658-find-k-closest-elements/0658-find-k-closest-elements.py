class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = [(-abs(num-x), -num) for num in arr]
        print(heap)
        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)

        return sorted([-num for _, num in heap])
        