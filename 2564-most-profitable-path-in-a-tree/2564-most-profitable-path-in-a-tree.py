class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges)
        graphs = defaultdict(list)

        for a, b in edges:
            graphs[a].append(b)
            graphs[b].append(a)

        bob_path = {}
        vis = [0] * (n+1)

        def Bob(curr, dist):
            if vis[curr]:
                return False

            vis[curr] = 1
            bob_path[curr] = dist

            if curr == 0:
                return True

            for neighbor in graphs[curr]:
                if Bob(neighbor, dist+1):
                    return True

            bob_path.pop(curr, None)
            return False

        Bob(bob, 0)

        vis = [0] * (n+1)
        self.ans = float("-inf")

        def Alice(curr, dist, income):
            if vis[curr]:
                return
            vis[curr] = 1

            # Alice reaches node first
            if curr not in bob_path or dist < bob_path[curr]:
                income += amount[curr] 
            # reach node at the same time
            elif dist == bob_path[curr]:
                income += amount[curr] // 2

            # update if reaches leaf
            if len(graphs[curr]) == 1 and curr != 0:
                self.ans = max(self.ans, income)

            for neighbor in graphs[curr]:
                Alice(neighbor, dist+1, income)

        Alice(0, 0, 0)
        return self.ans
        