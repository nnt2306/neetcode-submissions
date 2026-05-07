# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sub_valid_check(self,node,lb = -float('inf'),rb = float('inf')):
        '''
        In Python, when you call a function, Python creates a new function frame. 
        That frame stores the local variables for that call, including node, lb, and rb. 
        
        ## Passing lb and rb into the recursive call 
        creates a new local version of lb and rb for that call, so we do not need 
        self.lb or self.rb

        sub_valid_check(node=6, lb=5, rb=inf), Python remeber node = 6,lb = 5, rb =inf
        then from node 6 if we call left sub_valid_check(node=3, lb=5, rb=6), this will check
        again the store local lb = 5
        '''
        if node is None:
            return True
        if node.val >= rb or node.val <= lb:
            return False

        left_valid = self.sub_valid_check(node.left, lb = lb, rb = node.val)
        right_valid = self.sub_valid_check(node.right,lb = node.val,rb = rb)
        
        return (left_valid and right_valid)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.sub_valid_check(root)


        