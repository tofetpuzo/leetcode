# an image is represented by 2 D-ARRAY of integers, each integer reprs the 
# pixel value of the image(from 0 to 65535). Given a coordinate(sr, sc) the 
# starting pixel(row and column) of the flood fill and a pixel value new color, "flood fill the image" 
# to perform a flood fill, consider the starting pixel , plus any pixel connected 4 - directionally to the starting pixel of the same color 
# as the starting pixel, plus any pixels connected 4 - directionally to those pixels (also with the same color as the starting pixel) and so on. Replace the color of all the aforementioned pixels with the newColor
#  at the end, return the modified image
# image = [[1, 1, 1], [1, 1 , 0], [1, 0, 1]] sr = 1, sc = 1, newColor = 2
# output [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

from typing import List


def floodFill(grid: List[List[int]], sr: int, sc: int, newColor:  int):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    color = grid[sr][sc]
    
    if color == newColor:
       return grid
    
    def dfs(r, c):
        if grid[r][c] == color:
            grid[r][c] = newColor   
            if r >= 1: 
                dfs(r-1, c)
            if c >= 1: 
                dfs(r, c-1)
            if r + 1 < rows: 
                dfs(r+1, c)
            if c + 1< cols: 
                dfs(r, c+1)
            
        return grid
        
        
    dfs(sr, sc)
    return grid
        
image = [[1, 1, 1], [1, 1 , 0], [1, 0, 1]] 
sr = 1 
sc = 1
newColor = 2 

print(floodFill(image, sr, sc, newColor))     
        
        
 
        
        