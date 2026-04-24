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
        total = 0
        visited = set()
        def dfs(node):
            nonlocal total, visited
            total += graph[node][0]
            visited.add(node)


            for nei in graph[node][1]:
                if nei not in visited:
                    dfs(nei)

        dfs(id)
        return total 