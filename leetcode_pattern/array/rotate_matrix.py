# 48. Rotate Image
# Medium
# Topics
# Companies
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:


# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


# Constraints:

# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.9M
# Submissions
# 2.6M
# Acceptance Rate
# 76.1%


# def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:
#     matrix.reverse()
#     for i in range(len(matrix)):
#         for j in range(i):
#             print(i, j)
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#     return matrix


def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    end = n - 1

    for row in range(n // 2):
        for col in range(row, end - row):
            temp = matrix[row][col]
            matrix[row][col] = matrix[end - col][row]
            matrix[end - col][row] = matrix[end - row][end - col]
            matrix[end - row][end - col] = matrix[col][end - row]
            matrix[col][end - row] = temp
    return matrix


print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

"""
 [[1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]]
    reversed:
    [[7, 8, 9], 
    [4, 5, 6], 
    [1, 2, 3]]
   
    [[7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]]
    

"""