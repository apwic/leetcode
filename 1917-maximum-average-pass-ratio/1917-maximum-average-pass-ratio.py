class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p, t):
            return p/t - (p+1)/(t+1) 
            
        heap = [(gain(p, t), p, t) for p, t in classes]
        heapify(heap)

        for _ in range(extraStudents):
            _, p, t = heappop(heap)
            heappush(heap, (gain(p+1, t+1), p+1, t+1))

        return sum(p/t for _, p, t in heap) / len(classes)