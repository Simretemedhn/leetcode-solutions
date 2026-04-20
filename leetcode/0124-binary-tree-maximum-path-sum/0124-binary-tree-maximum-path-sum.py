# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float('-inf')
        
        def one_sided(node):
            if not node:
                return 0
            
            left = max(0, one_sided(node.left))
            right = max(0, one_sided(node.right))
            
            self.best = max(self.best, node.val + left + right)
            
            return node.val + max(left, right)
        
        one_sided(root)
        return self.best

"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def max_path(root):
            if root.left == None:
                return root.val
            if root.right == None:
                return root.val 
            
            left_max = max_path(root.left)
            right_max = max_path(root.right)

            if left_max > right_max:
                max_way = left_max 
            else:
                max_way = right_max 

            if root.val < 0:
                return max_way
            else:
                return max_way + root.val 
        return max_path(root)


"""
