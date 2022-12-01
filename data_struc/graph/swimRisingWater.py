import heapq
from typing import List


def swimRisingWater(grid: List[List[int]]) -> int:
    ROWS , COL = len(grid), len(grid[0])
    visit = set()
    minHeap = [[grid[0][0], 0, 0]] #(time/ height, r, c)
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visit.add((0,0))
    
    while minHeap:
        t, r, c = heapq.heappop(minHeap)
        if r == ROWS -1 and c == COL -1:
            return t
        
        for dr , dc in directions:
            neiR, neiC = r+dr, c+dc
            if (neiR < 0 or neiC < 0 or neiR == ROWS or neiC == COL or (neiR, neiC) in visit):
                continue
            visit.add((neiR, neiC))
            heapq.heappush(minHeap, [max(t, grid[neiR][neiC]), neiR, neiC])
            
            
grid = [[0, 2], [1, 3]]

print(swimRisingWater(grid))