class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def swap(state, i, j):
            temp = list(state)
            temp[i], temp[j] = temp[j], temp[i]
            return "".join(temp)

        goal = "123450"
        moves = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [1, 3, 5],
            [2, 4],
        ]

        start = "".join(str(num) for row in board for num in row)
        queue = deque([start])
        visited = set()
        visited.add(start)
        count = 0

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()

                if curr == goal:
                    return count

                idx = curr.index("0")
                for new in moves[idx]:
                    nxt = swap(curr, idx, new)

                    if nxt in visited:
                        continue

                    visited.add(nxt)
                    queue.append(nxt)
            count += 1

        return -1