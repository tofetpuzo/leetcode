# you are given a list of bombs,the range of a bomb is defined as the area where its effect can be felt.
# this area is in the shape of a circle with the center as the location of the bomb. 
# the bombs are represented by a 0-indexed 2d array boombs where bombs where dombs[i] = [xi, yi, ri]
# yi and xi denote y and x coordinate of the location of the ith bomb, wheras ri denotes the radius of its range
# you may choose to denote a single boomb. when a boomb is denoted, it will detonate all bombs that lie in its range
# these boombs will further detonate the boombs that lie in their ranges.
# given the list of bombs, return the max no of bombs that can be detonated if you are allowed to detonate only one bomb.
import collections
import math


def maximumDetonation(bombs: list[list[int]]):
    graph = collections.default(list)

    for i in range(len(bombs)):
        for j in range(len(bombs)):
            if i == j:
                continue
            if bombs[i][2] >= math.sqrt((bombs[i][0] - bombs[j][0])**2 + (bombs[i][1] - bombs[j][1]) ** 2):
                graph[i].append(j)

    res = 0



    def dfs(node):
        for child in graph[node]:
            if child not in visited:
                visited.add(child)
                dfs(child)


    for i in range(len(bombs)):
        visited = set([i])
        dfs(i)
        res = max(res, len(visited))
        
    return res


            