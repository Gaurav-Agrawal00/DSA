# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findKthNode(self,head,k):
        cnt = 0
        temp = head
        while temp is not None:
            cnt += 1
            if cnt == k:
                return temp
            temp = temp.next
        return None

    def reverse(self,head):
        # if head is None or head.next is None:
        #     return head
        temp = head
        curr = 0
        prev = None
        while temp is not None:
            curr = temp
            temp = temp.next
            curr.next = prev
            prev = curr
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prevNode = None
        while temp is not None:
            kthNode = self.findKthNode(temp,k)
            if kthNode == None :
                if prevNode:
                    prevNode.next = temp
                break
                
            nextNode = kthNode.next
            kthNode.next = None
            self.reverse(temp)
            if temp == head:
                head = kthNode
            else:
                prevNode.next = kthNode
            prevNode = temp
            temp = nextNode
        return head