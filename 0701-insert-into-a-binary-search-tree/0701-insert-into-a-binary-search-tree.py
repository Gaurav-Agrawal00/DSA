# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        ceil = -1
        curr = root
        while curr:
            if curr.val > val :
                ceil = curr
                curr = curr.left
            else:
                curr = curr.right
        
        if ceil == -1:
            curr = root
            while curr.right:
                curr = curr.right
            
            curr.right = TreeNode(val)
            return root
        temp = ceil.left
        new_ins = TreeNode(val)
        ceil.left = new_ins
        new_ins.left = temp
        return root