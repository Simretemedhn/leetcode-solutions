class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set()
        q = deque()
        q.append(0)
        visited.add(0)

        while q:
            vertix = q.popleft()

            for nei in rooms[vertix]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        return len(visited) == len(rooms)
        
        