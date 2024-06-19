class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(list)

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                    graph[j].append(i)

        seen = set()
        ans = 0

        def dfs(i):
            for node in graph[i]:
                if node not in seen:
                    seen.add(node)
                    dfs(node)

        for i in range(n):
            if i not in seen:
                ans += 1
                dfs(i)

        return ans
