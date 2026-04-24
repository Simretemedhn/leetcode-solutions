from collections import defaultdict 

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)

        n = len(bombs)
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue 
                x2, y2, r2 = bombs[j]
                
                distance_squared = (x1 - x2)**2 + (y1 - y2)**2
                if distance_squared <= r1**2:
                    graph[i].append(j)

        def dfs(node, visited):
            count = 1
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    count += dfs(nei, visited)
            return count

        max_ = 0 
        for i in range(len(bombs)):
            visited = {i}
            curr = dfs(i, visited)
            max_ = max(max_, curr)

        return max_
"""
from collections import defaultdict 

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)

        n = len(bombs)
        for  i in range(n):
            curr_loc_r, curr_loc_c, radius = bombs[i]
            for j in range(n):
                if i == j:
                    continue 
                next_loc_r, next_loc_c, radius2 = bombs[j]
                
                if (curr_loc_r - radius <= next_loc_r <= curr_loc_r + radius) and  (curr_loc_c - radius <= next_loc_c <= curr_loc_c + radius):
                    graph[(curr_loc_r, curr_loc_c)].append((next_loc_r, next_loc_c))
        print(graph)


        visited = set()
        memorization = {}
        def dfs(row, col, count, visited):
            
            for nei in graph[(row, col)]:
                if list(nei) not in memorization:
                    count += 1 
                    dfs(nei)
                else:
                    count  += memorization[(r_starting, c_starting)]

            memorization[(r_starting, c_starting)] = count + 1 

            return count + 1 


        
        max_ = 0 
        for bomb in bombs:
            r_starting, c_starting, radius = bomb
            if (r_starting, c_starting) in memorization:
                curr = memorization[(r_starting, c_starting)]
            else:
                curr = dfs(r_starting, c_starting, 0, set())
            max_ = max(max_, curr)

"""