# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        curr = head
        i = 0

        while i <= n and curr:
            curr = curr.next
            i += 1

        to_remove = head
        j = 0
        while curr:
            to_remove = to_remove.next
            curr = curr.next
            j += 1

        if i + j == n:
            return head.next

        if to_remove.next:
            to_remove.next = to_remove.next.next
        else:
            to_remove.next = None

        return head

        