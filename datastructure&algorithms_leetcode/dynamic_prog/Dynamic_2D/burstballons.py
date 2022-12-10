# You are given n ballons, indexed from 0 to n-1. Each ballon is painted
# with a number on it represented by an array nums. You are asked
#  to burst all the ballons
# if you burst the ith ballon, you will get adj= nums[i -1] * nums[i] * nums[i +1]
# coins. if i - 1 or i +1 goes out of the array, then treat it as if
# there is a ballon with a 1 painted on it
# return the maximum coins you can collect

# input nums = [3, 1, 5, 8]
# output : 167

# nums = [3, 1, 5, 8] -> [3, 5, 8] -> [3, 5] -> [3, 8] -> [8]-> []
# coins = 3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 167

from typing import List


def maxCoins(nums: List[int]) -> int:
    nums = [1] + nums + [1]
    dp = {}
    
    def dfs(l, r):
        if l > r: 
            return 0
        
        if (l, r) in dp:
            return dp[(l, r)]
        
        dp[(l, r)] = 0
        for i in range(l, r +1):
            coins = nums[l -1] * nums[i] * nums[r+1]   
            coins += dfs(l, i+1) + dfs(i, r+1)
            dp[(l, r)] = max(dp[(l, r)], coins)
        return dp[(l, r)]
        
    return dfs(1, len(nums) -2)
