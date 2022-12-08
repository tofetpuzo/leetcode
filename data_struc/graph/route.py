# you are given an array routes representing bus routes where routes[i] is a bus route 
# that the ith repeats forever. For example, if routes[0] = [1, 5, 7], this means that 
# the 0th bus travels the sequence 1-> 5-> 7-> 1->5->7->1 ... forever. You will start
# at the bus stop source (you are not on any bus initially ) and you want to go to 
# the bus stop target. You can travel between bus stops by buses only. 
# return the least number of buses you must take you take to travel from source to target.
# return -1 if it is not possible.
# input: routes = [[1, 2, 7], [3, 6, 7]] , source = 1, target = 6
# output = 2
from collections import defaultdict, deque
from typing import List


def routers(routes: List[List[int]], source: int, target: int):
    stop = set()
    bus = set()

    if source == target:
        return 0

    graph = defaultdict(set)
    queue = deque([source, 0])

    for bus, route in enumerate(routes):
        for stop in route:
            graph[stop].add(bus)
    
    while queue:
        stop, route_len queue.popleft()