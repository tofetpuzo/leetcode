# Given two text1 and text2, return the length of their longest common subsequence. A subsequence of a string is a new string generated from the original string with some charcters(can be none) ("e.g "ace" is a subsquence of abcde )

# example 
# input: text= "abcde" , text2 = "ace"
# output: 3
def longestCommonSequence(text1: str, text2: str):
    dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+ 1)]
    
    for i in range(len(text1) -1, -1, -1):
        for j in range(len(text2) -1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
                
                # if they do not match
            else:
                dp[i][j] = max(dp[i][j+1], dp[i+1][j])
    
    return dp[0][0]
text1= "abcde" 
text2 = "ace"
print(longestCommonSequence(text1, text2))
# output: 3