class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graphs = defaultdict(set)

        for edge in edges:
            a, b = edge
            graphs[a].add(b)

        nodes = set([num for num in range(n)])
        keys = list(graphs.keys())
            
        for key in keys:
            for neighbor in graphs[key]:
                if neighbor in nodes:
                    nodes.remove(neighbor)

        return nodes