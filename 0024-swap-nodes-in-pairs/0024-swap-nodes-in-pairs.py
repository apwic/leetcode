# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        new_head = None
        new_curr = None

        while curr:
            swap = None
            for _ in range(2):
                if curr:
                    nxt = curr.next
                    curr.next = swap
                    swap = curr
                    curr = nxt
            
            if new_head:
                new_curr.next = swap
                new_curr = new_curr.next.next
            else:
                new_head = swap
                new_curr = new_head.next

        return new_head