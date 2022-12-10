# input:  beginword = "hit " , endword ="cog", wordlist = ["hot", "dot", "dog", "lot", "log", "cog"]
# s: hit -> "hot" -> "dot" -> "dog" -> "cog" output = 5 words
import collections
from typing import List


def wordLadderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0
    
    nei = collections.defaultdict(list)
    
    wordList.append(beginWord)
    for word in wordList:
        for j in range(len(word)):
            pattern = word[:j] + "*" + word[j + 1:]
            nei[pattern].append(word)
    
    visit = set([beginWord])
    
    q = collections.deque([beginWord])
    res = 1
    while q:
        for i in range(len(q)):
            word = q.popleft()
            if word == endWord:
                return res
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j +1:]
                for neiword in nei[pattern]:
                    if neiword not in visit:
                      visit.add(neiword)  
                      q.append(neiword)
            
        res +=1
    return 0

beginword = "hit" 
endword="cog"
wordlist = ["hot", "dot", "dog", "lot", "log", "cog"]

print(wordLadderLength(beginword, endword, wordlist))