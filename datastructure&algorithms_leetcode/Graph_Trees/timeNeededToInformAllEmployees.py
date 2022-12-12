# A company has n employes with a unique ID for each employee from 0 to n -1.
# The head of the company is the one with headID. Each employee has one
# direct manager given in the manager array where manager[i] is the direct manager 
# of the i-th employee, manager[headID] = -1. Also, it is guaranted that the subordination
# relationships have a tree structure.
# The head of the company wants to inform all the company employees of an urgent piece of news.
# he will inform his direct subordinates, and they will inform their subordinates, and so on
# the head of the company wants to inform all the company employes of an urgent piece of news.
# he will inform his direct subordinates, and they will inform their subordinates, so on until all of his direct subordinates, and they will inform their subordinates and so on untill all the employess know about the urgent news. (i.e. after informaTime[i] minutes )
# all his direct subordinates can start spreading the news 