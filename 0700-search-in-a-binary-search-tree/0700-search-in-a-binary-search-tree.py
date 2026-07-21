# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None 
        if root.val == val:
            return root 
        
        # Search left
        left_result = self.searchBST(root.left, val)
        if left_result:
            return left_result
        
        # Search right
        right_result = self.searchBST(root.right, val)
        if right_result:
            return right_result
        
        return None