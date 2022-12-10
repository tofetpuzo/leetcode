import collections
from typing import List


def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    graph = collections.defaultdict(set)
    
    email_to_name = {}
    
    for account in accounts:
        name = account[0]
        for email in account[1:]:
            graph[email].add(account[1])
            graph[account[1]].add(email)
            email_to_name[email] = name
            
    res = []
    visit = set()
    
    for email in graph:
        if email not in visit:
            stack = [email]
            visit.add(email)
            
            local_res = []
            
            while stack:
                node = stack.pop()
                local_res.append(node)
                
                for edge in graph[node]:
                    if edge not in visit:
                        stack.append(edge)
                        visit.add(edge)
            res.append([email_to_name[email]] + sorted(local_res))
    
    return res
                        
accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
accounts1 = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]

print(accountsMerge(accounts))          
    
    