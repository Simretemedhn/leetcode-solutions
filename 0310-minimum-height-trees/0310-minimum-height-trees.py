from collections import defaultdict, deque 
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        degree = [0] * n 

        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
            degree[src] += 1
            degree[dst] += 1 
        
        q = deque([i for i in range(n) if degree[i] == 1])
        remaining =  n 
        while remaining > 2:
            len_count = len(q)
            remaining -= len_count 
            for _ in range(len_count):
                leaf = q.popleft()

                for nei in graph[leaf]:
                    degree[nei] -= 1 
                    if degree[nei] == 1:
                        q.append(nei)
        return list(q)
        
