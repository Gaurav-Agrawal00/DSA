# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        string = ''
        queue = deque([root])
        while queue:
            n = len(queue)
            for i in range(n):
                temp = queue.popleft()
                if temp:
                    string += str(temp.val) + ','
                else:
                    string += '#' + ','
                if temp:
                    queue.append(temp.left)
                    queue.append(temp.right)
        return string
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        value = data.split(',')
        if value[0] == '#':
            return None
        ind = 0
        root = TreeNode(int(value[0]))
        queue= deque([root])
        ind += 1
        
        while queue and ind < len(value)-1:
            temp = queue.popleft()
            if value[ind] != '#':
                temp.left = TreeNode(int(value[ind]))
                queue.append(temp.left)

            ind += 1
            if value[ind] != '#':
                temp.right = TreeNode(int(value[ind]))
                queue.append(temp.right)
            ind+=1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))