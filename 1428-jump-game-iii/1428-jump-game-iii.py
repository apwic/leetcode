class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        graphs = defaultdict(set)
        targets = set()

        for i in range(n):
            if arr[i] == 0:
                targets.add(i) 
            if i - arr[i] >= 0:
                graphs[i].add(i - arr[i])
            if i + arr[i] < n:
                graphs[i].add(i + arr[i])

        len_targets = len(targets)
        queue = deque([start])
        seen = set({start})

        while queue:
            node = queue.popleft()

            if node in targets:
                targets.remove(node)

            for neighbor in graphs[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)

        return len_targets != len(targets)
