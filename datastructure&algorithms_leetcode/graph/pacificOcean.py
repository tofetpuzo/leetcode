# You are given an m x n integer matrix heights representing the height of each unit cell in a continent.
# the pacific ocean touches the continent's left and top
# edges, and the atlantic ocean touches the continent's 
# bottom edges.
# water can only flow in four directions, up, down, left and right. Water flows from a cell to an adjacent one with an equal or lower height.
# return a list of grid coordinates where water can flow to both the pacific and atlantic oceans.
# input: heights: [[1, 2, 2, 3], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
from typing import List


def pacificOcean(heights: List[List[int]]) -> List[List[int]]:
    ROWS , COLS = len(heights), len(heights[0])
    pacific_ocean , atlantic_ocean = set(), set()
    
    def dfs(r, c, visit: set, prevHeight):
        if ((r, c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or 
            heights[r][c] < prevHeight):
                return
            
        visit.add((r,c))
        dfs(r + 1, c, visit, heights[r][c])
        dfs(r - 1, c, visit, heights[r][c])
        dfs(r, c+1, visit, heights[r][c])
        dfs(r, c-1, visit, heights[r][c])
        
        
    for c in range(COLS):
        # PACIFIC OCEAN
        dfs(0, c, pacific_ocean, heights[0][c])
        dfs(ROWS-1, c, atlantic_ocean, heights[ROWS-1][c])
        
    for r in range(ROWS):
        dfs(r, 0, pacific_ocean, heights[r][0])
        dfs(r, COLS -1 , atlantic_ocean, heights[r][COLS -1])    
    
    res = []
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in pacific_ocean and (r, c) in atlantic_ocean:
                res.append([r, c])
    return res


heights= [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]             
print(pacificOcean(heights))