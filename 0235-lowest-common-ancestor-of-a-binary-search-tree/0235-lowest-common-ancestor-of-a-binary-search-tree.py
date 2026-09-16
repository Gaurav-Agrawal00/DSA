# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if node.val > q.val and node.val > p.val:
            return self.lowestCommonAncestor(node.left,p,q)
        elif node.val < q.val and node.val < p.val:
            return self.lowestCommonAncestor(node.right,p,q)
        else:
            return node