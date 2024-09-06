# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        prev, curr = None, head

        while curr:
            if curr.val in nums:
                # first element removed
                if curr == head:
                    head = head.next
                else:
                    prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return head