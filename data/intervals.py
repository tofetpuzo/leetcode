# 56. Merge Intervals
# Medium

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

from typing import List

# s = [[1,3],[2,6],[8,10],[15,18]]
# 
s = [[1,4],[1,4]]
# s = [[1,4],[4,5]]
# s = [[1,3]]
# s = [[1,4],[0,4]]
# s = [[1,4],[5,6]]

def intervals(s: List[List[int]]):
    combined = []
    i = 1
    j = 0
    
    if len(s) < 2:
        return s
    
    for lists in range(len(s) -1):
        list1 = s[lists]
        list2 = s[lists+1]
       
                
        while i < len(list1) and j < len(list2):
            # [[1,3],[2,6],[8,10],[15,18]]        
                
            if list1[i] >= list2[j] and list2[j] > list1[i - 1]:
                combined.append([list1[i-1] , list2[-1]])
                i+=1
                break
            
            if list2[j] < list1[i - 1]:
                combined.append([list2[j] , list1[i]])
                j+=1
                break
             
            else:     
                combined.extend([list1, list2])
                break
                
                
        while lists:          
            combined.append(list2)
            lists-=1
            break

    return combined
                         
print(intervals(s))