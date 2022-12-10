from collections import deque
from typing import List


def rottenOranges(grid: List[List[int]]) -> int:
    q = deque()
    time, fresh = 0, 0
    ROWS, COLS = len(grid), len(grid[0])

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append([r, c])

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while q and fresh > 0:
        for _ in range(len(q)):
            # this removes the most recent rotten oranges
            r, c = q.popleft()
            for dr, dc in directions:
                # adj cols and rows
                row, col = r+dr, c+dc
                # if in bounds and fresh, make rotten
                if (row < 0 or row == len(grid) or col < 0
                        or col == len(grid[0]) or grid[row][col] != 1):
                    continue

                grid[row][col] = 2
                q.append([row, col])
                fresh -= 1

        time += 1

    return time if fresh == 0 else -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

print(rottenOranges(grid))
