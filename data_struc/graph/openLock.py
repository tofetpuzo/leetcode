from collections import deque
from typing import List


def openLock(deadends: List[List[str]], target: str) -> int:
    if "0000" in deadends:
        return -1
    
    def children(lock):
        res = []
        for i in range(4):
            digit = str((int(lock[i]) + 1) % 10)
            res.append(lock[:i] + digit + lock[i+1:])
            digit = str((int(lock[i]) - 1 + 10) % 10)
            res.append(lock[:i] + digit + lock[i+1:])
            
        return res
    
    q = deque()
    q.append(["0000", 0]) #[lock, turns]
    visit = set(deadends)
    while q:
        lock, turns = q.popleft()
        if lock == target:
            return turns
        
        # the number of turns it took to get  
        for child in  children(lock):
            if child not in visit:
                visit.add(child)
                q.append([child ,turns + 1])
                
    return -1


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
# output = 6

print(openLock(deadends, target))