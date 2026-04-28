# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checking_ancestor(self,r,a,b):
        ## Checking ancestor will return a boolean

        ## Also here we keep track of the global value that will not change through the recursion
        # and only update if successful
        global lca
        ## Remember if we compare two nodes reference r and p, this will be mean that
        # do r and p point to exact same node in memory

        ## If we compare r.val and p.val, this check only where the two nodes store
        # the same value
        if r is None:
            return False
        '''
        This thing will check current node, then go left then go right like dfs
        then when ever the thing allow us to have 2 condition we return the global directly
        '''
        node_is_p_or_q = (r.val == a.val or r.val == b.val)
        left_contains_p_or_q =self.checking_ancestor(r.left,a,b)
        right_contains_p_or_q =self.checking_ancestor(r.right,a,b)
        ## int(True) = 1, int(False) = 0
        if int(node_is_p_or_q) + \
        int(left_contains_p_or_q) + \
        int(right_contains_p_or_q) == 2:
            lca = r

        return (node_is_p_or_q 
                or left_contains_p_or_q
                or right_contains_p_or_q)

        
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.checking_ancestor(root,p,q)
        return lca
       

        
        
        

        