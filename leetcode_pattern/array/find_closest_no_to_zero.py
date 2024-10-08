# 2239. Find Closest Number to Zero
# Easy
# Topics
# Companies
# Hint
# Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.


# Example 1:

# Input: nums = [-4,-2,1,4,8]
# Output: 1
# Explanation:
# The distance from -4 to 0 is |-4| = 4.
# The distance from -2 to 0 is |-2| = 2.
# The distance from 1 to 0 is |1| = 1.
# The distance from 4 to 0 is |4| = 4.
# The distance from 8 to 0 is |8| = 8.
# Thus, the closest number to 0 in the array is 1.
# Example 2:

# Input: nums = [2,-1,1]
# Output: 1
# Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.


from os import close


def find_closest_no_to_zero(nums: list[int]) -> int:
    # nums.sort(key=lambda x: (abs(x), -x))
    # return nums[0]

    closest = float("inf")

    for num in nums:
        if abs(num) < abs(closest):
            closest = num
        elif abs(num) == abs(closest):
            closest = max(num, closest)
    return closest


nums = [-4, -2, 1, 4, 8]
# output = 1
print(find_closest_no_to_zero(nums))

n = [2, -1, 1]
# output = 1
print(find_closest_no_to_zero(n))

ns = [-3, -2, -5, 90, 4, 8]

print(find_closest_no_to_zero(ns))
