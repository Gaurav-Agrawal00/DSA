# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        in_mapInd = {val:ind for ind , val in enumerate(inorder)}
        
        def build(left,right):
            if left > right:
                return None
            
            
            root_val = postorder.pop()
            root = TreeNode(root_val)

            mid = in_mapInd[root_val]
            
            root.right = build(mid+1 , right)
            root.left = build(left,mid-1)

            return root

        return build(0 , len(postorder) -1)
