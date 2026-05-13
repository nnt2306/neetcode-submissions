# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

''' 
- First we determine the value of root node of the tree, assgin the preorder index start at 0
- At each step we move this index forward
- We need to store the index of root inside the inorder, divide the left sub tree
[0:inorder_index] and right [inorder_index +1 :]the 


'''
class Solution:
    def helper(self,left_in,right_in):
        ## We need to put this thing first otherwise 
        ## we do not have terminal condtion and preindex 
        ## can get out of index range
        if left_in > right_in :
            return None

        root = preorder[self.pre_index]
        self.pre_index +=1
        in_index = self.map_index_inorder[root]

        node = TreeNode(root)
        
        node.left = self.helper(left_in, in_index -1)
        node.right = self.helper(in_index +1, right_in)

        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_index = 0
        n = len(preorder)

        self.map_index_inorder = {}
        ## This hash map things make for search inorder index faster
        ## without search through whole subarray
        for index,val in enumerate(inorder):
            self.map_index_inorder[val] = index
        ## If we do not want to use self we need to put the helper function
        ## inside buildTree
        
        return self.helper(0,n-1)


        

    
        
        