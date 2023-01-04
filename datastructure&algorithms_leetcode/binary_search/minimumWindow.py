# Minimum Window Substring
# Given a string corpus and a string target, find the minimum window (substring) which contain all the characters that are found in target.

# The time complexity of the solution should be in order of O(n).


# NOTE: substring and  sub-sequence are different things


# Example 1:
# Input: corpus = "donutsandwafflemakemehungry"  target = "flea"

# Output: "affle" or "flema" 

# Example 2:
# Input: corpus = "whoopiepiesmakemyscalegroan"  target = "roam"

# Output: "myscalegro"  

# Example 3:
# Input: corpus = "coffeeteabiscuits"  target = "cake"

# Output: ""  
# Explanation: since the letter k is not found in the corpus, a minimum window cannot be found.


import collections
import sys




def minWindow(searchString, t):
    '''
    :type searchString: str
    :type t: str
    :rtype: str
    '''
    left = 0
    right = 0
    
    # It stores the length of maximum valid substring 
    minimum = sys.maxsize
    counter_t = collections.Counter(t)
    counter_search = collections.defaultdict(int)
    count = 0
    minimum_window = ""

    # Here we use the 2 pointers approach
    while right < len(searchString):
        print(counter_search)
        counter_search[searchString[right]] += 1
        if searchString[right] in counter_t: 
            # r : Counter({'r': 1, 'o': 1, 'a': 1, 'm': 1})
    # {'w': 1, 'h': 1, 'o': 2, 'p': 1, 'i': 1}) : Counter({'r': 1, 'o': 1, 'a': 1, 'm': 1})
            if counter_search[searchString[right]] <= counter_t[searchString[right]]:
                count += 1
        
        while left <= right and count == len(t):
            if minimum > right - left + 1:
                minimum = right - left + 1
                minimum_window = searchString[left : right + 1]
            
            counter_search[searchString[left]] -= 1
            if searchString[left] in counter_t and counter_search[searchString[left]] < counter_t[searchString[left]]:
                count-=1
                
            left += 1
        
        right += 1
        print(counter_search, counter_t)
        
    return minimum_window

corpus = "whoopiepiesmakemyscalegroan" 
target = "roam"
print(minWindow(corpus, target))

# counter_t = collections.Counter(t)
# counter_search = collections.defaultdict(int)
# counter_search[searchString[right]]: {'w': 0, 'h': 0, 'o': 1, 'p': 0, 'i': 0, 'e': 1, 's': 1, 'm': 0, 'a': 2, 'k': 0, 'y': 1, 'c': 1, 'l': 1, 'g': 1, 'r': 1, 'n': 1}) 
# Counter({'r': 1, 'o': 1, 'a': 1, 'm': 1})