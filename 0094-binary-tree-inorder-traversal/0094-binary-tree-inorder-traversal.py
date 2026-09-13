# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr  = root
        preOrder = []
        while curr:
            if curr.left is None:
                preOrder.append(curr.val)
                curr = curr.right
            else:
                temp = curr.left
                while temp.right and temp.right != curr:
                    temp = temp.right
                
                if temp.right != curr :
                    temp.right = curr
                    curr = curr.left
                else:
                    temp.right = None
                    preOrder.append(curr.val)
                    curr = curr.right
        return preOrder