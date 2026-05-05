from collections import defaultdict, deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        def parse(edge):
            e = defaultdict(list)
            for src, dst in edge:
                e[src].append(dst)
            return e 
        
        red = parse(redEdges)
        blue = parse(blueEdges)

        q = deque()
        q.append((0, 0, None))  
        answer = [-1] * n 
        visited = set()
        visited.add((0, None))  

        while q:
            node, length, last_color = q.popleft()
            
            if answer[node] == -1:
                answer[node] = length 

            if last_color != "red":
                for nei in red[node]:
                    if (nei, "red") not in visited:
                        visited.add((nei, "red"))
                        q.append((nei, length + 1, "red"))

            if last_color != "blue":
                for nei in blue[node]:
                    if (nei, "blue") not in visited:
                        visited.add((nei, "blue"))
                        q.append((nei, length + 1, "blue"))
        
        return answer

