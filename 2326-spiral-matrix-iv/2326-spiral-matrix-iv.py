# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        def valid(i, j):
            return 0 <= i < m and 0 <= j < n and (i, j) not in seen

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        matrix[0][0] = head.val

        x, y = 0, 0
        seen = {(0, 0)}
        p = head.next

        while p:
            for dx, dy in directions:
                x, y = x + dx, y + dy

                while valid(x, y):
                    if p:
                        matrix[x][y] = p.val
                        p = p.next
                    seen.add((x, y))
                    x, y = x + dx, y + dy

                x, y = x - dx, y - dy

        return matrix