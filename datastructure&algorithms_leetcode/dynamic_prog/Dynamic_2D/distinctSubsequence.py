# given two strings s and t, return the number of distinct subsquence of s which equals t
# input: s = "rabbbit" , t = "rabbit"
# output: 3
# explanation 
# there are 3 ways you can generate "rabbit" from s

# rabb b it , ra b bbit, rab b bit
def distinctSubsequence(s: str, t: str):
    cache = {}
    def dfs(i, j):
        if j == len(t):
            return 1
        
        if i == len(s):
            return 0
        
        if (i, j) in cache:
            return cache[(i, j)]
        
        if s[j] == t[j]:
            cache[(i, j)] = dfs(i+1, j+1) + dfs(i, j+1) 
            
        else:
            cache[(i, j)] = dfs(i+1, j)
        
        return cache[(i, j)]
    
    return dfs(0, 0)