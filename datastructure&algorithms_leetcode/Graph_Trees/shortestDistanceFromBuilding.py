# you are given an m x n grid of values 0, 1, 2 where:
# each 0 marks an empty land that you can pass by freely
# each 1 marks a building that you cannot pass through and
# each 2 marks an obstacle that you cannot pass through
# you want to build a house on an empty land that reaches all buildings in the shortest total travel distance
# you can only move up , down left and right
# return the shortest travel distance for such a house. if it is possible to build such a house according to the above rules, 
# return 1. the total distance is the sum of the distance between the houses of the friends and the meeting point
# Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0

# Output: 7

# Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
# the point (1,2) is an ideal empty land to build a house, as the total
# travel distance of 3+3+1=7 is minimal. So return 7.
import collections
from typing import List


def shortestDistanceFromBuilding(grid: List[List[int]]):
    ROWS , COLS = len(grid), len(grid[0])

    dist_matrix = [[0] * COLS for row in range(ROWS)]
    if not grid:
        return 0
    
    directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

    BUILDING = 1
    OBSTACLE = 2
    EMPTY_LAND = 0
    min_dist = float("inf")


    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == BUILDING:
                local_dist = float("inf")
                q = collections.deque([(row, col , 0)])


                while q:
                    cur_row, cur_col, dist = q.popleft()
                    for dr, dc in directions:
                        r, c = dr+cur_row , dc+cur_col
                        if (r in range(ROWS) and c in range(COLS) and grid[r][c] == EMPTY_LAND):
                            grid[r][c] -=1
                            dist_matrix[r][c] += dist + 1
                            q.append((r, c, dist + 1))
                            
                           
                            local_dist = min(local_dist, dist_matrix[r][c])
                            

                EMPTY_LAND-=1
                min_dist = local_dist

    return min_dist if min_dist != float("inf") else -1

grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

print(shortestDistanceFromBuilding(grid))
