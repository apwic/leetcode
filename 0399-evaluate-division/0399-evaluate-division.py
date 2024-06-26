class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graphs = defaultdict(set)

        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]
            graphs[a].add((b, val))
            graphs[b].add((a, 1/val))

        ans = []
        for start, end in queries:
            queue = deque([(start, 1)])
            seen = set({start})
            curr = -1

            while queue:
                node, val = queue.popleft()

                if node == end:
                    if graphs[node]:
                        curr = val
                    break

                for neighbor, neighbor_val in graphs[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, val*neighbor_val))

            ans.append(curr)
        
        return ans