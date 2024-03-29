# 1091. Shortest Path in Binary Matrix
# Medium
# 4.3K
# 180
# Companies

# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

#     All the visited cells of the path are 0.
#     All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

# The length of a clear path is the number of visited cells of this path.

#  

# Example 1:

# Input: grid = [[0,1],[1,0]]
# Output: 2

# Example 2:

# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4

# Example 3:

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1

import collections


def shortestPathBinaryMatrix(grid):

    if grid[0][0] and grid[-1][-1]:
        return -1

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    queue = collections.deque([(0, 0, 1)])
    rows = len(grid) -1
    cols = len(grid[0]) -1

    grid[0][0] = 1

    while queue:
        x, y, path_len = queue.popleft()

        if (x, y) == (rows, cols):
            return path_len
        
        for dr , dc in directions:
            new_rol = dr + x
            new_col = dc + y

            if(0 <= new_rol < rows+1 ) and (0 <= new_col < cols+1) and not grid[new_rol][new_col]:
                grid[new_rol][new_col] = 1
                queue.append((new_rol, new_col, path_len+1))

    return -1

grid = [[0,0,0],[1,1,0],[1,1,0]]
print(shortestPathBinaryMatrix(grid))


        
