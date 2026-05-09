# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''
        The ideal here is that all nodes in the left subtree < root
        < all nodes in right subtree
        '''
    def inorder_traverse(self,node):
        if node is None:
            return 

        self.inorder_traverse(node.left)
        self.res.append(node.val)
        self.inorder_traverse(node.right)
        
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ## In the first version self.res has noot been clean, so we need to remove
        # the node in self.l;eft right
        self.res = []
        self.inorder_traverse(root.left)
        left_size = len(self.res)

        if k <= left_size:
            return self.res[k-1]
        elif k == left_size +1:
            return root.val
        else:
            k = k-len(self.res)-1
            self.res = []
            self.inorder_traverse(root.right)
            return self.res[k-1]

        
    