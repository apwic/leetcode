# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            p = None
            while head:
                nxt = head.next
                head.next = p
                p = head
                head = nxt
        
            return p
        
        head = reverse(head)
        curr = head
        
        while curr:
            if curr.next and curr.val > curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
            
        return reverse(head)
            
            