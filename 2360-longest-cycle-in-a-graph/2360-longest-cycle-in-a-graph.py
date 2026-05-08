from collections import deque

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        indegree = [0] * n
        
        for i in range(n):
            if edges[i] != -1:
                indegree[edges[i]] += 1
        q = deque([i for i in range(n) if indegree[i] == 0])

        while q:
            node = q.popleft()
            nxt = edges[node]
            if nxt != -1:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        visited = [False] * n
        max_cycle = -1
        
        for i in range(n):
            if indegree[i] > 0 and not visited[i]:
                curr = i
                length = 0
                while not visited[curr]:
                    visited[curr] = True
                    curr = edges[curr]
                    length += 1
                max_cycle = max(max_cycle, length)
        
        return max_cycle
