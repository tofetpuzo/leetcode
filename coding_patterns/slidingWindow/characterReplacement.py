def longestSubStringKDistinct(char: str, k: int):

    count = {}
    res = 0
    l = 0
    
    
    for r in range(len(char)):
        count[char[r]] = 1 + count.get(char[r], 0)
        windowLength = (r - l + 1)
        while windowLength  - max(count.values()) > k:
            count[char[l]] -= 1
            l +=1

        res = max(res, r - l + 1)
    return res

# input s = "aabacccac", k=1 -> output: 3 []