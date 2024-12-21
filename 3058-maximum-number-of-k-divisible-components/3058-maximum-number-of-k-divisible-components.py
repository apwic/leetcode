class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n < 2:
            return 1
            
        graphs = defaultdict(list)
        indegrees = defaultdict(int)

        for a, b in edges:
            graphs[a].append(b)
            graphs[b].append(a)
            indegrees[a] += 1
            indegrees[b] += 1

        # try to prune from the leaf
        queue = deque(node for node in range(n) if indegrees[node] == 1)
        ans = 0

        while queue:
            node = queue.popleft()
            indegrees[node] -= 1
            val = 0

            # if value divisible, then become component
            if values[node] % k == 0:
                ans += 1
            else:
                val = values[node]

            for neighbor in graphs[node]:
                if indegrees[neighbor] == 0:
                    continue

                indegrees[neighbor] -= 1
                values[neighbor] += val

                # became leaf add the leaf
                if indegrees[neighbor] == 1:
                    queue.append(neighbor)

        return ans