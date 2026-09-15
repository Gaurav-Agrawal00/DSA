# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,node):
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        
        right_node = node.right
        left_right_node = node.left
        while left_right_node.right:
            left_right_node = left_right_node.right
        
        left_right_node.right = right_node
        return node.left

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if root.val == key:
            return self.helper(root)
        
        curr = root
        while curr:
            if curr.val > key:
                if curr.left and curr.left.val == key:
                    curr.left = self.helper(curr.left)
                    break
                curr = curr.left
            else:
                if curr.right and curr.right.val == key:
                    curr.right = self.helper(curr.right)
                    break
                curr = curr.right
        return root