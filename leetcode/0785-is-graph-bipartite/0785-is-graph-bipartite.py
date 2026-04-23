class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colored = [-1] * len(graph)
        def dfs(node, color):
            colored[node] = color 

            for nei in graph[node]:
                if colored[nei] == -1:
                    if not dfs(nei, 1- color):
                        return False 
                elif colored[nei] == color:
                    return False 
        
            return True 

        for i in range(len(graph)):
            if colored[i] == -1:
                if not dfs(i, 0):
                    return False 
        return dfs(0, 0)
