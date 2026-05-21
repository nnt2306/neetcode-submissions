# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def compute_sum(self,node):
        if node is None:
            return 0
        left_sum = self.compute_sum(node.left)
        print(f"Node now is {node.val} and left sum is {left_sum}")
        right_sum = self.compute_sum(node.right)
        print(f"Node now is {node.val} and right sum is {right_sum}")


        left_gain = max(left_sum,0)
        right_gain = max(right_sum,0)
        print(f"Node val is {node.val} and Total gain is {node.val+ max(left_gain, right_gain)}")


        ## Update the global_max, need to think about it again
        ## carefully set up things:
        candidate = node.val + left_gain + right_gain
        self.global_max_sum = max(self.global_max_sum, candidate)
        
        ## See it further but here ideal is that
        ## at node we will return node.val + max(left_gain, right_gain) for given node
        ## Because we will need update upward so we cannot sum like global max
        #, this can create conflict because this can sum a branch also, so we need
        # separately protocol (see further in book)
        return node.val + max(left_gain, right_gain)


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max_sum = -float('inf')
        self.compute_sum(root)

        return self.global_max_sum
        
        