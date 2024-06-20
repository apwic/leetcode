class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(node):
            if node not in seen:
                seen.add(node)
                for neighbor in rooms[node]:
                    dfs(neighbor)

        seen = set()
        dfs(0)
        return len(seen) == len(rooms)
        