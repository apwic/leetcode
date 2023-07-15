# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None):
            return head
        
        rev = head
        nxt = rev.next
        rev.next = None
        
        while (nxt != None):
            before = rev
            rev = nxt
            nxt = nxt.next
            rev.next = before

        return rev
        