class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visit = set([0])
        q = deque([0])

        while q:
            room = q.popleft()

            for key in rooms[room]:
                if key not in visit:
                    visit.add(key)
                    q.append(key)


        return len(visit) == n

        