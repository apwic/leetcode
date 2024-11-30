class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graphs = defaultdict(deque)
        indegree, outdegree = defaultdict(int), defaultdict(int)

        for a, b in pairs:
            graphs[a].append(b)
            outdegree[a] += 1
            indegree[b] += 1


        def dfs(node):
            while graphs[node]:
                neighbor = graphs[node].popleft()
                dfs(neighbor)

            result.append(node)

        start = -1
        for node in outdegree:
            if outdegree[node] == indegree[node] + 1:
                start = node
                break

        if start == -1:
            start = pairs[0][0]

        result = []
        dfs(start)

        result.reverse()

        return [[result[i-1], result[i]] for i in range(1, len(result))]