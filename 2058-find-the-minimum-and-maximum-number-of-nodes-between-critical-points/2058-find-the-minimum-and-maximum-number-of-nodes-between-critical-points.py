# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head.next.next is None:
            return [-1,-1]
        prev = head
        temp = head.next
        front = head.next.next
        prevP = -1
        firstP = -1
        minDist = float('inf')
        cnt = 1
        while front is not None:
            if (front.val > temp.val and prev.val > temp.val ) or (front.val < temp.val and prev.val < temp.val):
                if firstP > -1 :
                    minDist = min(minDist , cnt - prevP)
                if firstP == -1:
                    firstP = cnt
                prevP = cnt 
            cnt += 1
            prev = temp 
            temp = front
            front = front.next
        
        if minDist == float('inf'):
            return [-1,-1]
        return [minDist,prevP - firstP]