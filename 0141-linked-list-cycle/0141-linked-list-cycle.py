# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        i = 0
        
        while fast and fast.next:
            if slow == fast and i != 0:
                return True

            slow = slow.next
            fast = fast.next.next
            i += 1

        return False

