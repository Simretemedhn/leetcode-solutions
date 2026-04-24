class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        n = len(graph) - 1 
        
        def dfs(node, path):
            path.append(node)
            
            if node == n:
                result.append(path.copy())  
            else:
                for nei in graph[node]:
                    dfs(nei, path)
            
            path.pop()  
        
        dfs(0, [])
        return result


        