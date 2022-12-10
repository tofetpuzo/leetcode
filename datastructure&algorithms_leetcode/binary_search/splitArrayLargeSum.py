from typing import List

def splitArray(nums: List[int] , m: int) -> int:
    def canSplit(largest):
        subArray = 0
        curSum = 0
        for n in nums:
            curSum += n
            if curSum > largest:
                subArray+=1
                curSum = n      
        return subArray + 1 <= m 
    
    l , r = max(nums) , sum(nums)
    res = r
    while l <= r:
        mid = l + ((r- l)// 2)  
        if canSplit(mid):
            res = mid
            r = mid - 1           
        else:
            l = mid + 1 
                  
    return res
            

nums = [7, 2, 5, 10, 8] 
m = 2
print(splitArray(nums=nums, m=m))