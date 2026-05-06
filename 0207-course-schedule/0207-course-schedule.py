from collections import defaultdict, deque 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses       
        graph = defaultdict(list) 

        for course, pre_req in prerequisites:
            indegree[course] += 1  
            graph[pre_req].append(course)

        q = deque([i for i in range(len(indegree)) if indegree[i] == 0])
        order = []
        while q:

            course = q.popleft()
            order.append(course)

            for nei in graph[course]:
                indegree[nei] -= 1 
                if indegree[nei] == 0:
                    q.append(nei)
        return len(order) == numCourses