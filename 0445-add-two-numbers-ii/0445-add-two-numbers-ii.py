# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]):
        ref = head
        nxt = ref.next
        ref.next = None

        while (nxt != None):
            before = ref
            ref = nxt
            nxt = nxt.next
            ref.next = before

        return ref
        
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_rev = self.reverseList(l1)
        l2_rev = self.reverseList(l2)
        l3 = ListNode()
        p = l3

        rem = 0
        while (l1_rev != None and l2_rev != None):
            temp = l1_rev.val + l2_rev.val + rem
            p.val = temp % 10
            rem = (temp - p.val) // 10

            l1_rev = l1_rev.next
            l2_rev = l2_rev.next
            
            if (l1_rev != None or l2_rev != None):
                p.next = ListNode()
                p = p.next
            
        while (l1_rev != None):
            temp = l1_rev.val + rem
            p.val = temp % 10
            rem = (temp - p.val) // 10

            l1_rev = l1_rev.next
            
            if (l1_rev != None):
                p.next = ListNode()
                p = p.next

        while (l2_rev != None):
            temp = l2_rev.val + rem
            p.val = temp % 10
            rem = (temp - p.val) // 10

            l2_rev = l2_rev.next
            
            if (l2_rev != None):
                p.next = ListNode()
                p = p.next
                
        if (rem != 0):
            p.next = ListNode()
            p = p.next
            p.val = rem

        return self.reverseList(l3)