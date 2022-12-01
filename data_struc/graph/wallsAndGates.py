
from collections import deque
from typing import List


def wallsAndGates(room: List[List[int]]):
    
    ROWS, COLS = len(room), len(room[0])
    visit = set()
    q = deque()
    
    
    def addRoom(r, c):
        if(r< 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visit or room[r][c] == -1):
            return
        
        visit.add((r,c))
        q.append([r,c])
        
    for r in range(ROWS):
        for c in range(COLS):
            if room[r][c] == 0:
                q.append([r, c])
                visit.add((r,c))
                
    dist = 0
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            room[r][c] = dist
            
            addRoom(r+1, c)
            addRoom(r-1, c)
            addRoom(r, c+1)
            addRoom(r, c-1)
            
        dist +=1
        return dist
        
rooms = [[21474833647, -1, 0, 21474833647],[21474833647, 21474833647,21474833647,-1], [0, -1,21474833647,-1] ]

print(wallsAndGates(rooms))