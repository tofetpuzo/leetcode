from typing import List


def duplicates(nums: List[int]):
    # this is a linked list algorithm
    #

    # find the point the two intersect at 
    slow , fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
        else:
            return False


    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            break
        else:
            return False
    
    return True

