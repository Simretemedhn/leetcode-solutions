from collections import deque, defaultdict

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:    

        def parse(edges):
            e = defaultdict(list)  
            for src, dst in edges:
                e[src].append(dst)
            return e 
            
        red = parse(redEdges)
        blue = parse(blueEdges)

        answer = [-1 for _ in range(n)]
        q = deque()
        q.append((0, 0, None))  # (node, length, prev_color)
        visit = set()
        visit.add((0, None))

        while q:
            node, length, state = q.popleft() 

            if answer[node] == -1:
                answer[node] = length 
            
            if state != "RED":
                for nei in red[node]:
                    if (nei, "RED") not in visit:
                        visit.add((nei, "RED"))
                        q.append((nei, length + 1, "RED"))

            if state != "BLUE":
                for nei in blue[node]:
                    if (nei, "BLUE") not in visit:
                        visit.add((nei, "BLUE"))
                        q.append((nei, length + 1, "BLUE"))
        return answer

