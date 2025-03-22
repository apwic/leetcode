class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graphs = defaultdict(list)

        for a, b in edges:
            graphs[a].append(b)
            graphs[b].append(a)

        def dfs(vis, node, comp, edge):
            if comp[node]:
                return 0

            edge = 0
            vis[node] = 1
            comp[node] = 1

            for neighbor in graphs[node]:
                edge += 1
                edge += dfs(vis, neighbor, comp, edge)

            return edge

        ans = 0
        vis = [0] * n
        for node in range(n):
            if vis[node]:
                continue

            component = [0] * n
            total_edge = dfs(vis, node, component, 0) // 2
            total_comp = sum(component)

            if total_comp * (total_comp - 1) // 2 == total_edge:
                ans += 1

        return ans