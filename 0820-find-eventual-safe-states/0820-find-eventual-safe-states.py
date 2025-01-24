class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = [[] for _ in range(n)]
        indegree = [0] * n

        for a in range(n):
            for b in graph[a]:
                reverse_graph[b].append(a)
            indegree[a] = len(graph[a])

        queue = deque([i for i in range(n) if indegree[i] == 0])
        safe = [0] * n

        while queue:
            node = queue.popleft()
            safe[node] = 1
            for neighbor in reverse_graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return [i for i in range(n) if safe[i] == 1]