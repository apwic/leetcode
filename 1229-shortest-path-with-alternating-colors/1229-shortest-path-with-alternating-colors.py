class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        blueGraphs = defaultdict(set)
        redGraphs = defaultdict(set)

        for a, b in blueEdges:
            blueGraphs[a].add(b)

        for a, b in redEdges:
            redGraphs[a].add(b)

        ans = [-1 for _ in range(n)]
        queue = deque([(0, "r", 0), (0, "b", 0)])
        seen = set({(0, "r"), (0, "b")})

        while queue:
            node, color, dist = queue.popleft()
            ans[node] = min(dist, ans[node]) if ans[node] != -1 else dist

            if color == "b":
                graphs = blueGraphs
                nextColor = "r"
            else:
                graphs = redGraphs
                nextColor = "b"

            for neighbor in graphs[node]:
                if (neighbor, nextColor) not in seen:
                    seen.add((neighbor, nextColor))
                    queue.append((neighbor, nextColor, dist+1))

        return ans