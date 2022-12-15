import collections


def killProcess(pid: list[int], ppid: list[int], kill: int):
    graph = collections.defaultdict(list)

    for idx , pare in zip(pid, ppid):
        graph[pare].append(idx)

    queue = collections.deque([kill])
    res = []

    while queue:
        to_kill = queue.popleft()

        res.append(to_kill)        

        if to_kill in graph:
            queue.extend(graph[to_kill])

    return res

pid = [1, 3, 10, 5]
ppid = [3, 0, 5, 3]

kill = 5
print(killProcess(pid, ppid, kill))
   
        
