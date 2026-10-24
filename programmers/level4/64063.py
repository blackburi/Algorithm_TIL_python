# 호텔 방 배정

import sys
sys.setrecursionlimit(200_000)

def solution(k, room_number):
    # key : 방 번호, value : 다음 방 번호
    rooms = {}    
    answer = []
    
    def find(room) :
        # 방이 비어 있다면(rooms에 없다면) 자신 반환
        if room not in rooms :
            rooms[room] = room+1
            return room
        
        # 방이 비어있지 않다면 다음 빈 방을 찾음
        empty_room = find(rooms[room])
        rooms[room] = empty_room
        return empty_room
    
    for r in room_number :
        assign = find(r)
        answer.append(assign)
    
    return answer