# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        res = []
        stack = [(root, [root.val])] 
        while stack:
            node, digits = stack.pop()
            
            if not node.left and not node.right:
                num = int("".join(map(str, digits)))
                res.append(num)
            else:
                if node.right:
                    stack.append((node.right, digits + [node.right.val]))
                if node.left:
                    stack.append((node.left, digits + [node.left.val]))
        
        return sum(res)
"""
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        digit = [root.val]
        stack = [root]
        res = []
        
        def till_leaf(node, digit):
            while node:
                if node.left:
                    stack.append(node.left)
                    digit.append(node.left.val)
                node = node.left
            numm = int("".join(digit))
            res.append(numm)  

        while stack:
            stack.pop()
            digit.pop()
            if stack:
                node = stack[-1]

            till_leaf(node.right, digit)

        return sum(res)
"""