class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def bfs(root = 0):
            queue = deque([(root, 0)])
            visited = set([root])

            while queue:
                node, distance = queue.popleft()

                if node == n-1:
                    return distance

                for neighbor in graphs[node]:
                    if neighbor in visited:
                        continue

                    visited.add(neighbor)
                    queue.append((neighbor, distance+1))

            return -1

        graphs = defaultdict(set)

        for i in range(n):
            graphs[i].add(i+1)

        res = []
        for a, b in queries:
            graphs[a].add(b)
            res.append(bfs())

        return res