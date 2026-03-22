# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        q = deque([root])

        while q:
            leng = len(q)
            for i in range(leng):
                node = q.popleft()
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)

                if node.val % 2 == 0:
                    if node.left:
                        if node.left.left:
                            res += node.left.left.val
                        if node.left.right:
                            res += node.left.right.val
                    if node.right:
                        if node.right.left:
                            res += node.right.left.val
                        if node.right.right:
                            res += node.right.right.val

        return res
