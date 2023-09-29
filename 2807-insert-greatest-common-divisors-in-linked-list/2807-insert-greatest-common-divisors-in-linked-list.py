# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def gcd(a, b):
            if (a == 0):
                return b
            
            return gcd(b % a, a)
        
        p = head
        
        while (p.next != None):
            nxt = p.next
            p.next = ListNode(gcd(p.val, nxt.val), nxt)
            p = nxt
            
        return head
        
        
        