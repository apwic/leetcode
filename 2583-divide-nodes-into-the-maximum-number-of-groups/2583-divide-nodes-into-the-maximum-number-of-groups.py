class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graphs = [[] for _ in range(n+1)]
        for a, b in edges:
            graphs[a].append(b)
            graphs[b].append(a)

        def check(vis, start):
            pq = deque([start])
            vis[start] = 1

            while pq:
                node = pq.popleft()
                for neighbor in graphs[node]:
                    if not vis[neighbor]:
                        vis[neighbor] = -1 * vis[node]
                        pq.append(neighbor)
                    elif vis[neighbor] == vis[node]:
                        return False

            return True

        def bipartite():
            vis = [0] * (n+1)
            for node in range(1, n+1):
                if vis[node] == 0 and not check(vis, node):
                    return False

            return True

        def bfs(start):
            pq = deque([start])
            vis = [0] * (n+1)
            vis[start] = 1
            level = 0

            while pq:
                num = len(pq)
                for _ in range(num):
                    node = pq.popleft()
                    for neighbor in graphs[node]:
                        if not vis[neighbor]:
                            vis[neighbor] = 1
                            pq.append(neighbor)

                level += 1

            return level

        def maxLevel(vis, start):
            pq = deque([start])
            vis[start] = 1
            ans = 0

            while pq:
                node = pq.popleft()
                ans = max(ans, dist[node])
                for neighbor in graphs[node]:
                    if not vis[neighbor]:
                        vis[neighbor] = 1
                        pq.append(neighbor)

            return ans

        if not bipartite():
            return -1

        dist = [0] * (n+1)
        for node in range(1, n+1):
            dist[node] = bfs(node)

        ans = 0
        vis = [0] * (n+1)
        for node in range(1, n+1):
            if not vis[node]:
                ans += maxLevel(vis, node)

        return ans