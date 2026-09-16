# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLca(self,node,p,q):
        # if node.val == q.val:
        if not node:
            return

        if node.val > q.val:
            return self.findLca(node.left,p,q)
        elif node.val <= q.val and node.val >= p.val:
            return node
        else:
            return self.findLca(node.right,p,q)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            return self.lowestCommonAncestor(root,q,p)
        
        return self.findLca(root,p,q)