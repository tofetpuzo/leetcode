<<<<<<< HEAD
from typing import List
# given an array nums with n objects colored red, white or blue sort them 
# in place so that objects of the same color are adjacent with the colors
# in the order red, white and blue

# here, we will use the integers 0, 1, 2 to represent the color, red, white and respectively
# nums = [2, 0, 2, 1, 1, 0]
# output = [0, 0, 1, 1, 2,2]

def dutchFlagProblem(nums: List[int]):

    i = 1
    j = 0
    combined = []
    if len(nums) > 2:
        return nums
    
=======
def swap_index(my_list, idx1, idx2):
    temp = my_list[idx1]
    my_list[idx1] = my_list[idx2]
    my_list[idx2] = temp
    
    
def pivot_sort(my_list, pivot_index, end_idex):
    swap_idx = pivot_index
    for i in range(pivot_index+1, end_idex+1):
        if my_list[i] < my_list[pivot_index]:
            swap_idx+=1
            swap_index(my_list, swap_idx, i)
    swap_index(my_list, pivot_index, swap_idx)   
    return swap_idx

def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot_sort(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)
        quick_sort_helper(my_list,pivot_index+1, right)
    return my_list

def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)

nums = [2, 0, 2, 1, 1, 0]
print(quick_sort(nums))
>>>>>>> 92b48eb2b6764554ceb0e5443090cc1dfdca31e9
