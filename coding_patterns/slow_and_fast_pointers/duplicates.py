from typing import List


def duplicates(nums: List[int]):
    # this is a linked list algorithm
    #

    # find the point the two intersect at 
    slow , fast = 0, 0
    while True:
        if (slow < 0 or fast < 0 or slow >len(nums) or fast >len(nums)):
            return False
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            return True

        fast = nums[nums[fast]]

        if slow == fast:
            return True
   
        return False
    

    # while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        # if slow == fast:
        #     break
    # slow2 = 0
    # while True:
    #     slow = nums[slow]
    #     slow2 = nums[slow2]
    #     if slow == slow2:
    #         return True
    #     else:
    #         return False
    
nums = [2, -1, 1, 2]

print(duplicates(nums))