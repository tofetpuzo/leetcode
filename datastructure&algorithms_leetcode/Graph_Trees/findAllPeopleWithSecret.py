# you are given an integer n indicating there are n people numbered from 0 to n -1
#  you are also given a 0 - indexed 2D integer array meetings where meetings[i] = [xi, yi , timei]
# indicates that person xi and person yi have a meeting at timei.
# a person may attend multiple meetings at the same time. Finally you are given an integer firstP6erson
#
# person 0 has a secret and initially shares the secret with a person firstPerson at time O. 
# this secret is then shared every time a meeting takes place with a person that has the secret.
# more formally, for every meeting, if a person xi has the secret at timei, then they will share the secret
# with person yi, and vice versa

# the secrets are shared instanteously. That s, a person may receive the secret and share it with people 
# in other meetings within the same time frame.

# return a list of all the people that have the secret after all the meetings have taken place. 

# n = 6 , meetings =[[1, 2, 5], [2, 3, 8], [1, 5, 10]], firstPerson = 1
# output: [0, 1, 2, 3, 5]
import collections
from typing import List


def findAllPeopleWithSecret(meetings: List[List[int]], firstPerson: int):
    meetings.sort(key=lambda x : x[2])
    
    meeting_dict = collections.defaultdict(list)
    
    for person1, person2, time in meetings:
        meeting_dict[time].append([person1, person2])
        
    has_secret = set((0, firstPerson))
    
    for times, meetings_persons in meeting_dict.items():
        graph = collections.defaultdict(list)
        seen = set()
        
        for person_1, person_2 in meetings_persons:
            graph[person_1].append(person_2)
            graph[person_2].append(person_1)
            if person_1 in has_secret:
                seen.add(person_1)
                
            if person_2 in has_secret:
                seen.add(person_2)
        
        queue = collections.deque(seen)
        while queue:
            person = queue.popleft()
            
            for nei in graph[person]:
                if nei not in has_secret:
                    has_secret.add(nei)
                    queue.append(nei)
    
    return list(has_secret)
                    
            
        
        
        
    

    


meetings = [[1, 2, 5], [2, 3, 8], [1, 5, 10]]
firstPerson = 1
print(findAllPeopleWithSecret(meetings, 2))