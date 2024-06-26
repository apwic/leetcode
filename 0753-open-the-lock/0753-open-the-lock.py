class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def find_neighbor(node):
            neighbors = set()

            for i in range(len(node)):
                el = int(node[i])
                dec = (el - 1) % 10
                inc = (el + 1) % 10
                neighbors.add(node[:i] + str(dec) + node[i+1:])
                neighbors.add(node[:i] + str(inc) + node[i+1:])

            return neighbors

        queue = deque([("0000", 0)])
        seen = set(deadends)

        if "0000" in seen:
            return -1

        seen.add("0000")

        while queue:
            node, step = queue.popleft()

            if node == target:
                return step

            neighbors = find_neighbor(node)
            for neighbor in neighbors:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, step+1))

        return -1
        