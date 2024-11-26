class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graphs = defaultdict(set)
        roots = set([i for i in range(n)])

        for a, b in edges:
            roots.add(a)
            graphs[a].add(b)

        def dfs(node, visited):
            for neighbor in graphs[node]:
                if neighbor in visited:
                    continue

                visited.add(node)
                roots.discard(neighbor)
                dfs(neighbor, visited)

        temp = roots.copy()
        for node in temp:
            if node in roots:
                dfs(node, set())

        if len(roots) == 1:
            for root in roots:
                return root

        return -1