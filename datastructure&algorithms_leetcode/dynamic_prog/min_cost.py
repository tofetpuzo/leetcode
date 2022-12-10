from typing import List


def min_cost(cost: List[int]) -> int:
    cost.append(0)
    # [10, 15, 20] 0
    
    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost  , cost[i+2])
        
    return min(cost[0], cost[1])
        
