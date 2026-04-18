# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        Technique using DFS
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False

        if not self.isSameTree(p.left,q.left):
            return False
        if not self.isSameTree(p.right,q.right):
            return False
        return True
        '''
        queue1 = deque([p])
        queue2 = deque([q])

        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            
            ## Here this cover a case even when we pop left is None
            if node1 is None and node2 is None:
                continue

            if node1 is None or node2 is None:
                return False

            if node1.val != node2.val:
                return False
            ## Here we include None also in append because there will be 

            queue1.append(node1.left)
            queue1.append(node1.right)

            queue2.append(node2.left)
            queue2.append(node2.right)

        return not queue1 and not queue2
        
        