# given a string, find the length of the longest substring
# that contains at most k distinct characters
# input: s ="ece baa" , k = 2 -> output: 3 [ece, baa]
# input: s = "aabacccac", k=2 -> output: 6 [ab, aba, ba, acccac]
# input s = "aabacccac", k=1 -> output: 3 []
from collections import defaultdict


def longestSubStringKDistinct(char: str, k: int):
    if len(char) == 0 or k == 0: return 0
    startIdx = endIdx = 0

    seen = defaultdict(int)
    res = 0

    while endIdx < len(char):
        if char[endIdx] not in seen:
            k -=1
        seen[char[endIdx]] = endIdx

        # shrinking the window
        while k < 0:
            if seen[char[startIdx]] == startIdx:
                k+=1
                del seen[char[startIdx]]
            startIdx +=1
            
        res = max(res, endIdx - startIdx +1)
        endIdx +=1
    return res

            
