# 215. Kth Largest Element in an Array
# Medium
# 12.8K
# 642
# Companies

# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# You must solve it in O(n) time complexity.

#  

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

import collections
import heapq

def findKthLargest(nums: list, k: int):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # x=len(nums)-k
        # heapq.heapify(nums)
        # for i in range(x):
        #     heapq.heappop(nums)
        # return heapq.heappop(nums)

        idx = 0   
        queue = collections.deque()

        if len(nums) == 1:
           return nums[0]

        if len(nums) == 2:       
           return nums[1]

        for i in range(len(nums) -1):
        #     [1, 2, 4, 5]
            if nums[i] >= nums[i + 1]:
                continue
            else:
                idx+=1
                if idx == k:
                   queue.append(nums[:i+2])
        return queue[-1][-2]
          


# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k = 4
nums = [3,2,1,5,6,4]
k = 2



print(findKthLargest(nums, k))