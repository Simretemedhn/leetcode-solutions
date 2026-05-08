from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
            
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        
        q = deque([0])
        visited = {0}
        last = 0
        
        while q:
            node = q.popleft()
            last = node
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        
        parent = {}  
        q = deque([last])
        visited = {last}
        parent[last] = -1  
        farthest = last
        
        while q:
            node = q.popleft()
            farthest = node
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    parent[nei] = node
                    q.append(nei)
        
        path = []
        current = farthest
        while current != -1:
            path.append(current)
            current = parent[current]

        path_length = len(path)
        if path_length % 2 == 1:
            return [path[path_length // 2]]
        else:
            return [path[path_length // 2 - 1], path[path_length // 2]]