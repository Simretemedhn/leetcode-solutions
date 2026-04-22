from collections import defaultdict 
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)




        visited = set()
        def dfs(node):
            nonlocal visited 
            if node == destination:
                return True 
            
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei):
                        return True 
            return False 

        return dfs(source) 
            
            
