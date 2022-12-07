from typing import List


def circularArray(nums: List[int]):
    def isPostive(no):
        return True if no > 0 else False

    for index in range(len(nums)):
        i = index
        if nums[i] != 0:
            is_Positive = isPostive(nums[i])
            current = (i + nums[i]) % len(nums)
            print(current, i , nums[i] , len(nums))
            nums[i] = 0
            was_in_loop = False
            while nums[current] != 0 and isPostive(nums[current]) == is_Positive:
                was_in_loop = True
                temp = nums[current]
                nums[current] = 0
                current = (current+temp) % len(nums)
                print(current, temp , len(nums))
            if current == i and was_in_loop:
                return True

    return False


nums = [2, -1, 1, 2, 24]
# nums = [-1, -2, -3, -4, -5, 6]

print(circularArray(nums))