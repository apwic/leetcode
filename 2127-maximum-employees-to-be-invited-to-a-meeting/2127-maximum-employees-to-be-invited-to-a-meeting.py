class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indegree = [0] * n

        for node in range(n):
            indegree[favorite[node]] += 1

        pq = deque()
        for node in range(n):
            if indegree[node] == 0:
                pq.append(node)

        depth = [1] * n

        while pq:
            node = pq.popleft()
            nxt = favorite[node]
            depth[nxt] = max(depth[nxt], depth[node] + 1)
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                pq.append(nxt)

        cycle1 = 0
        cycle2 = 0

        for node in range(n):
            if indegree[node] == 0:
                continue

            curr_length = 0
            curr_node = node
            while indegree[curr_node] != 0:
                indegree[curr_node] = 0
                curr_length += 1
                curr_node = favorite[curr_node]

            if curr_length == 2:
                cycle2 += depth[node] + depth[favorite[node]]
            else:
                cycle1 = max(cycle1, curr_length)

        return max(cycle1, cycle2)
            