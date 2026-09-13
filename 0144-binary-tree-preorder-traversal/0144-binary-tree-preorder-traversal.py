# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preOrder = []
        curr = root
        while curr:
            
            if curr.left:
                temp = curr.left
                while temp.right and temp.right != curr:
                    temp = temp.right

                if temp.right is None:
                    preOrder.append(curr.val)
                    temp.right = curr
                    curr = curr.left
                else:
                    temp.right = None
                    curr = curr.right
            else:
                preOrder.append(curr.val)
                curr = curr.right
        return preOrder