import collections
from typing import List


def numberofIslands(grid: List[List[int]]):
    ROWS , COLS = len(grid), len(grid[0])
    if not grid:
        return 0
    
    directions = [ [1, 0], [-1, 0], [0, 1],  [0, -1]]
    visit = set()
    res = 0

    def bfs(r, c):
        q= collections.deque()
        visit.add((r, c))
        q.append((r,c))

        while q:
           row, col = q.popleft()
           for dr, dc in directions:
                r, c = dr + row, col + dc
                if (r in range(ROWS) and c in range(COLS) and grid[r][c] == "1" and (r, c) not in visit):
                    q.append((r,c))
                    visit.add(r, c)


    for r in range(ROWS):
        for c in range(COLS):
            if ((r, c) not in visit and grid =="1"):
                bfs(r, c)
                res +=1

    return res


        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     # input s = "aabacccac", k=1 -> output: 3 []
