# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        curr = root
        new_node = TreeNode(val)
        
        while True: 
            if curr.val > val:
                if curr.left is None:  
                    curr.left = new_node
                    break
                curr = curr.left  
            else:
                if curr.right is None: 
                    curr.right = new_node
                    break
                curr = curr.right  
        
        return root
"""
        res = []

        q = deque([root])

        while q:
            node = q.popleft()
            res.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return res """

