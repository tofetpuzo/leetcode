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