class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p, t):
            return (p+1)/(t+1) - p/t
            
        heap = [(-gain(p, t), p, t) for p, t in classes]

        for _ in range(extraStudents):
            diff, p, t = heapq.heappop(heap)
            diff = gain(p+1, t+1)
            heapq.heappush(heap, (-diff, p+1, t+1))

        return sum([p/t for _, p, t in heap]) / len(classes)