from collections import defaultdict, deque 
from typing import List

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        n = len(quiet)
        indegree = [0] * n

        for src, dst in richer:
            graph[src].append(dst)
            indegree[dst] += 1 
        
        answer = [i for i in range(n)]
        q = deque([i for i in range(n) if indegree[i] == 0])

        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()

                for nei in graph[node]:
                    if quiet[answer[nei]] > quiet[answer[node]]:
                        answer[nei] = answer[node]
                    
                    indegree[nei] -= 1      
                    if indegree[nei] == 0:
                        q.append(nei)
        
        return answer