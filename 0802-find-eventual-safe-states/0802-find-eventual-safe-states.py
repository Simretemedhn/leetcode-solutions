class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        is_safe = {}

        def dfs(i):
            if i in is_safe:
                return is_safe[i]
            is_safe[i] = False 
            for nei in graph[i]:
                if not dfs(nei):
                    return False 
            is_safe[i] = True 
            return True 

        answer = []
        for i in range(n):
            if dfs(i):
                answer.append(i)
        return answer 





""" my first dump solution 
        is_safe = {}

        stack2 = []
        def dfs(node):
            stack = [node]
            visited = set([node])  
            last = None 
            
            while stack:
                curr = stack.pop()
                stack2.append(curr)
                last = curr
                
                for nei in graph[curr]:
                    if nei in visited:
                        is_safe[nei] = False 
                        return False 
                    elif nei not in visited:
                        visited.add(nei)  
                        stack.append(nei)
            is_safe[last] = True 
            return True 
        for i in range(len(graph)):
            if i not in is_safe:
                dfs(i)
                last = stack2.pop()
                if is_safe[last]:
                    while stack2:
                        node = stack2.pop()
                        if node not in is_safe:
                            dfs(node)
                else:
                    while stak2:
                        node = stack2.pop()
                        is_safe[node] = False 

        return [i for i in range(len(is_safe)) if is_safe]  
"""