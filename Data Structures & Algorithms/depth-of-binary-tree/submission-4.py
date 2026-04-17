# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = deque([root])
        depth = 0
        while queue:
            level_size = len(queue)
            print(level_size)
            while level_size >0:
                node = queue.popleft()
                print(node.val)

                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                level_size -=1
                print(level_size)
            depth +=1

        return depth


        