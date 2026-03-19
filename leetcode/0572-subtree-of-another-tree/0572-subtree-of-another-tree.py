# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if not root or not subRoot:
            return False
            
        q = deque([root])
        
        def is_same_tree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            
            return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
        
        while q:
            node = q.popleft()
            
            if node.val == subRoot.val:
                if is_same_tree(node, subRoot):
                    return True
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return False
