class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        

        # state = 0 = unvisited, 1 = currently processing, 2 = already proceeced 
        answer = []
        state = [0] * numCourses
        def dfs(course):

            #cycle exist 
            if state[course] == 1:
                return False 
            elif state[course] == 2:
                return True 
            
            state[course] = 1 
            for nei in graph[course]:
                if not dfs(nei):
                    return False 
            
            state[course] = 2
            answer.append(course) 
            return True 


        for course in range(numCourses):
            if not dfs(course):
                return []
        return answer[::-1]