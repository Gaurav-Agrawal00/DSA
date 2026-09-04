# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findDia(self,node,dia):
        if node is None:
            return 0
        lh = self.findDia(node.left,dia)
        rh = self.findDia(node.right , dia)
        dia[0] = max(lh + rh , dia[0])
        return max(lh , rh) + 1


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = [0]
        self.findDia(root,dia)
        return dia[0]