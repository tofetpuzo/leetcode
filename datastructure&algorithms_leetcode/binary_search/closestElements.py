# 658. Find K Closest Elements
# Medium
# 6.5K
# 527
# Companies

# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. 
# The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

#     |a - x| < |b - x|, or
#     |a - x| == |b - x| and a < b

#  

# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]

# Example 2:

# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]


from typing import List


def findClosestElemenets(arr: List[int], k: int, x: int):
    l, r = 0, len(arr) - k 

    while l < r:
        mid = (l + r) //2
        if x - arr[mid] >= arr[mid+k] - x:
            l = mid + 1
        else:
            r = mid
            
    return arr[l : l+k]

arr = [1, 2, 3, 4, 5] 
k = 3 
x = 3
# output = [1, 2, 3, 4]

# arr = [1, 2, 3, 4, 5] 
# k = 4 
# x = . -1
# output = [1, 2, 3, 4]

print(findClosestElemenets(arr, k, x))
