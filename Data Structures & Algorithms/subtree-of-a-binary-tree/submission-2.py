# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def isSameTree(self,a:Optional[TreeNode],b:Optional[TreeNode]):
        if a is None and b is None:
            return True
        
        if a is None or b is None:
            return False
        
        if a.val != b.val:
            return False
        if not self.isSameTree(a.left,b.left):
            return False
        if not self.isSameTree(a.right,b.right):
            return False
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ## Empty tree is subtree of any tree
        if subRoot is None:
           return True
        
        if root is None:
            return False

        ## For or if any condition True this will return immediately, otherwise this will go 
        ## sequentially

        ## In this either the trees are indentical or subRoot is a subtree of left child
        # or subRoot is subtree of right child, the main check is the isSameTree
        # When we do recursively this will check is Same tree for root left and root right
        # with subRoot, this is the main things    

        ## The total runtime will be O(nm), we call isSameTree in many different root 
        ## Each isSameTree can cost up to O(m) with m is number of nodes in subRoot
        return (
        self.isSameTree(root, subRoot)
        or self.isSubtree(root.left, subRoot)
        or self.isSubtree(root.right, subRoot)
    ) 


        