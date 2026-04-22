from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)


        visited = set()
        stack = [source]
        
        while stack:
            node = stack.pop()

            if node not in visited:
                visited.add(node)
                if node == destination:  
                    return True
                
                for nei in graph[node]:
                    if nei not in visited:  
                        stack.append(nei)

        return False



            
            
