class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graphs = defaultdict(set)

        for i, (a, b) in enumerate(edges):
            graphs[a].add((b, math.log(succProb[i])))
            graphs[b].add((a, math.log(succProb[i])))

        max_prob = {i: float('-inf') for i in graphs.keys()}
        max_prob[start_node] = 0
        queue = [[0, start_node]]

        while queue:
            val, node = heapq.heappop(queue)
            val = -val

            if node == end_node:
                return math.exp(val)

            for neighbor, prob in graphs[node]:
                new_prob = val + prob
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(queue, (-new_prob, neighbor)) 

        return 0.0