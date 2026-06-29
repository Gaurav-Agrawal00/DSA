# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummyO = ListNode(-1)
        dummyE = ListNode(-1)
        t1 = dummyO
        t2 = dummyE
        temp = head
        while temp is not None and temp.next is not None:
            t1.next = temp
            t2.next = temp.next
            t1 = t1.next
            t2 = t2.next
            temp = temp.next.next
        
        if temp:
            t1.next = temp
            t2.next = temp.next
            t1 = t1.next
            t2 = t2.next
        
        t1.next = dummyE.next
        return dummyO.next