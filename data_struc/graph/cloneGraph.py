# given a reference of a node in a connected undirected graph, return a deep(clone) of the graph.
# each node in the graph contains a val(int) and a list(List[node])
class Node:
    def __init__(self, neighbors, value) -> None:
        self.value = value
        self.neighbors = neighbors if neighbors is not None else []

    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            # a clone of the graph does not exist.
            copy = Node(node.value)
            oldToNew[node] = copy

            # make copies of every single neighbors.
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node) if node else None
