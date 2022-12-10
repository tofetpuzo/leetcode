from typing import List


def findClosestElemenets(arr: List[int], k: int, x: int) -> List[int]:
    l, r = 0, len(arr) - k 

    while l < r:
        mid = (l + r) //2
        if x - arr[mid] > arr[mid+k] - x:
            l = mid + 1
        else:
            r = mid
            
    return arr[l : l+k]

arr = [1, 2, 3, 4, 5] 
k = 3 
x = 3
# output = [1, 2, 3, 4]

# arr = [1, 2, 3, 4, 5] 
# k = 4 
# x = . -1
# output = [1, 2, 3, 4]

print(findClosestElemenets(arr, k, x))
