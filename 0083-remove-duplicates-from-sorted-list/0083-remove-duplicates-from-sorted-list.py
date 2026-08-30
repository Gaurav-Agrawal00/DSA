# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None :
            return head
        temp = head.next
        prev = head
        while temp is not None :
            if prev.val == temp.val :
                prev.next = temp.next
            else:
                prev = temp
            temp = temp.next
        return head