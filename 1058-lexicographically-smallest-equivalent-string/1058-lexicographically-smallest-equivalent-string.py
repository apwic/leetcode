class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graphs = defaultdict(set)
        for a, b in zip(s1, s2):
            graphs[a].add(b)
            graphs[b].add(a)

        visited = defaultdict(int)
        mapSmallest = {}

        def dfs(node, group):
            visited[node] = 1
            group.append(node)
            for neighbor in graphs[node]:
                if not visited[neighbor]:
                    dfs(neighbor, group)

        for ch in set(s1 + s2):
            if not visited[ch]:
                group = []
                dfs(ch, group)
                smallest = min(group)
                for member in group:
                    mapSmallest[member] = smallest

        return "".join(mapSmallest.get(ch, ch) for ch in baseStr)