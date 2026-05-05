class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque()
        q.append(0)
        visited = set()
        visited.add(0)

        while q:
            room = q.popleft()

            for nei in rooms[room]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        return len(visited) == len(rooms)