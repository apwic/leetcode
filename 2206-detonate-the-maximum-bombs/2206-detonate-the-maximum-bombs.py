class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graphs = defaultdict(set)
        n = len(bombs)

        def in_radius(x, y, r, a, b):
            return (x-a)**2 + (y-b)**2 <= r*r

        for i in range(n):
            x, y, r = bombs[i]
            for j in range(n):
                a, b, _ = bombs[j]
                if i == j:
                    continue

                if in_radius(x, y, r, a, b):
                    graphs[i].add(j)

        def dfs(node, seen):
            seen.add(node)
            for neighbor in graphs[node]:
                if neighbor not in seen:
                    dfs(neighbor, seen)

            return len(seen)

        ans = 0
        for i in range(n):
            seen = set()
            ans = max(ans, dfs(i, seen))

        return ans
            