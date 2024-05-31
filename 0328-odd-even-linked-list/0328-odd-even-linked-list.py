# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        if not head.next:
            return head

        odd, prev_odd = head, None
        even, prev_even = head.next, None
        start_even = even

        while even and even.next:
            prev_odd = odd
            odd = odd.next.next
            prev_odd.next = odd

            prev_even = even
            even = even.next.next
            prev_even.next = even

        odd.next = start_even
        return head