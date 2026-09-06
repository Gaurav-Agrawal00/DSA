# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ansSet = {}
        queue = deque([(root,0,0)])
        while queue:
            node , x , y = queue.popleft()
            if x not in ansSet :
                ansSet[x] = {}
            if y not in ansSet[x]:
                ansSet[x][y] = []
            ansSet[x][y].append(node.val)
            if node.left :
                queue.append((node.left,x-1,y+1))
            if node.right :
                queue.append((node.right,x+1,y+1))
        
        ans = []
        for x in sorted(ansSet.keys()):
            col = []
            for y in sorted(ansSet[x].keys()):
                col.extend(sorted(ansSet[x][y]))
            ans.append(col)

        return ans