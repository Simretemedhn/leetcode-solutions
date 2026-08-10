# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if it is bigger that both we have to go to the left 
        # if it is smaller than both we have to go to the right 
        # if it is in the middle of both, it is the number 
        # if one of the number if found it is the number 
        if not root:
            return None 
        if root == p or root == q:
            return root  
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q) 
        else:
            return root

