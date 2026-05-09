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
    def inorder_traverse(self,node,res):
        if node is None:
            return 

        self.inorder_traverse(node.left,res)
        res.append(node.val)
        self.inorder_traverse(node.right,res)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        This thing is good, but this store the whole tree and it can be wasteful

        '''
        res = []
        self.inorder_traverse(root,res)

        return res[k-1]
         
        