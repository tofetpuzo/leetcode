# you are given an array of integers nums, there is a sliding window of size k 
# which moving from the very left of the array to the very right. You can only see the k numbers 
# in the window. Each time the sliding window moves right by one positon. return the max sliding window


# [1, 3, 3, 5, 5, 6, 7]

import collections
from typing import List


def slidingWindows(nums: List[int], k : int):
    N = len(nums)
    l = r = 0

    output = []
    queue = collections.deque()

    while r < N:
        
        # pop smaller values from queue
        while queue and nums[queue[-1]] < nums[r]:
            queue.pop()
        queue.append(r)

        # remove left val from window
        if l > queue[0]:
            queue.popleft()

        if (r + 1) >= k:
            output.append(nums[queue[0]])
            l+=1
        
        r+=1

    return output


nums = [1, 3, -1, -3, 5, 3 , 6, 7]
k = 3
print(slidingWindows(nums, k))