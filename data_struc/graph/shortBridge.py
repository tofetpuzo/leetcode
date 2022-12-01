from collections import deque
from typing import List


def shortestBridge(grid: List[List[int]]) -> int:
    N = len(grid)
    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    def invalid(r, c):
        return r < 0 or c < 0 or r == N or c == N
    
    visit = set()
    def dfs(r, c):
        if (invalid(r, c) or not grid[r][c] or (r,c) in visit):
            return
        
        visit.add((r, c))
        for dr, dc in direction:
            dfs(r+dr, c + dc)
            
    
    def bfs():
        length_of_bridge , q = 0 , deque(visit)
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in direction:
                    curR, curC = r + dr, c + dc
                    if invalid(curR, curC) or (curR, curC) in visit:
                        continue
                    if grid[curR][curC]:
                        return length_of_bridge
                    q.append([curR, curC])
                    visit.add((curR, curC))
                    
            length_of_bridge+=1
        
        
    for r in range(N):
        for c in range(N):
            if grid[r][c]:
                dfs(r,c)
                return bfs()

grid = [[0,1, 0], [0, 0, 0], [0, 0, 1]]

print(shortestBridge(grid))