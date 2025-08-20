# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])

        queue = deque([0])

        while queue:
            node = queue.popleft()
            
            for nb in rooms[node]:
                if nb not in visited:
                    visited.add(nb)
                    queue.append(nb)

        return len(rooms) == len(visited)