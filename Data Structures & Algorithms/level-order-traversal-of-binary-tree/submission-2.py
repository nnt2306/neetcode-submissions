# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        queue = deque([root])
        list_que = [] # It is better that we assign it blank before than give it first value directly
        while queue:
            level_size = len(queue)
            local_list = []
            while level_size >0: # This things will iterate through all the level
                node = queue.popleft()
                local_list.append(node.val) # This will avoid putting the blank list at the end
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_size -=1
            list_que.append(local_list)
        return list_que
                

            