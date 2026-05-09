# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ''' 
    Better way is that we might not need the list, we can have O(1) space
    ## If we return node.val directly in the code, this will miss the part of 
    left node.left,k and this can miss the return and return None

    For most recuresive calls before kth node is found left answer and right are usually None
    ## This means no answer found here so continue the process

    For example at node 2 all the process show that is None, then it go to node 3 
    this will show None directly on the left then process
    '''
    def inorder_traverse(self,node,k):
        if node is None:
            return 
        left_answer = self.inorder_traverse(node.left,k)
        if left_answer is not None: # So when this is None this will continue to count
        ## Taken example the answer is the left most one when this reach None, 
        # the count will be activate then left answer will be recoiurd 
            return left_answer

        self.count +=1
        if self.count == k:
            return node.val

        right_answer = self.inorder_traverse(node.right,k)
        if right_answer is not None:
            return right_answer

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        return self.inorder_traverse(root,k)
        
        