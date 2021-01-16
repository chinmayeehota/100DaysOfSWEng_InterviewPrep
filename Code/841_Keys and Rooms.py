class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False] *len(rooms)
        print(seen)
        print(type(seen))
        seen[0] = True
        stack =[0]
        while stack:
            room = stack.pop()
            for ele in rooms[room]:
                if not seen[ele]:
                    seen[ele] = True
                    stack.append(ele)
        return all(seen)