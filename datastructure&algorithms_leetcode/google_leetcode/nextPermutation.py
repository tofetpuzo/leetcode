# 31. Next Permutation
# Medium
# 13.9K
# 3.9K
# Companies

# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

#     For example, for arr = [1,2,3], the following are all the permutations of
#    arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

# The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
#
# More formally, if all the permutations of the array are sorted in one container according to their lexicographical order,
# then the next permutation of that array is the permutation that follows it in the sorted container.
# If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

#     For example, the next permutation of arr = [1,2,3] is [1,3,2].
#     Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
#     While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.

# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

#  [2, 3, 1] [2, 1, 3]
#                   ^
#  [1, 2, 3] is [1, 3, 2].
#                   ^
#  algorithm
# step 1: let pointer be set to last
# step 2: check if last number is >= num[i - 1]
# return exactly number

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]

# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]

# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]

def swap(nums, id1, id2):
    temp = nums[id1]
    nums[id1] = nums[id2]
    nums[id2] = temp

#  [2, 3, 1] [2, 1, 3] ans [3,1,2]
#                   ^
#  [1, 2, 3] is [1, 3, 2].

#  algorithm
# step 1: let pointer be set to last
# step 2: check if last number is >= first
# but make sure that the first is > next[id1+1]
# return list
# def check(nums, first , last):
#     if nums[first] <= nums[last]:
#         nums[first] , nums[last] = nums[last], nums[first]
#     return True

# def nextPermutation(nums)
#     l , r = 0, len(nums) -1
#     first = 0
#     # step 1: let pointer be set to last
#     while l <= r or first < r :
#         if nums[r] <= nums[l]:     
#             nums[l], nums[r] = nums[r] , nums[l]  
#             l+=1     
#             if check(nums, first , r) and nums[first] >= nums[first+1]:
#                 swap(nums, first , first+1)
#                 nextPermutation(nums)
#                 return nums
#             else:
#                 if nums[first] <= nums[first+1]:
#                     swap(nums, first , first+1)
#                     first+=1        
#         else:
#             if nums[r -1] < nums[r]:
#                 nums[r-1] , nums[r] = nums[r] , nums[r -1]
                

#         r+=1
             
#         return nums


def reverse(nums, begin, end):
    while begin < end:
        swap(nums, begin, end)
        begin+=1
        end -=1

def permutation(nums):
    if len(nums) == 1:
        return
    if len(nums) == 2:
        return swap(nums, 0, 1)

    dec = len(nums) - 2
    while dec >= 0 and nums[dec] >= nums[dec+1]:
        dec -=1
    reverse(nums, dec+1, len(nums) -1)
    if dec == -1:
        return
    num_next = dec + 1
    while num_next < len(nums) and nums[num_next] <= nums[dec]:
        num_next +=1
    swap(nums, num_next, dec)

    return nums



# nums = [2, 3, 1]
# nums = [3,2,1]
# nums = [1, 2, 3]
# nums = [9, 1,1,1,5]
nums = [1, 2, 7, 9, 6, 4, 1] 
# output = [1, 2, 9, 1, 4, 6, 7]

# nums = [1, 7, 9, 9, 8, 3]
# output = [1, 8, 3, 7, 9, 9]
# print(nextPermutation(nums))
# print(reverse(nums, 0, len(nums)))
print(permutation(nums))

