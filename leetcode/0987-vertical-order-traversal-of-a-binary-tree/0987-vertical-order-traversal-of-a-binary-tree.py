# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        pos_map = defaultdict(list)
        
        q = deque([(root, 0, 0)])
        
        while q:
            node, col, row = q.popleft()
            pos_map[col].append((row, node.val))
            
            if node.left:
                q.append((node.left, col - 1, row + 1))
            if node.right:
                q.append((node.right, col + 1, row + 1))
        
        result = []
        for col in sorted(pos_map.keys()):
            pos_map[col].sort(key=lambda x: (x[0], x[1]))
            result.append([val for _, val in pos_map[col]])
        
        return result

"""
from collections import deque, defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        pos_map = defaultdict(list)

        q = deque([(root, 0)]) 
        res = []
        while q:
            leng = len(q)

            for i in range(leng):
                node, level = q.popleft()
                pos_map[level].append(node.val)
                
                if node.left:
                    q.append((node.left, level-1))
                if node.right:
                    q.append((node.right, level+1))
        sorted_dict = dict(sorted(pos_map.items()))

        
        for pos, nodes in sorted_dict.items():
            res.append(nodes)
        return res 

"""