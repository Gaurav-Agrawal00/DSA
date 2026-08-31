# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None :
            return head
        old = None
        dummyHead = ListNode(-1)
        tail = dummyHead
        prev = head
        curr = head.next
        while prev is not None:
            if (old is None or old.val != prev.val ) and (curr is None or curr.val != prev.val):
                tail.next = prev
                tail = tail.next
            old = prev
            prev = curr
            if curr is not None:
                curr = curr.next
        tail.next = None
        return dummyHead.next