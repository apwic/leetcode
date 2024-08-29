class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        graphs = defaultdict(set)

        for i in range(n):
            graphs[i] = set()

            x1, y1 = stones[i]
            for j in range(n):
                if i == j:
                    continue

                x2, y2 = stones[j]
                if x1 == x2 or  y1 == y2:
                    graphs[i].add(j)
                    graphs[j].add(i)

        def dfs(node, l=0):
            if node in seen:
                return l

            l += 1
            seen.add(node)

            for neighbor in graphs[node]:
                l = max(l, dfs(neighbor, l))

            return l

        ans = []
        seen = set()
        for i in range(n):
            if i not in seen:
                ans.append(dfs(i))

        return sum(ans) - len(ans)