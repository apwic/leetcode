class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graphs = defaultdict(list)

        def checkCycle(visited, node, parent):
            visited.add(node)

            for neighbor in graphs[node]:
                if neighbor not in visited:
                    if checkCycle(visited, neighbor, node) :
                        return True
                elif neighbor != parent:
                    return True

            return False

        for a, b in edges:
            graphs[a].append(b)
            graphs[b].append(a)

            visited = set()
            if checkCycle(visited, a, b):
                return [a, b]