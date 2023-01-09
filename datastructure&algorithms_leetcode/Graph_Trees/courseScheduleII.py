# There are total of numCourses you have to take, labeled from 0 to numCourses-1
# some courses may have prerequisties, for example to take course 0 you have to
# first take course 1 which is expressed as a pair: [0, 1]

# given the total number of courses and a list of prerequiste pairs, 
# is it possible for you to finish all course?

# example 1:
numCourse = 5
prerequisites = [[1, 0], [0,2], [1, 3], [1, 4], [3, 4]]
# numCourse = 4, prerequisites = [[1, 0], [2, 1], [2, 0], [3, 2]]
# output = true

def courseScheduleII(numCourse: int, prerequisites: list[list[int]]):
    
    if not prerequisites:
        return [num for num in range(numCourse)]
    
    preMap= {i : [] for i in range(numCourse)}
    
    for course, preps in prerequisites:
        preMap[course].append(preps)
    
    white = set(preMap.keys())
    # currently visiting -> visited during the dfs call
    # black visiting -> already visited
    grey = set()
    black = set()
    
    order = []
    def dfs(crs, grey, black, order):
        grey.add(crs)
        
        for prep in preMap[crs]:
            if prep in black:
                continue
            
            if prep in grey:
                return False

            if not dfs(prep, grey, black, order):
               return False
           
        order.append(crs)
        grey.remove(crs)
        black.add(crs)
   
        return True
    
    while white:
        crs = white.pop()
        if crs in black:
            continue
        
        if not dfs(crs, grey, black, order):
            return False
    return order



  

numCourse = 5
prerequisites = [[1, 0], [0,2], [1, 3], [1, 4], [3, 4]]

print(courseScheduleII(numCourse, prerequisites))
