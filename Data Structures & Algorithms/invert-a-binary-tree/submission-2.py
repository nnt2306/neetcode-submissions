# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ## When we modify tree in place, whole tree is still accessed through its entry point
        ## This is the way we use recursion, maybe we can try iteratively with deque
        '''
        if root is None:
            return
        root.left,root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        '''
        if root is None:
            return
        queue = deque([root])
        while queue:
           node = queue.popleft() # remove the left 
           ## at first iteration node is root, then from next we will always swap left and right
           # finally when we return root this will update what is our new left and new right
           node.left,node.right = node.right,node.left # proceed the node
           if node.left:
               queue.append(node.left) # append right
           if node.right:
               queue.append(node.right)
        return root



