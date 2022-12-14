# There are total of numCourses you have to take, labeled from 0 to numCourses-1
# some courses may have prerequisties, for example to take course 0 you have to
# first take course 1 which is expressed as a pair: [0, 1]

# given the total number of courses and a list of prerequiste pairs, is it possible for you to finish all course?

# example 1:
numCourse = 5
prerequisites = [[1, 0], [0,2], [1, 3], [1, 4], [3, 4]]
# numCourse = 4, prerequisites = [[1, 0], [2, 1], [2, 0], [3, 2]]
# output = true

def courseScheduleII(numCourse: int, prerequisites: list[list[int]]):
    
    preMap= {i : [] for i in range(numCourse) }
    for course, preps in prerequisites:
        preMap[course].append(preps)

    order = []
    
    visit = set()
    def dfs(crs):
        
        if crs in visit:
            return False

        if preMap[crs] == []:
            return True
        
        visit.add(crs)
        for pre in preMap[crs]:
            if not dfs(pre): return False
        visit.remove(crs)
        preMap[crs] = []
        return True
    
    for crs in range(numCourse):
        if not dfs(crs): return False

    return True
  



print(courseScheduleII(numCourse, prerequisites))
