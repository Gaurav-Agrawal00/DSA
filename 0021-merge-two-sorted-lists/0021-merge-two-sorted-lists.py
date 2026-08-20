# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = list1
        t2 = list2 
        if t1 is None and t2 is None:
            return 
        if t2 is None:
            return t1
        if t1 is None:
            return t2
        dummyHead = ListNode(-1)
        temp = dummyHead
        t1 = list1
        t2 = list2 
        while t1 is not None and t2 is not None :
            if t1.val < t2.val :
                temp.next = t1
                t1 = t1.next
                temp = temp.next
            else:
                temp.next = t2
                temp = temp.next
                t2 = t2.next
        while t1 is not None:
            temp.next = t1
            t1 = t1.next
            temp = temp.next

        while t2 is not None:
            temp.next = t2
            t2 = t2.next
            temp = temp.next
        
        return dummyHead.next