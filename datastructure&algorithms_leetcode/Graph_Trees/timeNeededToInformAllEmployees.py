# A company has n employes with a unique ID for each employee from 0 to n -1.
# The head of the company is the one with headID. Each employee has one
# direct manager given in the manager array where manager[i] is the direct manager 
# of the i-th employee, manager[headID] = -1. Also, it is guaranted that the subordination
# relationships have a tree structure.
# The head of the company wants to inform all the company employees of an urgent piece of news.
# he will inform his direct subordinates, and they will inform their subordinates, and so on
# the head of the company wants to inform all the company employes of an urgent piece of news.
# he will inform his direct subordinates, and they will inform their subordinates, so on until all of his direct subordinates, and they will inform their subordinates and so on untill all the employess know about the urgent news. (i.e. after informaTime[i] minutes )
# all his direct subordinates can start spreading the news ).
# return the number of minutes needed to inform all the employess about the urgent news.


# Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
# Output: 1
# Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs 1 minute to inform them all.
# The tree structure of the employees in the company is shown.

import collections

def numofMinutes(n: int, headID: int , manager: list[int], informTime: list[int]):
    if n <= 1:
        return 0
    
    res = 0
    graph = collections.defaultdict(list)
    
    for idx , parent in enumerate(manager):
        graph[parent].append(idx)
        

    queue = collections.deque([(headID, informTime[headID])])
    while queue:
        cur_emp , cur_time = queue.popleft()
        
        res = max(res, cur_time)
        for emp in graph[cur_emp]:
            queue.append((emp, cur_time + informTime[emp]))
    
    return res
        
n = 6
headID = 2 
manager = [2,2,-1,2,2,2]
informTime = [0,0,1,0,0,0]  
print(numofMinutes(n=n, headID=headID, manager=manager, informTime=informTime))
        