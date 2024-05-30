# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l, r = left-1, right-1

        if not head.next or l == r:
            return head

        i = 0
        start, end = None, None
        prev = None
        curr = head

        while curr is not None and i <= r:
            if l <= i <= r:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

                if i == l:
                    end = prev
            else:
                start = curr
                curr = curr.next

            i += 1

        if start: 
            start.next = prev
        else:
            head = prev

        end.next = curr
        return head
