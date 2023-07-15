# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 == None and list2 == None):
            return None
        
        if (list1 == None):
            return list2
        
        if (list2 == None):
            return list1
        
        list3 = ListNode()
        p = list3
        while (list1 != None and list2 != None):
            if(list1.val < list2.val):
                p.val = list1.val
                list1 = list1.next
            else:
                p.val = list2.val
                list2 = list2.next
                            
            if (list1 != None or list2 != None):
                p.next = ListNode()
                
            p = p.next
            
        while (list1 != None):
            p.val = list1.val
            list1 = list1.next
            
            if (list1 != None):
                p.next = ListNode()
            
            p = p.next
                                 
        while (list2 != None):
            p.val = list2.val
            list2 = list2.next
            
            if (list2 != None):
                p.next = ListNode()
                
            p = p.next
                
                        
        return list3