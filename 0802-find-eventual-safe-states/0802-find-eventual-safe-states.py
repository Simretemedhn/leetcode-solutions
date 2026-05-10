from collections import defaultdict, deque 

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        rev_graph = defaultdict(list)
        indegree  = [0] * len(graph)
        
        for i, dsts in enumerate(graph):
            for every in dsts:
                rev_graph[every].append(i)
                indegree[i] += 1 
        
        q = deque([node for node in range(len(graph)) if indegree[node] == 0])

        answer = []
        while q:
            node = q.popleft()
            answer.append(node)

            for nei in rev_graph[node]:
                indegree[nei] -= 1 
                if indegree[nei] == 0:
                    q.append(nei)
        answer.sort()
        return answer 
