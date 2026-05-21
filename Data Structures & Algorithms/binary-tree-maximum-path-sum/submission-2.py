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
        right_sum = self.compute_sum(node.right)

        left_gain = max(left_sum,0)
        right_gain = max(right_sum,0)

        ## Update the global_max :
        candidate = node.val + left_gain + right_gain
        self.global_max_sum = max(self.global_max_sum, candidate)

        return node.val + max(left_gain, right_gain)


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.global_max_sum = -float('inf')
        self.compute_sum(root)

        return self.global_max_sum
        
        