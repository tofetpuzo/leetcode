class Graph:
    def __init__(self, num_nodes, edges) -> None:
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        for node1, node2 in edges:
            self.data[node1].append(node2)
            self.data[node2].append(node1)

    def __repr__(self) -> str:
        return "\n".join(["{}: {}".format(nodes, nei) for nodes, nei in enumerate(self.data)])

    def __str__(self) -> str:
        return self.__repr__()

    def add_edges(self, node1, node2, edges):
        for node, nei in enumerate(self.data):
            # 4, 5
            if node1 == node:
                if node2 not in nei:
                    self.data[node].append(node2)
            if node2 == node:
                if node1 not in nei:
                    self.data[node].append(node1)
            # if (node1, node2) not in edges:
            #     self.data.append([node1, node2])
            #     self.num_nodes += 1
            #     break
        # for _, _ in edges:
        #     self.data[node1].insert(node2)
        #     self.data[node2].insert(node1)

            # self.num_nodes += 1


num_nodes = 5

edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]

graph = Graph(5, edges)
print(graph)
print("===")
# graph.add_edges(node1=4, node2=5, edges=edges)
# graph.add_edges(node1=2, node2=3, edges=edges)
# print(graph)


def bfs(graph, root):
    queue = []
    visited = [False] * len(graph.data)
    distance = [None] * len(graph.data)
    parent = [None] * len(graph.data)
    visited[root] = True
    queue.append(root)
    index = 0
    distance[root] = 0

    while index < len(queue):
        current = queue[index]
        index += 1
        # check all edges of current
        for node in graph.data[current]:
            if not visited[node]:
                distance[node] = 1 + distance[current]
                parent[node] = current
                visited[node] = True
                queue.append(node)
    return queue, distance, parent


print(bfs(graph, 2))


def dfs(graph, root):
    stack = []
    visited = [False] * len(graph.data)
    parent = [None] * len(graph.data)
    stack.append(root)
    result = []
    
    while len(stack) > 0:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            result.append(current)
            for node in graph.data[current]:
                parent[node] = current
                if not visited[node]:
                    stack.append(node)
                
    return result 
            
        