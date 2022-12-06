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
    