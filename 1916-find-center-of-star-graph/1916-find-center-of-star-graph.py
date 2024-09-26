class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graphs = defaultdict(set)

        for a, b in edges:
            graphs[a].add(b)
            graphs[b].add(a)

        n = len(graphs.keys())

        for key in graphs.keys():
            if len(graphs[key]) == n-1:
                return key

        return -1