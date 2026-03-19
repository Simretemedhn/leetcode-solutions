# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stack = [(root, 1)] 
        max_ = 1

        while stack:
            parent = stack.pop()
            if parent[0].left: stack.append((parent[0].left, parent[1]+1))
            max_ = max(max_, parent[1])
            if parent[0].right: stack.append((parent[0].right, parent[1]+1)) 
            max_ = max(max_, parent[1])
        
        return max_