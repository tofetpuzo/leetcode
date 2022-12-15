import collections


grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
def shortetsPathMatrix(grid: list[list[int]]):
    grid[0][0] = 1

    if grid[0][0] or grid[-1][-1]:
        return -1

    direction = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    ROWS = len(grid)
    COLS = len(grid[0])
   
    queue = collections.deque([(0, 0, 1)])

    while queue:
        row, col, path_len = queue.popleft()

        if (row, col) == (ROWS-1, COLS -1):
            return path_len

        for dr , dc in direction:
            new_r = row+ dr
            new_c = col + dc

            if new_r in range(ROWS) and new_c in range(COLS) and not grid[new_r][new_c]:
                grid[new_r][new_c] = 1

                queue.append((new_r, new_c, path_len+1))

    return -1

print(shortetsPathMatrix(grid))
