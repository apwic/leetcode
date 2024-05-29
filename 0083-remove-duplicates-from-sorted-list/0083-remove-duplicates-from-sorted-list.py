# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        from collections import defaultdict
        freq = defaultdict(int)
        p = head

        while p:
            freq[p.val] += 1
            p = p.next

        new_head = ListNode()
        new_p = new_head

        for i, val in enumerate(freq.keys()):
            new_p.val = val
            if i < len(freq.keys()) - 1:
                new_p.next = ListNode()
                new_p = new_p.next
            else:
                new_p.next = None
        
        return new_head