# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        q = deque([root])
        search = set()

        while q:
            leng = len(q)
            for i in range(leng):
                node = q.popleft()
                if node.val in search:
                    return True 
                else:
                    search.add(k-node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)


        return False 
        