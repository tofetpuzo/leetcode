# A robot is located at the top-left corner of a m x n grid(marked 'start' in the 
# diagram below) the robot can only move either down or right at any point in time. 
# the robot is trying to reach the bottom right corner of the grid (marked finish in the diagram below).

# how many possible unique paths are there?

# start # # # # #
# #     # # # # #
# #     # # # # #

def unique_paths(m: int,  n: int) :
    row = [1] * n 
    for _ in range(m -1):
        newRow = [1] * n
        for j in range(n-2, -1, -1):
            newRow[j] = newRow[j+1] + row[j] 
        row = newRow
    return row[0]

print(unique_paths(5, 9))