class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graphs = defaultdict(set)

        for a, b in edges:
            graphs[a].add(b)
            graphs[b].add(a)
            
        def dfs(node):
            if node not in seen:
                seen.add(node)

                for neighbor in graphs[node]:
                    dfs(neighbor)

        seen = set()
        ans = 0

        for node in range(n):
            if node not in seen:
                ans += 1
                dfs(node)

        return ans