class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graphs = defaultdict(set)
        roads = defaultdict(set)

        for conn in connections:
            a, b = conn
            graphs[a].add(b)
            roads[a].add(b)
            roads[b].add(a)

        self.ans = 0
        seen = {0}

        def dfs(node):
            for neighbor in roads[node]:
                if neighbor not in seen:
                    if neighbor in graphs[node]:
                        self.ans += 1

                    seen.add(neighbor)
                    dfs(neighbor)

        dfs(0)
        return self.ans
        