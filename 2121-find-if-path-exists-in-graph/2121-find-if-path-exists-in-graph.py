class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graphs = defaultdict(set)

        for a, b in edges:
            graphs[a].add(b)
            graphs[b].add(a)
            
        self.found = False

        def dfs(node):
            if node == destination:
                self.found = True

            if node not in seen:
                seen.add(node)
                for neighbor in graphs[node]:
                    dfs(neighbor)

        seen = set()
        dfs(source)

        return self.found
