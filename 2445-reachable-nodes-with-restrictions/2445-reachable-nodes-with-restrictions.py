class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graphs = defaultdict(set)
        restricted = set(restricted)

        for a, b in edges:
            graphs[a].add(b)
            graphs[b].add(a)

        def dfs(node):
            if node in restricted:
                return 

            if node not in seen:
                seen.add(node)
                for neighbor in graphs[node]:
                    dfs(neighbor)

        seen = set()
        dfs(0)
        return len(seen)