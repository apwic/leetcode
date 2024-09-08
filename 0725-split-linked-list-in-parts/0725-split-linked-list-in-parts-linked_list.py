# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        p = head

        while p:
            n += 1
            p = p.next

        div, rem = n // k, n % k

        ans = []
        p = head

        for i in range(k):
            part = p
            size = div

            if rem:
                size += 1
                rem -= 1

            # move p until size
            for _ in range(size-1):
                if p:
                    p = p.next

            # break p
            if p:
                next_part = p.next
                p.next = None
                p = next_part

            ans.append(part)

        return ans