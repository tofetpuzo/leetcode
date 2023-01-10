# 93. Shortest Path in a Grid with Obstacles Elimination
# Hard
# 3.9K
# 71
# Companies

# You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). 
# You can move up, down, left, or right from and to an empty cell in one step.

# Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1)
#  given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

#  

# Example 1:

# Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
# Output: 6

# Explanation: 
# The shortest path without eliminating any obstacle is 10.
# The shortest path with one obstacle elimination at position (3,2) is 6. 
# Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

# Example 2:

# Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
# Output: -1
# Explanation: We need to eliminate at least two obstacles to find such a walk.
import collections


def shortestPath(self, grid: list[list[int]], k):
    """
    :type grid: List[List[int]]
    :type k: int
    :rtype: int
    """
    rows = len(grid)
    cols = len(grid[0])

    target = (rows-1, cols-1)

    if k >= (rows-1) + (cols-1):
        return rows + cols -2

    # the first 0 is for total number of paths taken

    queue = collections.deque([(0, (0, 0, k))])
    seen = set([(0, 0, k)])
    direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    while queue:
        steps, (row, col, removal_left) = queue.popleft()
        if (row, col) == target:
            return steps
        
        for dr, dc in directions:
            new_row = dr + row
            new_col = dr + col

            if(0<= new_row< rows) and (0< new_col<= cols):
                new_removals = removal_left - grid[new_row][]

        