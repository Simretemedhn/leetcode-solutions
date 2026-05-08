from collections import defaultdict, deque 

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(list)
        for src, dst in prerequisites:
            graph[src].append(dst)

        def isreachable(start, end):
            q = deque([start])
            visited = set()
            visited.add(start)

            while q:
                node = q.popleft()

                for nei in graph[node]:
                    if nei == end:
                        return True 
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            return False 
        answer = []
        for start, end in queries:
            if isreachable(start, end):
                answer.append(True)
            else:
                answer.append(False)
        return answer 
