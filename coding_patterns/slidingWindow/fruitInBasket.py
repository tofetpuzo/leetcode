# [1, 2, 3, 2, 2 ]
# output : 2
# we can collect [2, 3, 3, 2]

# [3, 3, 3, 1, 2, 1, 1, 2, 3,3,4] 
# output: 5 , [1, 2, 1, 1, 2]
#              s  
#                 e
from typing import List


def totalFruit(tree: List[int]):
    count = 0
    max_len = 0
    count = {}
    start = end = 0
    while end < len(tree):
        count[tree[end]] = end
        if len(count) >= 3:
            min_val = min(count.values())
            del count[tree[min_val]]
            start = min_val + 1
        max_len = max(max_len, end - start + 1)
        end +=1
    return max_len

    

