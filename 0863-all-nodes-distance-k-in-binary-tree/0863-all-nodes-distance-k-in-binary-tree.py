# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def parent_node(self,node,parent_data):
        dataSet = deque([node])
        while dataSet:
            temp = dataSet.popleft()
            if temp.left:
                parent_data[temp.left] = temp
                dataSet.append(temp.left)
            if temp.right:
                parent_data[temp.right] = temp
                dataSet.append(temp.right)
        
    def find_kthDist(self,node,parent_data,target,k):
        queue = deque([target])
        is_viewed = {target}

        curr_lvl = 0
 
        while queue:
            if curr_lvl == k:
                break

            curr_lvl += 1
            n = len(queue)
            for i in range(n):
                temp = queue.popleft()
                
                if temp.left and temp.left not in is_viewed:
                    is_viewed.add(temp.left)
                    queue.append(temp.left)
                
                if temp.right and temp.right not in is_viewed:
                    is_viewed.add(temp.right)
                    queue.append(temp.right)
                
                if temp in parent_data and parent_data[temp] not in is_viewed:
                    is_viewed.add(parent_data[temp])
                    queue.append(parent_data[temp])

        return [temp.val for temp in queue]


    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_data = {}
        if not root:
            return []
        self.parent_node(root,parent_data)

        return self.find_kthDist(root,parent_data,target,k)