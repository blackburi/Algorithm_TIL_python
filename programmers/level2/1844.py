# 게임 맵 최단거리

from collections import deque

def solution(maps):
    
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    moving = deque()
    
    n = len(maps)
    m = len(maps[0])
    
    visited = [[False]*m for _ in range(n)]
    arrival = False
    
    moving.append((0, 0, 1)) # (x, y, 이동 횟수)
    
    while moving :
        x, y, length = moving.popleft()
        
        if x == n-1 and y == m-1 :
            arrival = True
            break
        
        for i in range(4) :
            mx = x + move[i][0]
            my = y + move[i][1]
            
            if 0 <= mx < n and 0 <= my < m and maps[mx][my]==1 and not visited[mx][my] :
                visited[mx][my] = True
                moving.append((mx, my, length+1))
    
    if arrival :
        return length
    else :
        return -1