# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        if temp is None or temp.next is None:
            return head
        newHead = temp.next
        prev = None
        while temp is not None and temp.next is not None :
            nextNode = temp.next
            temp.next = nextNode.next
            nextNode.next = temp
            if prev is not None:
                prev.next = nextNode
            prev = temp
            temp = temp.next


        return newHead
