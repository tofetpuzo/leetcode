import collections
from typing import List


def shortestPathBinaryMatrix(grid: List[List[int]]):
    if grid[0][0] or grid[-1][-1]:
        return -1
    
    queue = collections.deque([])
    