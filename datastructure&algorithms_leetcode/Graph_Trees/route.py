# you are given an array routes representing bus routes where routes[i] is a bus route 
# that the ith repeats forever. For example, if routes[0] = [1, 5, 7], this means that 
# the 0th bus travels the sequence 1-> 5-> 7-> 1->5->7->1 ... forever. You will start
# at the bus stop source (you are not on any bus initially ) and you want to go to 
# the bus stop target. You can travel between bus stops by buses only. 
# return the least number of buses you must take you take to travel from source to target.
# return -1 if it is not possible.
routes = [[1, 2, 7], [3, 6, 7]] 
source = 1
target = 6
# output = 2
from collections import defaultdict, deque
from typing import List


def routers(routes: List[List[int]], source: int, target: int):
    visited_stop = set()
    visited_bus = set()

    if source == target:
        return 0

    graph = defaultdict(set)
    queue = deque([(source, 0)])

    for bus, route in enumerate(routes):
        for stop in route:
            graph[stop].add(bus)
    
    while queue:
        stop, route_len = queue.popleft()
        if stop == target:
            return route_len

        for bus in graph[stop]:
            if bus not in visited_bus:
                visited_bus.add(bus)
            for stop in routes[bus]:
                if stop not in visited_stop:
                    visited_stop.add(stop)
                    queue.append((stop, route_len+1))

    return -1

print(routers(routes , source, target))

# def mergeAccount(accounts: List[List[str]]):

#     email_to_name = {}
    
#     graph = defaultdict(set)

#     for account in accounts:
#         name = account[0]
#         for email in account[1:]:
#              graph[email].add(account[1])
#              graph[account[1]].add(email)
#              email_to_name[email] = name

#     visited = set()
#     res = []
#     for email in graph:
#         if email not in visited:
#             stack = [email]
#             visited.add(email)
#             local_res = []
#             while stack:
#                 node = stack.pop()
#                 local_res.append(node)
#                 for edge in graph[node]:
#                     if edge not in visited:
#                         stack.append(edge)
#                         visited.add(edge)
#             res.append([email_to_name[email] + sorted(local_res)])

#     return res

                

            
