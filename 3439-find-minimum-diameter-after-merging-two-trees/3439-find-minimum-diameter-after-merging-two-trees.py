class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def createGraph(edges):
            graphs = defaultdict(list)
            
            for a, b in edges:
                graphs[a].append(b)
                graphs[b].append(a)

            return graphs

        def DFS(graphs, node, parent):
            # depth1 > depth2
            depth1 = depth2 = 0
            diameter = 0

            for neighbor in graphs[node]:
                if neighbor == parent:
                    continue

                child_dia, depth = DFS(graphs, neighbor, node)
                depth += 1
                diameter = max(diameter, child_dia)

                if depth > depth1:
                    depth1, depth2 = depth, depth1
                elif depth > depth2:
                    depth2 = depth

                diameter = max(diameter, depth1 + depth2)
                
            return diameter, depth1

        # find maximum length
        def findLength(edges):
            if len(edges) <= 1:
                return len(edges)

            graphs = createGraph(edges)
            length, _ = DFS(graphs, 0, -1)

            return length

        len1 = findLength(edges1)
        len2 = findLength(edges2)
        combined = ceil(len1/2) + ceil(len2/2) + 1

        return max(len1, len2, combined)
