def bs(graph, root):
    visited = [root]
    queue =[root]
    
    while queue:
        root_node = queue.pop(0)
        print(root_node)
        for adjacent_node in graph[root_node]:
            if adjacent_node not in visited:
                visited.append(adjacent_node)
                queue.append(adjacent_node)


def ds(graph, root):
    visited = [root]
    stack =[root]   
    while stack:
        root_node = stack.pop()
        print(root_node)
        for adjacent_node in graph[root_node]:
            if adjacent_node not in visited:
                visited.append(adjacent_node)
                stack.append(adjacent_node)
                   
customDict = {"a": ["b", "c"],
              "b": ["a", "d", "e"],
              "c": ["a", "e"],
              "d": ["d", "f", "e"],
              "e": ["d", "f"],
              "f": ["d", "e"]
              }

ds(customDict, "a")
print("--")
bs(customDict, "a")
# print(graph.gdict["e"], end="\n")