from collections import defaultdict, deque 
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses 
        graph = defaultdict(list)
        
        for src, dst in prerequisites:
            graph[dst].append(src)
            indegree[src] += 1 

        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        answer = []
        while q:
            node  = q.popleft()
            answer.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1 
                if indegree[nei] == 0:
                    q.append(nei)
        return answer if len(answer) == numCourses else []