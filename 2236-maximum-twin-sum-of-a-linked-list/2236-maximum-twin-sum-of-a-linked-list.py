# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverse(head):
            prev = None
            curr_rev = ListNode()
            curr = head
            n = 0

            while curr:
                curr_rev.val = curr.val
                curr_rev.next = prev
                prev = curr_rev
                curr = curr.next
                curr_rev = ListNode()
                n += 1

            return n, prev

        n, head_rev = reverse(head)
        curr, curr_rev = head, head_rev
        max_sum, i = 0, 0

        while i <= n//2:
            max_sum = max(max_sum, curr.val + curr_rev.val)
            curr, curr_rev = curr.next, curr_rev.next
            i += 1

        return max_sum
