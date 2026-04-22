
from collections import defaultdict
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        stack = [source]

        while stack:
            node = stack.pop()

            if node == destination:
                return True

            if node not in visited:
                visited.add(node)

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)

        return False