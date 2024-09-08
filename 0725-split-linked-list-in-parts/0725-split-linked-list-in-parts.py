# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def create(arr):
            head = ListNode()
            prev, p = None, head

            for num in arr:
                p.val = num
                p.next = ListNode()
                prev = p
                p = p.next

            prev.next = None

            return head

        # linked list to array
        arr = []
        p = head

        while p:
            arr.append(p.val)
            p = p.next
        
        n = len(arr)

        # divide into parts
        if n > k:
            div, rem = n // k, n % k
        else:
            div, rem = 1, 0

        ans = [None] * k
        i, idx = 0, 0

        while idx < n:
            curr = div
            if rem:
                curr += 1
                rem -= 1

            ans[i] = create(arr[idx:idx+curr])
            idx += curr
            i += 1

        return ans