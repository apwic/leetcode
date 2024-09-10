# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            if a == 0:
                return b
            if b == 0:
                return a

            while b != 0:
                a, b = b, a % b

            return a

        prev, p = head, head.next

        while p:
            prev.next = ListNode(gcd(prev.val, p.val))
            prev.next.next = p
            prev, p = p, p.next

        return head