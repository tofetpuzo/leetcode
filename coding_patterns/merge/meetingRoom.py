# given an array of meeting time intervals consisting of start and end times [[s1, e1], [s2, e2]]

# find mininum number of conference room required
# 
# interval = [(0, 30), (5, 10), (15, 20)]
# output = 2
# explanation we need two meeting rooms 
# room1 : (0, 30)
# room2: (5, 10), (15, 20) 


from typing import List


def meetingRoom(intervals: List[tuple[int]]):
    start = sorted([i for i in intervals])
    end = sorted([i for i in intervals])
    res, output = 0, 0
    s , e = 0, 0
    while s < len(intervals):
        if start[s] < end[e]:
            s +=1
            output+=1
        else:
            e +=1
            output -=1

        res = max(res, output)
    return res

