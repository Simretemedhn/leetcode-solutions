# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        def down_Sum(node, dir):
            sum_ = 0
            while node:
                sum_ += node.val
                if sum_ == targetSum:
                    count += 1
                node = node.dir

            down_Sum(node.left)
            down_Sum(node.right)
        
        down_Sum(root, left)
        down_Sum(root, right)
    
        return count 
"""
    
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
            
        self.count = 0 
        
        def down_Sum(node, current_sum):
            if not node:
                return
            
            current_sum += node.val
            
            if current_sum == targetSum:
                self.count += 1
            
            down_Sum(node.left, current_sum)
            down_Sum(node.right, current_sum)
        
        def dfs(node):
            if not node:
                return
            
            down_Sum(node, 0)
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.count