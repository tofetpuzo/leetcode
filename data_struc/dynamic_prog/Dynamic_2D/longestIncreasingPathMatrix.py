#  given an m x n integers matrix, return the length of the longest increasing path of the matrix. From each cell, you can either move in 4 directions: left, right, up or down , you may not move diagonally or outside the boundary

# input : matrix = [[9,9,4], [6, 6, 8], [2, 1, 1]] output : 4 -> longest path is [1, 2, 6, 9]
from typing import List


def longestIncreasingPathMatrix(matrix: List[List[int]]) -> int:
    ROWS , COLS = len(matrix) , len(matrix[0])
    dp = {} # (r,c ) -> LIP
    
    def dfs(r, c, previous_val):
        if(r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= previous_val):
            return 0
        
        if (r, c) in dp:
            return dp[(r, c)]
        
        res = 1
        res = max(res, 1 + dfs(r+1, c, matrix[r][c]))
        res = max(res, 1 + dfs(r-1, c, matrix[r][c]))
        res = max(res, 1 + dfs(r, c+1, matrix[r][c]))
        res = max(res, 1 + dfs(r, c-1, matrix[r][c]))
        
        dp[(r, c)] = res
        return res
     
    for r in range(ROWS):
        for c in range(COLS):
            dfs(r, c, -1)
    return max(dp.values())