class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        mark = [-1] * n

        for i in range(n):
            if mark[i] == -1:
                stack = [i]
                mark[i] = 0
                
                while stack:
                    node = stack.pop()
                    
                    for nei in graph[node]:
                        if mark[nei] == -1:
                            mark[nei] = 1 - mark[node]  
                            stack.append(nei)
                        elif mark[nei] == mark[node]:
                            return False
        return True


"""class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        mark = [-1] * n

        for ind, des in enumerate(graph):
            if mark[ind] == -1:
                mark[ind] = 0  
            
            if mark[ind] == 0:
                child_mark = 1 
            else:
                child_mark = 0
                
            for nei in des:
                if mark[nei] == -1:
                    mark[nei] = child_mark
                elif mark[nei] != child_mark:
                    return False 

        return True """

