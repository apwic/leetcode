# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sys.set_int_max_str_digits(0)
        arr_head = []
        
        while head:
            arr_head.append(str(head.val))
            head = head.next
            
        res = ''.join(arr_head)
        res = list(str(int(res)*2))
        new_head = ListNode()
        p = new_head
        
        for idx, ch in enumerate(res):
            p.val = int(ch)
            if idx == len(res) - 1:
                p.next = None
            else:
                p.next = ListNode()
                p = p.next
            
        return new_head
            
        