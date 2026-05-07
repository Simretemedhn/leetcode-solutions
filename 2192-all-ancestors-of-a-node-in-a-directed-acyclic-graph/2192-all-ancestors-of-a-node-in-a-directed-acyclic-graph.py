from collections import defaultdict 

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        with_nei = defaultdict(list)
        for src, dst in edges:
            with_nei[dst].append(src) 
        
        def bfs(node, output, visited):
            q = deque([nei for nei in with_nei[node]])
            visited.update(q)
            while q:
                node = q.popleft()
                output.append(node)

                for nei in with_nei[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

            return sorted(output) 
        
        answer = []
        for i in range(n):
            if with_nei[i] != 0:
                ancestors = bfs(i, [], set())
                answer.append(ancestors)
            else:
                answer.append([])
        
        return answer 

        