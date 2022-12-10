from typing import List


def find132pattern(nums: List[int])-> bool:
    stack = [] # pair [ num, minLeft]
    
    curMin = nums[0]
    
    for n in nums[1:]:
        while stack and n >= stack[-1][0]:
            stack.pop()
        if stack and n > stack[-1][1]:
            return True
        
        stack.append([n, curMin])
        curMin = min(curMin, n)
        
    return False
        
nums = [-1,3,2,0]    
print(find132pattern(nums))
        
    