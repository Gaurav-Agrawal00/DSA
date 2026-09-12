# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_ind = {val : ind for ind , val in enumerate(inorder)}
        
        self.pre_val = 0
        def build(left,right):
            if left > right:
                return None
            
            root_val = preorder[self.pre_val]
            root = TreeNode(root_val)
            self.pre_val += 1

            mid = pre_ind[root_val]

            root.left = build(left,mid-1)
            root.right = build(mid+ 1 , right)

            return root

        return build(0,len(inorder) - 1)

        