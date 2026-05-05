# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        from collections import defaultdict, deque

        def treeToGraph(root):
            if not root:
                return defaultdict(list)
                
            e = defaultdict(list)
            q = deque()
            q.append((root, None))
            
            while q:
                node, parent = q.popleft()
                if node.left:
                    q.append((node.left, node))
                    e[node.val].append(node.left.val)
                    e[node.left.val].append(node.val)
                if node.right:
                    q.append((node.right, node))
                    e[node.val].append(node.right.val)
                    e[node.right.val].append(node.val)
            return e
        
        if k == 0:
            return [target.val]
        
        myGraph = treeToGraph(root)
        result = []
        q = deque()
        q.append(target.val)
        visited = set()
        visited.add(target.val)
        distance = 0
        
        while q:
            distance += 1
            level_size = len(q)
            
            for _ in range(level_size):
                node = q.popleft()
                
                for nei in myGraph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        if distance == k:
                            result.append(nei)
                        else:
                            q.append(nei)
            
            if distance == k:
                return result
        
        return result  
