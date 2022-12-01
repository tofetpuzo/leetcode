# 1936. Add Minimum Number of Rungs
# You are given a strictly increasing integer array rungs that represents the height of rungs on a ladder. You are currently on the floor at height 0, and you want to reach the last rung.

# You are also given an integer dist. You can only climb to the next highest rung if the distance between where you are currently at (the floor or on a rung) and the next rung is at most dist. You are able to insert rungs at any positive integer height if a rung is not already there.

# Return the minimum number of rungs that must be added to the ladder in order for you to climb to the last rung.

# Input: rungs = [1,3,5,10], dist = 2
#  
 
from typing import List


def addRungs(rungs: List[int], dist: int) -> int:
    for a, b in zip(rungs, [0] + rungs):
        print(a, b, (a - b - 1)// dist)
    return sum((a - b - 1) // dist for a, b in zip(rungs, [0] + rungs))

rungs = [1,3,5,10]
# [3,4,6,7], [3,6,8,10]
dist = 2
print(addRungs(rungs, dist))
    