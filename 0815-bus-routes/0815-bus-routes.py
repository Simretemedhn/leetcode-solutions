class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        rout = defaultdict(list)

        n = len(routes)
        for i in range(n):
            l = len(routes[i])
            for j in range(l):
                num = routes[i][j]
                rout[num].append(i)
        print(rout)
        q = deque()
        q.extend(rout[source])
        visited = set()
        visited.update(rout[source])
        level = 0 

        while q:
            n = len(q)
            level += 1 
            for _ in range(n):
                index = q.popleft()

                for member in routes[index]:
                    if member == target:
                        return level 
                    for ind in rout[member]:
                        if ind not in visited:
                            visited.add(ind)
                            q.append(ind)
        return -1 
