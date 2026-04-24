"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int: 
        graph = {emp.id: [emp.importance, emp.subordinates] for emp in employees}

        stack = [id]

        visited = set()
        total = 0
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                total += graph[vertex][0]
                visited.add(vertex)



            for nei in graph[vertex][1]:
                stack.append(nei)
        return total 



        