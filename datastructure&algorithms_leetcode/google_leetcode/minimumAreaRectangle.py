# 939. Minimum Area Rectangle
# Medium
# 1.7K
# 259
# Companies

# You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

# Return the minimum area of a rectangle formed from these points, with sides parallel to the X 
# and Y axes. If there is not any such rectangle, return 0.

# Example
# Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4

# Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2
def minAreaRect(points: list[list[int]]):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    min_size = float("inf")
    visited = set()

    for x1, y1 in points:
        for x2, y2 in visited:
            if(x1, y2) in visited and (x2 , y1) in visited:
                size = abs(x2 -x1) * abs(y2 - y1)
                min_size = min(min_size, size)
                
        visited.add((x1, y1))

    return min_size if min_size != float("inf") else 0


points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2
print(minAreaRect(points))